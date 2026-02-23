WTX
crates.io docs license rustc Tests

A collection of different transport implementations and related tools focused primarily on web technologies. Features the in-house development of 6 IETF RFCs (6265, 6455, 7541, 7692, 8441, 9113), 3 formal specifications (gRPC, MySQL, PostgreSQL) and several other invented ideas.

Works on embedded devices with heap allocators. If you find this crate interesting, please consider giving it a star ⭐ on GitHub.

Comparisons
In a way, WTX can be seen as an amalgamation that consolidates the functionality of several other web development projects into a single toolkit. Take a look at the following table to see how some built-from-scratch implementations compare with other similar projects.

Technology	Similar Projects	Feature (wtx)
Client API Framework	N/A	client-api-framework
Database Client	jdbc, odbc, sqlx	postgres, mysql
Database Schema Manager	flyway, liquibase, refinery	schema-manager
gRPC	grpc, tonic	grpc-client, grpc-server
HTTP Client Pool	reqwest	http-client-pool
HTTP Server Framework	axum, spring-boot, fastapi	http-server-framework
HTTP/2	h2, nghttp2	http2
WebSocket	tokio-tungstenite, uWebSockets	web-socket-handshake
Note that all features are optional and must be set at compile time. For more information, take a look at the documentation available at https://c410-f3r.github.io/wtx.

Performance
Many things that generally improve performance are used in the project, to name a few:

Manual vectorization: When an algorithm is known for processing large amounts of data, several experiments are performed to analyze the best way to split loops in order to allow the compiler to take advantage of SIMD instructions in x86 processors.
Memory allocation: Whenever possible, all heap allocations are called only once at the start of an instance creation and additionally, stack memory usage is preferably prioritized over heap memory.
Fewer dependencies: No third-party is injected by default. In other words, additional dependencies are up to the user through the selection of Cargo features, which decreases compilation times. For example, you can see the mere 13 dependencies required by the PostgreSQL client using cargo tree -e normal --features postgres.
Since memory are usually held at the instance level instead of being created and dropped on the fly, its usage can growth significantly depending on the use-case. If appropriated, try using a shared pool of resources or try limiting how much data can be exchanged between parties.

High-level benchmarks
Checkout wtx-bench to see a variety of benchmarks or feel free to point any misunderstandings or misconfigurations.

WebSocket Benchmark

There are mainly 2 things that impact performance, the chosen runtime and the number of pre-allocated bytes. Specially for servers that have to create a new instance for each handshake, pre-allocating a high number of bytes for short-lived or low-transfer connections can have a negative impact.

PostgreSQL Benchmark

Low-level benchmarks
Anything marked with #[bench] in the repository is considered a low-level benchmark in the sense that they measure very specific operations that generally serve as the basis for other parts.

Take a look at https://bencher.dev/perf/wtx to see all low-level benchmarks over different periods of time.

Development benchmarks
These numbers provide an estimate of the expected waiting times when developing with WTX. If desired, you can compare them with other similar Rust projects through the dev-bench.sh script.

Technology	Required Deps 1	All Deps 2	Clean Check	Clean Debug Build	Clean Opt Build	Opt size
Client API Framework	0	31	6.42s	7.79s	8.45s	872K
gRPC Client	2	16	4.80s	6.04s	6.53s	736K
HTTP Client Pool	2	15	4.60s	5.84s	6.44s	728K
HTTP Server Framework	2	34	7.87s	10.53s	10.60s	996K
Postgres Client	13	26	5.12s	6.19s	6.69s	652K
WebSocket Client	10	22	4.24s	5.04s	5.31s	560K
Transport Layer Security (TLS)
When using a feature that requires network connection, it is often necessary to perform encrypted communication and since WTX is not hard-coded with a specific stream implementation, it is up to you to choose the best TLS provider.

Some utilities like TokioRustlsConnector or TokioRustlsAcceptor are available to make things more convenient but keep in mind that it is still necessary to activate a crate that provides certificates for client usage.

Examples
Demonstrations of different use-cases can be found in the wtx-instances directory as well as in the documentation.

Limitations
Does not support systems with a pointer length of 16 bits.

Expects the infallible sum of the lengths of an arbitrary number of slices, otherwise the program will likely trigger an overflow that can possibly result in unexpected operations. For example, in a 32bit system such a scenario should be viable without swap memory or through specific limiters like ulimit.

Internal dependencies required by the feature. ↩

The sum of optional and required dependencies used by the associated binaries. ↩








Calendar
Provides basic primitives to work with time-related operations.

Date: Proleptic Gregorian calendar. Can represent years from -32767 to 32766.

DateTime: ISO-8601 representation with timezones.

Duration: Time span in nanoseconds. Can be negative unlike core::time::Duration.

Instant: A specific point in time. Contains the underlying mechanism that provides a timestamp.

Time Clock time with nanosecond precision.

Also supports arithmetic operations and flexible formatting.

Example
//! Basic time operation.

extern crate wtx;

use wtx::calendar::{Duration, Instant};

fn main() -> wtx::Result<()> {
  println!(
    "ISO 8601 representation of the next 2 minutes in UTC: {}",
    Instant::now_date_time(0)?.add(Duration::from_minutes(2)?)?
  );
  Ok(())
}



Client API Framework
A flexible client API framework for writing asynchronous, fast, organizable, scalable and maintainable applications. Supports several data formats, transports and custom parameters.

Checkout the wtx-apis project to see a collection of APIs based on wtx.

To use this functionality, it is necessary to activate the client-api-framework feature.

Objective
It is possible to directly decode responses using built-in methods provided by some transport implementations like reqwest or surf but as complexity grows, the cost of maintaining large sets of endpoints with ad-hoc solutions usually becomes unsustainable. Based on this scenario, wtx comes into play to organize and centralize data flow in a well-defined manner to increase productivity and maintainability.

For API consumers, the calling convention of wtx endpoints is based on fluent interfaces which makes the usage more pleasant and intuitive.

Moreover, the project may in the future create automatic bindings for other languages in order to avoid having duplicated API repositories.

Example

//! Illustrates how the `client-api-framework` feature facilitates the management and utilization
//! of large API endpoints for both HTTP and WebSocket requests.
//!
//! Contains one API called `GenericThrottlingApi` and its two endpoints: an HTTP JSON-RPC
//! `genericHttpRequest` and an WebSocket `genericWebSocketSubscription`.
//!
//! Everything that is not inside `main` should be constructed only once in your program.

extern crate serde;
extern crate tokio;
extern crate wtx;

use core::time::Duration;
use tokio::net::TcpStream;
use wtx::{
  client_api_framework::{
    Api,
    misc::{Pair, RequestCounter, RequestLimit},
    network::{HttpParams, WsParams, transport::SendingReceivingTransport},
  },
  de::format::SerdeJson,
  http::client_pool::{ClientPoolBuilder, ClientPoolTokio},
  misc::Uri,
  rng::Xorshift64,
  web_socket::{WebSocket, WebSocketBuffer, WebSocketConnector},
};

wtx::create_packages_aux_wrapper!();

#[derive(Debug)]
#[wtx::api(error(wtx::Error), pkgs_aux(PkgsAux), transport(http, ws))]
pub struct GenericThrottlingApi {
  pub rc: RequestCounter,
}

impl Api for GenericThrottlingApi {
  type Error = wtx::Error;
  type Id = GenericThrottlingApiId;

  async fn before_sending(&mut self) -> Result<(), Self::Error> {
    self.rc.update_params().await?;
    Ok(())
  }
}

#[wtx::pkg(
  data_format(json_rpc("genericHttpRequest")),
  id(crate::GenericThrottlingApiId),
  transport(http)
)]
mod generic_http_request {
  #[pkg::aux]
  impl<A, DRSR> crate::HttpPkgsAux<A, DRSR> {}

  #[derive(Debug, serde::Serialize)]
  #[pkg::req_data]
  pub struct GenericHttpRequestReq(#[pkg::field(name = "generic_number")] i32);

  #[pkg::res_data]
  pub type GenericHttpRequestRes = (u8, u16, u32);
}

#[wtx::pkg(
  data_format(json_rpc("genericWebSocketSubscription")),
  id(crate::GenericThrottlingApiId),
  transport(ws)
)]
mod generic_web_socket_subscription {
  #[pkg::aux]
  impl<A, DRSR> crate::WsPkgsAux<A, DRSR> {}

  #[derive(Debug, serde::Serialize)]
  #[pkg::req_data]
  pub struct GenericWebSocketSubscriptionReq<'str> {
    generic_string: &'str str,
    #[serde(skip_serializing_if = "Option::is_none")]
    generic_number: Option<i32>,
  }

  #[pkg::res_data]
  pub type GenericWebSocketSubscriptionRes = u64;
}

async fn http_pair()
-> Pair<PkgsAux<GenericThrottlingApi, SerdeJson, HttpParams>, ClientPoolTokio<fn(&()), ()>> {
  Pair::new(
    PkgsAux::from_minimum(
      GenericThrottlingApi {
        rc: RequestCounter::new(RequestLimit::new(5, Duration::from_secs(1))),
      },
      SerdeJson,
      HttpParams::from_uri("ws://generic_web_socket_uri.com".into()),
    ),
    ClientPoolBuilder::tokio(1).build(),
  )
}

async fn web_socket_pair() -> wtx::Result<
  Pair<
    PkgsAux<GenericThrottlingApi, SerdeJson, WsParams>,
    WebSocket<(), Xorshift64, TcpStream, WebSocketBuffer, true>,
  >,
> {
  let uri = Uri::new("ws://generic_web_socket_uri.com");
  let web_socket = WebSocketConnector::default()
    .connect(TcpStream::connect(uri.hostname_with_implied_port()).await?, &uri)
    .await?;
  Ok(Pair::new(
    PkgsAux::from_minimum(
      GenericThrottlingApi {
        rc: RequestCounter::new(RequestLimit::new(40, Duration::from_secs(2))),
      },
      SerdeJson,
      WsParams::default(),
    ),
    web_socket,
  ))
}

#[tokio::main]
async fn main() -> wtx::Result<()> {
  let mut hp = http_pair().await;
  let _http_response_tuple = hp
    .trans
    .send_pkg_recv_decode_contained(
      &mut hp.pkgs_aux.generic_http_request().data(123).build(),
      &mut hp.pkgs_aux,
    )
    .await?
    .result?;

  let mut wsp = web_socket_pair().await?;
  let _web_socket_subscription_id = wsp
    .trans
    .send_pkg_recv_decode_contained(
      &mut wsp.pkgs_aux.generic_web_socket_subscription().data("Hello", None).build(),
      &mut wsp.pkgs_aux,
    )
    .await?
    .result?;
  Ok(())
}







Database Client
Provides a set of functions that establish connections, execute queries and manage data transactions in different databases.

Benchmark

Independent benchmarks are available at https://github.com/diesel-rs/metrics.

PostgreSQL
Implements a subset of https://www.postgresql.org/docs/16/protocol.html. PostgreSQL is a robust, open-source relational database management system that, among other things, supports several data types and usually also excels in concurrent scenarios.

To use this functionality, it is necessary to activate the postgres feature.

Example
//! Demonstrates different interactions with a PostgreSQL database.

extern crate tokio;
extern crate wtx;
extern crate wtx_instances;

use wtx::{
  database::{Executor as _, Record, Records},
  misc::into_rslt,
};

#[tokio::main]
async fn main() -> wtx::Result<()> {
  let uri = "postgres://USER:PASSWORD@localhost/DATABASE";
  let mut executor = wtx_instances::executor_postgres(uri).await?;
  executor
    .transaction(|this| async {
      this.execute_ignored("CREATE TABLE IF NOT EXISTS example(id INT, name VARCHAR)").await?;
      this
        .execute_stmt_none("INSERT INTO foo VALUES ($1, $2), ($3, $4)", (1u32, "one", 2u32, "two"))
        .await?;
      Ok(((), this))
    })
    .await?;
  let records = executor
    .execute_stmt_many("SELECT id, name FROM example", (), |_| Ok::<_, wtx::Error>(()))
    .await?;
  let record0 = into_rslt(records.get(0))?;
  let record1 = into_rslt(records.get(1))?;
  assert_eq!((record0.decode::<_, u32>(0)?, record0.decode::<_, &str>("name")?), (1, "one"));
  assert_eq!((record1.decode::<_, u32>("id")?, record1.decode::<_, &str>(1)?), (2, "two"));
  Ok(())
}
MySQL
Implements a subset of https://dev.mysql.com/doc/dev/mysql-server/latest/. MySQL is also a robust, open-source relational database management system generally used in web applications.

WTX includes CI coverage for MariaDB and Percona, as such, interactions with these MySQL-based databases shouldn’t be a problem.

To use this functionality, it is necessary to activate the mysql feature.

Example
//! Demonstrates a MySQL query.

extern crate tokio;
extern crate wtx;
extern crate wtx_instances;

use wtx::database::{Executor, Record, Records};
use wtx_instances::executor_mysql;

#[tokio::main]
async fn main() -> wtx::Result<()> {
  let mut executor = executor_mysql("mysql://USER:PASSWORD@localhost/DATABASE").await?;
  let records = executor
    .execute_stmt_many("SELECT id, name FROM example", (), |_| Ok::<_, wtx::Error>(()))
    .await?;
  assert_eq!(records.get(0).as_ref().and_then(|record| record.decode("id").ok()), Some(1));
  assert_eq!(records.get(1).as_ref().and_then(|record| record.decode("name").ok()), Some("two"));
  Ok(())
}
Batch
Only PostgreSQL supports the sending of multiple statements in a single round-trip.

MariaDB has MARIADB_CLIENT_STMT_BULK_OPERATIONS but it only prevents one round trip of a single statement.
The X protocol (MySQL) is not implemented at the current time and is also not supported by MariaDB or PerconaDB.
MULTI_STATEMENT, from the Client/Server protocol, does not allow multiple prepared statements.
//! Sends multiple commands at once and awaits them.

extern crate tokio;
extern crate wtx;
extern crate wtx_instances;

use wtx::{
  collection::ArrayVectorU8,
  database::{Record, Records},
  misc::into_rslt,
};

const COMMANDS: &[&str] = &["SELECT 0 = $1", "SELECT 1 = $1", "SELECT 2 = $1"];

#[tokio::main]
async fn main() -> wtx::Result<()> {
  let uri = "postgres://USER:PASSWORD@localhost/DATABASE";
  let mut executor = wtx_instances::executor_postgres(uri).await?;
  let mut batch = executor.batch();
  let mut idx: u32 = 0;
  let mut records = ArrayVectorU8::<_, { COMMANDS.len() }>::new();
  for cmd in COMMANDS {
    batch.stmt(cmd, (idx,))?;
    idx = idx.wrapping_add(1);
  }
  batch.flush(&mut records, |_| Ok(())).await?;
  for record in records {
    assert_eq!(into_rslt(record.get(0))?.decode::<_, bool>(0)?, true);
  }
  Ok(())
}
Tests
The #[wtx::db] macro automatically migrates and seeds individual tests in isolation to allow concurrent evaluations.

Its current state is limited to PostgreSQL tests that use the standard std::net::TcpStream along side the built-in executor.

Required features: executor, macros, postgres and schema-manager-dev. Connected users must have the right to create new databases.


//! The DB isolation provided by `#[wtx::db]` allows the concurrent execution of identical queries
//! without causing conflicts.
//!
//! The `dir` parameter is optional.

fn main() {}

#[cfg(test)]
mod tests {
  use std::net::TcpStream;
  use wtx::database::{
    Executor, Record,
    client::postgres::{ExecutorBuffer, PostgresExecutor},
  };

  #[wtx::db(dir("../.test-utils"))]
  async fn first_test(conn: PostgresExecutor<wtx::Error, ExecutorBuffer, TcpStream>) {
    common(conn).await;
  }

  #[wtx::db(dir("../.test-utils"))]
  async fn second_test(conn: PostgresExecutor<wtx::Error, ExecutorBuffer, TcpStream>) {
    common(conn).await;
  }

  #[wtx::db(dir("../.test-utils"))]
  async fn third_test(conn: PostgresExecutor<wtx::Error, ExecutorBuffer, TcpStream>) {
    common(conn).await;
  }

  async fn common(mut conn: PostgresExecutor<wtx::Error, ExecutorBuffer, TcpStream>) {
    conn
      .execute_ignored(
        "
        CREATE TABLE foo(id INT PRIMARY KEY, description TEXT NOT NULL);
        INSERT INTO foo VALUES (1, 'BAR!');
    ",
      )
      .await
      .unwrap();
    let id: &str = conn.execute_single("SELECT * FROM foo").await.unwrap().decode(0).unwrap();
    assert_eq!(id, "1");
  }
}





Encrypted Connections
It usually isn’t straightforward to stablish encrypted connections with PostgreSQL or MySQL, worse yet, wtx has a set of limited SSL policies that doesn’t allow the by-passing of invalid certificates.

The following sections will briefly demonstrate how to configure both servers and clients to establish encrypted connections using self-signed certificates with Podman or Docker. Most of the procedures can be adapted for non-containerized environments and also for certificates issued by trusted actors.

In case of doubt, always remember that a server needs a key and a certificate while both parties need a root authority certificate. Sometimes even a CA certificate isn’t necessary.

Generate certificates
Just an example, you can use other tools like cert-manager or other algorithms like ed25519.

CERTS_DIR="SOME_DIRECTORY"
openssl req -newkey rsa:2048 -nodes -subj "/C=FI/CN=vahid" -keyout $CERTS_DIR/key.pem -out $CERTS_DIR/key.csr
openssl x509 -signkey $CERTS_DIR/key.pem -in $CERTS_DIR/key.csr -req -days 1825 -out $CERTS_DIR/cert.pem
openssl req -x509 -sha256 -nodes -subj "/C=FI/CN=vahid" -days 1825 -newkey rsa:2048 -keyout $CERTS_DIR/root-ca.key -out $CERTS_DIR/root-ca.crt
cat <<'EOF' >> $CERTS_DIR/localhost.ext
authorityKeyIdentifier=keyid,issuer
basicConstraints=CA:FALSE
subjectAltName = @alt_names
[alt_names]
DNS.1 = localhost
IP.1 = 127.0.0.1
EOF
openssl x509 -req -CA $CERTS_DIR/root-ca.crt -CAkey $CERTS_DIR/root-ca.key -in $CERTS_DIR/key.csr -out $CERTS_DIR/cert.pem -days 1825 -CAcreateserial -extfile $CERTS_DIR/localhost.ext
rm $CERTS_DIR/key.csr
rm $CERTS_DIR/localhost.ext
rm $CERTS_DIR/root-ca.srl
MySQL
Let’s start with a my.cnf file that tells, among other things, where the certificates are located. MySQL permits the placement of my.cnf in a set of pre-configured paths but here we will put it in /etc/mysql.

[mysqld]
ssl-ca=/var/lib/mysql/root-ca.crt
ssl-cert=/var/lib/mysql/cert.pem
ssl-key=/var/lib/mysql/key.pem
Then you need to place these certificates in the container at the specified location AND set the same files as read-only for the current user. As far as I can tell, there are three possible ways.

Create a custom Docker image.
List a set of volume mappings along side some initial script.
Inline certificates in docker-entrypoint-initdb.d
Let’s use option 3 for the sake of simplicity with a script named setup.sh.

#!/usr/bin/env bash

echo "Contents of the generated root CA certificate file" > /var/lib/mysql/root-ca.crt
echo "Contents of the generated certificate file" > $/var/lib/mysql/cert.pem
echo "Contents of the generated key file" > /var/lib/mysql/cert.pem

chown mysql:mysql /var/lib/mysql/cert.pem /var/lib/mysql/key.pem
chmod 0600 /var/lib/mysql/cert.pem /var/lib/mysql/key.pem
Everything should be ready on the server side.

podman run \
  --name SOME_CONTAINER_NAME \
  -d \
  -e MYSQL_DATABASE=SOME_DATABASE \
  -e MYSQL_PASSWORD=SOME_PASSWORD \
  -e MYSQL_ROOT_PASSWORD=SOME_ROOT_PASSWORD \
  -e MYSQL_USER=SOME_USER \
  -p 3306:3306 \
  -v SOME_DIRECTORY/my.cnf:/etc/mysql/my.cnf \
  -v SOME_DIRECTORY/setup.sh:/docker-entrypoint-initdb.d/setup.sh \
  docker.io/library/mysql:9
Now it is just a matter of including the root CA certificate in the wtx client. With everything properly configured, a successful encrypted connection should be expected.

async fn tls() {
  let uri = UriRef::new("SOME_URI");
  let mut rng = ChaCha20::from_os().unwrap();
  let _executor = MysqlExecutor::<crate::Error, _, _>::connect_encrypted(
    &Config::from_uri(&uri).unwrap(),
    ExecutorBuffer::new(usize::MAX, &mut rng),
    &mut rng,
    TcpStream::connect(uri.hostname_with_implied_port()).await.unwrap(),
    |stream| async {
      Ok(
        crate::misc::TokioRustlsConnector::default()
          .push_certs(include_bytes!("SOME_DIRECTORY/root-ca.crt"))
          .unwrap()
          .connect_without_client_auth(uri.hostname(), stream)
          .await
          .unwrap(),
      )
    },
  )
  .await?;
}
PostgreSQL
The steps for PostgreSQL are almost the same of MySQL. One major difference is the fact that postgresql.conf (my.cnf counterpart) is created on the fly instead of being mapped as a volume.

With the above MySQL instructions and the following PostgreSQL snippets an encrypted connection should be properly established.

#!/usr/bin/env bash

echo "Contents of the generated root CA certificate file" > $PGDATA/root-ca.crt
echo "Contents of the generated certificate file" > $PGDATA/cert.pem
echo "Contents of the generated key file" > $PGDATA/cert.pem

chmod 0600 $PGDATA/cert.pem $PGDATA/key.pem

cat >> "$PGDATA/postgresql.conf" <<-EOF
ssl = on
ssl_ca_file = 'root-ca.crt'
ssl_cert_file = 'cert.pem'
ssl_key_file = 'key.pem'
EOF

podman run \
  --name SOME_CONTAINER_NAME \
  -d \
  -e POSTGRES_DB=SOME_DB \
  -e POSTGRES_PASSWORD=SOME_PASSWORD \
  -p 5432:5432 \
  -v SOME_DIRECTORY/setup.sh:/docker-entrypoint-initdb.d/setup.sh \
  docker.io/library/postgres:18





  Database Schema Management
Embedded and CLI workflows using raw SQL commands. A schema manager is a tool thats allows developers to define, track and apply changes to database structures over time, ensuring consistency across different environments.

To use this functionality, it is necessary to activate the schema-manager feature.

CLI
# Example

cargo install --git https://github.com/c410-f3r/wtx --features schema-manager-dev wtx-ui
echo DATABASE_URI="postgres://USER:PASSWORD@localhost:5432/DATABASE" > .env
RUST_LOG=debug wtx-cli migrate
The CLI application expects a configuration file that contains a set of paths where each path is a directory with multiple migrations.

# wtx.toml

migration_groups = [
  "migrations/1__initial",
  "migrations/2__fancy_stuff"
]
Each provided migration and group must contain an unique version and a name summarized by the following structure:

// Execution order of migrations is dictated by their numeric declaration order.

migrations
+-- 1__initial (Group)
    +-- 1__create_author.sql (Migration)
    +-- 2__create_post.sql (Migration)
+-- 2__fancy_stuff (Group)
    +-- 1__something_fancy.sql (Migration)
wtx.toml
The SQL file itself is composed by two parts, one for migrations (-- wtx IN section) and another for rollbacks (-- wtx OUT section).

-- wtx IN

CREATE TABLE author (
  id INT NOT NULL PRIMARY KEY,
  added TIMESTAMPTZ NOT NULL,
  birthdate DATE NOT NULL,
  email VARCHAR(100) NOT NULL,
  first_name VARCHAR(50) NOT NULL,
  last_name VARCHAR(50) NOT NULL
);

-- wtx OUT

DROP TABLE author;
One cool thing about the expected file configuration is that it can also be divided into smaller pieces, for example, the above migration could be transformed into 1__author_up.sql and 1__author_down.sql.

-- 1__author_up.sql

CREATE TABLE author (
  id INT NOT NULL PRIMARY KEY,
  added TIMESTAMPTZ NOT NULL,
  birthdate DATE NOT NULL,
  email VARCHAR(100) NOT NULL,
  first_name VARCHAR(50) NOT NULL,
  last_name VARCHAR(50) NOT NULL
);
-- 1__author_down.sql

DROP TABLE author;
migrations
+-- 1__some_group (Group)
    +-- 1__author (Migration directory)
        +-- 1__author_down.sql (Down migration)
        +-- 1__author_up.sql (Up migration)
        +-- 1__author.toml (Optional configuration)
wtx.toml
Library
The library gives freedom to arrange groups and uses some external crates, bringing ~10 additional dependencies into your application. If this overhead is not acceptable, then you probably should discard the library and use the CLI binary instead as part of a custom deployment strategy.

extern crate tokio;
extern crate wtx;

use std::path::Path;
use wtx::database::{schema_manager::Commands, DEFAULT_URI_VAR};
use wtx::collection::Vector;

#[tokio::main]
async fn main() {
  let mut commands = Commands::with_executor(());
  commands.migrate_from_dir(Path::new("my_custom_migration_group_path")).await.unwrap();
}
Embedded migrations
To make deployment easier, the final binary of your application can embed all necessary migrations through the binary that is available in the wtx-ui crate.

extern crate wtx;

// This is an example! The actual contents are filled by the `wtx-ui embed-migrations` binary call.
mod embedded_migrations {
  pub(crate) static GROUPS: wtx::database::schema_manager::EmbeddedMigrationsTy = &[];
}

use wtx::database::schema_manager::Commands;
use wtx::collection::Vector;

async fn migrate() -> wtx::Result<()> {
  Commands::with_executor(()).migrate_from_groups(embedded_migrations::GROUPS).await
}
Conditional migrations
If one particular migration needs to be executed in a specific set of databases, then it is possible to use the -- wtx dbs parameter in a file.

-- wtx dbs mssql,postgres

-- wtx IN

CREATE SCHEMA foo;

-- wtx OUT

DROP SCHEMA foo;
Repeatable migrations
Repeatability can be specified with -- wtx repeatability SOME_VALUE where SOME_VALUE can be either always (regardless of the checksum) or on-checksum-change (runs only when the checksums changes).

-- wtx dbs postgres
-- wtx repeatability always

-- wtx IN

CREATE OR REPLACE PROCEDURE something() LANGUAGE SQL AS $$ $$

-- wtx OUT

DROP PROCEDURE something();
Keep in mind that repeatable migrations might break subsequent operations, therefore, you must known what you are doing. If desirable, they can be separated into dedicated groups.

migrations/1__initial_repeatable_migrations
migrations/2__normal_migrations
migrations/3__final_repeatable_migrations
Namespaces/Schemas
For supported databases, there is no direct user parameter that inserts migrations inside a single database schema but it is possible to specify the schema inside the SQL file and arrange the migration groups structure in a way that most suits you.

-- wtx IN

CREATE TABLE cool_department_schema.author (
  id INT NOT NULL PRIMARY KEY,
  full_name VARCHAR(50) NOT NULL
);

-- wtx OUT

DROP TABLE cool_department_schema.author;











Environment Variables
EnvVars allows the insertion of environment variables into a custom structure where the name of the fields match the name of the variables. .env files are also supported but they should be restricted to development environments.

The unsafe std::env::set_var function is not invoked due to concerns about concurrent access, therefore, direct usage of std::env::var is not recommended unless:

EnvVars is not used at all.
There are no .env files.
A specific variable is always originated from the current process.
Example

//! `EnvVars` allows the interactive reading of environment variables.

extern crate wtx;

use std::sync::OnceLock;
use wtx::{
  calendar::{DateTime, Utc},
  misc::EnvVars,
};

static VARS: OnceLock<Vars> = OnceLock::new();

fn main() -> wtx::Result<()> {
  let _rslt = VARS.set(EnvVars::from_available()?.finish());
  let Vars { now, origin, port, rust_log } = VARS.wait();
  println!("`NOW={now:?}`, `ORIGIN={origin}`, `PORT={port}` and `RUST_LOG={rust_log:?}`");
  Ok(())
}

#[derive(Debug, wtx::FromVars)]
struct Vars {
  #[from_vars(map_now)]
  now: Option<DateTime<Utc>>,
  origin: String,
  #[from_vars(map_port)]
  port: u16,
  rust_log: Option<String>,
}

fn map_now(var: String) -> wtx::Result<DateTime<Utc>> {
  Ok(DateTime::from_iso8601(var.as_bytes())?)
}

fn map_port(var: String) -> wtx::Result<u16> {
  Ok(var.parse()?)
}





Error Handling
The majority of operations performed by WTX is fallible, in other words, most functions or methods return a Result enum instead of panicking under the hood. A considerable effort is put to hint the compiler that a branch is unreachable to optimize code generation but that is another topic.

Due to this characteristic downstream users are encouraged to create their own Error enum with a WTX variant along side a From trait implementation. Not to mention the unlocking of the useful ? operator that performs the automatic conversion of any supported error element.

extern crate wtx;

use wtx::de::FromRadix10;

#[derive(Debug)]
pub enum Error {
    MyDogAteMyHomework,
    RanOutOfCoffee,
    Wtx(wtx::Error)
}

impl From<wtx::Error> for Error {
    fn from(from: wtx::Error) -> Self {
        Self::Wtx(from)
    }
}

fn main() -> Result<(), Error> {
    let _u16_from_bytes = u16::from_radix_10(&[49][..])?;
    let _u16_from_i8 = u16::try_from(1i8).map_err(wtx::Error::from)?;
    Ok(())
}
All these conventions are of course optional. If desired everything can be unwrapped using the Result::unwrap method.

When you encounter an error, try take a look at the available documentation of that specific error (https://docs.rs/wtx/latest/wtx/enum.Error.html). If the documentation didn’t help, feel free to reach out for potential improvements.






Executor
Simple dependency-free runtime intended for tests, toy programs and demonstrations. Performance is not a main concern and you should probably use other executors like tokio.

To use this functionality, it is necessary to activate the executor feature.

Example

//! The `executor` feature allows the execution of asynchronous operations

extern crate wtx;
extern crate wtx_instances;

#[wtx::main]
async fn main() {
  println!("Hello from program!");
}

#[wtx::test]
async fn test_with_runtime(runtime: &wtx::executor::Runtime) {
  runtime
    .spawn_threaded(async move {
      println!("Hello from test!");
    })
    .unwrap();
}






HTTP Client Pool
High-level pool of HTTP clients where multiple connections that can be referenced in concurrent scenarios.

Reuses valid connections and recycles dropped communications to minimize contention and latency. Instances are created on-demand and maintained for subsequent requests to the same host.

Also useful because HTTP/2 and HTTP/3 expect long-lived sessions by default unlike HTTP/1.

To use this functionality, it is necessary to activate the http-client-pool feature.

Example

//! Fetches and prints the response body of a provided URI.
//!
//! Currently, only HTTP/2 is supported.

extern crate tokio;
extern crate wtx;
extern crate wtx_instances;

use wtx::{
  http::{HttpClient, ReqBuilder, ReqResBuffer, client_pool::ClientPoolBuilder},
  misc::{Uri, from_utf8_basic},
};

#[tokio::main]
async fn main() -> wtx::Result<()> {
  let uri = Uri::new("SOME_URI");
  let pool = ClientPoolBuilder::tokio(1).build();
  let res = pool.send_req_recv_res(ReqResBuffer::empty(), ReqBuilder::get(uri.to_ref())).await?;
  println!("{}", from_utf8_basic(&res.rrd.body)?);
  Ok(())
}








HTTP Server Framework
A small and fast to compile framework that can interact with many built-in features.

Databases
JSON
Middlewares
Streaming
URI router
WebSocket
If dynamic or nested routes are needed, then please activate the matchit feature. Without it, only simple and flat routes will work.

To use this functionality, it is necessary to activate the http-server-framework feature.

HTTP/2 Benchmarks

Endpoints
Under the hood every endpoint transforms a Request (Body, Method, Headers, Uri) into a Response (Body, Headers, StatusCode) and users can perform a finer control over this process.

Input
You will get what you declare as input. Everything else is previously sanitized.

async fn health() {}
The above example accepts nothing () as input parameter, which automatically implies a sanitization of the received request.

extern crate wtx;

use wtx::http::{ReqResBuffer, server_framework::State};

async fn print_request(state: State<'_, (), (), ReqResBuffer>) {
  println!("Request: {:?}", &state.req);
}
On the other hand, the above example gives you access to the full request. This also implies that you should be responsable for data management.

Output
Determines how responses are constructed. Similar to input handling, the output defines what clients receive.

For instance, this endpoint returns a simple Hello as the response body along side an implicit 200 OK status. No headers are sent.

async fn hello() -> &'static str {
  "Hello"
}
There are many other types of outputs that perform different operations. Please see the documentation for a full listening.

Buffers
A key consideration is that the buffers used for receiving requests are the same ones utilized for constructing responses, which means, among other things:

If the response body is equal to or smaller than the request body in size, a memory allocation can be avoided, potentially improving runtime performance.
If you use State with VerbatimParams or DynParams::Verbatim, then you should probably be careful to avoid leaking request information into responses.
extern crate wtx;

use wtx::http::{ReqResBuffer, server_framework::{State, VerbatimParams}};

// The response will contain the same headers and data received from the request. Basically an echo.
async fn echo(_: State<'_, (), (), ReqResBuffer>) -> wtx::Result<VerbatimParams> {
  Ok(VerbatimParams::default())
}
Example

//! An HTTP server framework showcasing nested routes, middlewares, manual streams, dynamic routes,
//! PostgreSQL connections and JSON deserialization/serialization.
//!
//! Currently, only HTTP/2 is supported.

extern crate serde;
extern crate tokio;
extern crate wtx;
extern crate wtx_instances;

use core::{fmt::Write, ops::ControlFlow};
use tokio::net::{TcpStream, tcp::OwnedWriteHalf};
use wtx::{
  database::{Executor, Record},
  http::{
    ManualStream, Method, ReqResBuffer, Request, Response, StatusCode,
    server_framework::{
      Middleware, PathOwned, Router, SerdeJsonOwned, ServerFrameworkBuilder, StateClean,
      VerbatimParams, get, json,
    },
  },
  http2::{Http2Buffer, Http2ErrorCode, ServerStream},
  pool::{PostgresRM, SimplePool},
  rng::{ChaCha20, SeedableRng},
};

type LocalPool = SimplePool<PostgresRM<wtx::Error, TcpStream>>;

#[tokio::main]
async fn main() -> wtx::Result<()> {
  let router = Router::paths(wtx::paths!(
    ("/db/{id}", get(db)),
    ("/json", json(Method::Post, deserialization_and_serialization)),
    (
      "/say",
      Router::new(wtx::paths!(("/hello", get(hello)), ("/world", get(world))), CustomMiddleware,)?,
    ),
    ("/stream", get(stream)),
  ))?;
  let pool = LocalPool::new(
    4,
    PostgresRM::tokio(ChaCha20::from_os()?, "postgres://USER:PASSWORD@localhost/DB_NAME".into()),
  );
  ServerFrameworkBuilder::new(ChaCha20::from_os()?, router)
    .with_stream_aux(move |_| Ok(pool.clone()))
    .tokio(
      &wtx_instances::host_from_args(),
      |error| eprintln!("{error:?}"),
      |_| Ok(()),
      |_| Ok(()),
      |error| eprintln!("{error:?}"),
    )
    .await
}

async fn deserialization_and_serialization(
  _: SerdeJsonOwned<DeserializeExample>,
) -> wtx::Result<SerdeJsonOwned<SerializeExample>> {
  Ok(SerdeJsonOwned(SerializeExample { _baz: [1, 2, 3, 4] }))
}

async fn db(
  state: StateClean<'_, (), LocalPool, ReqResBuffer>,
  PathOwned(id): PathOwned<u32>,
) -> wtx::Result<VerbatimParams> {
  let mut lock = state.stream_aux.get_with_unit().await?;
  let record = lock.execute_stmt_single("SELECT name FROM persons WHERE id = $1", (id,)).await?;
  let name = record.decode::<_, &str>(0)?;
  state.req.rrd.body.write_fmt(format_args!("Person of id `{id}` has name `{name}`"))?;
  Ok(VerbatimParams(StatusCode::Ok))
}

async fn hello() -> &'static str {
  "hello"
}

async fn stream(
  mut manual_stream: ManualStream<(), ServerStream<Http2Buffer, OwnedWriteHalf>, LocalPool>,
) -> wtx::Result<()> {
  manual_stream.stream.common().send_go_away(Http2ErrorCode::NoError).await;
  Ok(())
}

async fn world() -> &'static str {
  "world"
}

struct CustomMiddleware;

impl Middleware<(), wtx::Error, LocalPool> for CustomMiddleware {
  type Aux = ();

  fn aux(&self) -> Self::Aux {}

  async fn req(
    &self,
    _: &mut (),
    _: &mut Self::Aux,
    _: &mut Request<ReqResBuffer>,
    _: &mut LocalPool,
  ) -> wtx::Result<ControlFlow<StatusCode, ()>> {
    println!("Inspecting request");
    Ok(ControlFlow::Continue(()))
  }

  async fn res(
    &self,
    _: &mut (),
    _: &mut Self::Aux,
    _: Response<&mut ReqResBuffer>,
    _: &mut LocalPool,
  ) -> wtx::Result<ControlFlow<StatusCode, ()>> {
    println!("Inspecting response");
    Ok(ControlFlow::Continue(()))
  }
}

#[derive(serde::Deserialize)]
struct DeserializeExample {
  _foo: i32,
  _bar: u64,
}

#[derive(serde::Serialize)]
struct SerializeExample {
  _baz: [u8; 4],
}




HTTP/2
Implementation of RFC7541 and RFC9113. HTTP/2 is the second major version of the Hypertext Transfer Protocol, introduced in 2015 to improve web performance, it addresses limitations of HTTP/1.1 while maintaining backwards compatibility.

Passes the hpack-test-case and the h2spec test suites. Due to official and unofficial deprecations, prioritization and server-push are not supported.

There are a bunch of low-level details that most individuals don’t care about when they are building applications. If that is your case, high level interfaces are available in http-client-pool or http-server-framework.

To use this functionality, it is necessary to activate the http2 feature.

HTTP/1.1 Upgrade
Does not support upgrading from HTTP/1.1 because browsers also don’t support such a feature. Connections must be established directly using HTTP/2 or via ALPN (Application-Layer Protocol Negotiation) during the TLS handshake.

Operating Modes
There are two distinct operating modes for handling data transmission.

Automatic Mode
The system takes full responsibility. When you provide a buffer of data to be sent, the implementation automatically fragments it into appropriate DATA frames based on the maximum frame size and the current flow control window.

Manual Mode
Allows more control but you should know HTTP/2 concepts and their interactions. In this mode the user is responsible for constructing and sending individual HEADERS, DATA and TRAILERS frames.

Client Example
//! Fetches an URI using low-level HTTP/2 resources.

extern crate tokio;
extern crate wtx;
extern crate wtx_instances;

use tokio::net::TcpStream;
use wtx::{
  http::{HttpClient, ReqBuilder, ReqResBuffer},
  http2::{Http2, Http2Buffer, Http2ErrorCode, Http2Params},
  misc::{Uri, from_utf8_basic},
  rng::{Xorshift64, simple_seed},
};

#[tokio::main]
async fn main() -> wtx::Result<()> {
  let uri = Uri::new("SOME_URI");
  let (frame_reader, http2) = Http2::connect(
    Http2Buffer::new(&mut Xorshift64::from(simple_seed())),
    Http2Params::default(),
    TcpStream::connect(uri.hostname_with_implied_port()).await?.into_split(),
  )
  .await?;
  let _jh = tokio::spawn(frame_reader);
  let res = http2.send_req_recv_res(ReqResBuffer::empty(), ReqBuilder::get(uri.to_ref())).await?;
  println!("{}", from_utf8_basic(&res.rrd.body)?);
  http2.send_go_away(Http2ErrorCode::NoError).await;
  Ok(())
}
Server Example

//! Low-level HTTP/2 server that uses optioned parameters.
//!
//! Automatic streams are handled by the system while manual stream are handled by the user. In
//! this particular example all manual streams are considered to be WebSocket connections over
//! HTTP/2.
//!
//! Please note that it is much easier to just use the HTTP server framework.

extern crate tokio;
extern crate tokio_rustls;
extern crate wtx;
extern crate wtx_instances;

use tokio::{io::WriteHalf, net::TcpStream};
use tokio_rustls::server::TlsStream;
use wtx::{
  collection::Vector,
  http::{
    AutoStream, ManualServerStream, OperationMode, OptionedServer, ReqResBuffer, Response,
    StatusCode, is_web_socket_handshake,
  },
  http2::{Http2Buffer, Http2Params, WebSocketOverStream},
  misc::TokioRustlsAcceptor,
  rng::{Xorshift64, simple_seed},
  web_socket::{Frame, OpCode},
};

#[tokio::main]
async fn main() -> wtx::Result<()> {
  OptionedServer::http2_tokio(
    (
      TokioRustlsAcceptor::without_client_auth()
        .http2()
        .build_with_cert_chain_and_priv_key(wtx_instances::CERT, wtx_instances::KEY)?,
      &wtx_instances::host_from_args(),
      (),
      (),
    ),
    |_| Ok(()),
    |acceptor, stream| async move { Ok(tokio::io::split(acceptor.accept(stream).await?)) },
    |error| eprintln!("{error}"),
    |_| {
      Ok((
        (),
        Http2Buffer::new(&mut Xorshift64::from(simple_seed())),
        Http2Params::default()
          .set_enable_connect_protocol(true)
          .set_max_hpack_len((128 * 1024, 128 * 1024)),
      ))
    },
    |_| Ok(Vector::new()),
    |_, _, protocol, req, _| {
      Ok((
        (),
        if is_web_socket_handshake(&req.rrd.headers, req.method, protocol) {
          OperationMode::Manual
        } else {
          OperationMode::Auto
        },
      ))
    },
    |error| eprintln!("{error}"),
    auto,
    manual,
  )
  .await
}

async fn auto(
  _: (),
  mut ha: AutoStream<(), Vector<u8>>,
) -> Result<Response<ReqResBuffer>, wtx::Error> {
  ha.req.clear();
  Ok(ha.req.into_response(StatusCode::Ok))
}

async fn manual(
  _: (),
  mut hm: ManualServerStream<(), Http2Buffer, Vector<u8>, WriteHalf<TlsStream<TcpStream>>>,
) -> Result<(), wtx::Error> {
  let rng = Xorshift64::from(simple_seed());
  hm.req.rrd.headers.clear();
  let mut wos = WebSocketOverStream::new(&hm.req.rrd.headers, false, rng, hm.stream).await?;
  loop {
    let mut frame = wos.read_frame(&mut hm.stream_aux).await?;
    match (frame.op_code(), frame.text_payload()) {
      (_, Some(elem)) => println!("{elem}"),
      (OpCode::Close, _) => break,
      _ => {}
    }
    wos.write_frame(&mut Frame::new_fin(OpCode::Text, frame.payload_mut())).await?;
  }
  wos.close().await?;
  Ok(())





Internal Development
Intended for the development of WTX although some tips might be useful for your projects.

Size constraints
A large enum aggressively used in several places can cause a negative runtime impact. In fact, this is so common that the community created several lints to prevent such a scenario.

large_enum_variant
result_large_err
variant_size_differences
Some real-world use-cases and associated benchmarks.

https://ziglang.org/download/0.8.0/release-notes.html#Reworked-Memory-Layout
https://github.com/rust-lang/rust/pull/100441
https://github.com/rust-lang/rust/pull/95715
That is why WTX has an enforced Error enum size of 16 bytes and that is also the reason why WTX has so many bare variants.

Profiling
Uses the h2load benchmarking tool (https://nghttp2.org/documentation/h2load-howto.html) and the h2load internal binary (https://github.com/c410-f3r/wtx/blob/main/wtx-instances/src/bin/h2load.rs) for illustration purposes.

Compilation time / Size
cargo-bloat: Finds out what takes most of the space in executables.

cargo bloat --bin h2load --features h2load | head -20
cargo-llvm-lines: Measures the number and size of instantiations of each generic function in a program.

CARGO_PROFILE_RELEASE_LTO=fat cargo llvm-lines --bin h2load --features h2load --package wtx-instances --release | head -20
Performance
Prepare the executables in different terminals.

h2load -c100 --log-file=/tmp/h2load.txt -m10 -n10000 --no-tls-proto=h2c http://localhost:9000
cargo build --bin h2load --features h2load --profile profiling --target x86_64-unknown-linux-gnu
samply: Command line CPU profiler.

cargo build --bin h2load --features h2load --profile profiling --target x86_64-unknown-linux-gnu
samply record ./target/x86_64-unknown-linux-gnu/profiling/h2load
callgrind: Gives global, per-function, and per-source-line instruction counts and simulated cache and branch prediction data.

valgrind --tool=callgrind --dump-instr=yes --collect-jumps=yes --simulate-cache=yes ./target/x86_64-unknown-linux-gnu/profiling/h2load
Compiler flags
Some non-standard options that will influence the final binary. Only use them if you know what you are doing.

Size
-Cforce-frame-pointers=no
-Cforce-unwind-tables=no
More size-related parameters can be found at https://github.com/johnthagen/min-sized-rust.

Runtime
-Cllvm-args=–inline-threshold=1000
-Cllvm-args=-vectorize-loops
-Cllvm-args=-vectorize-slp
-Ctarget-cpu=x86-64-v3
Security
-Ccontrol-flow-guard=yes
-Crelocation-model=pie
-Crelro-level=full
-Zstack-protector=strong






Secrets
The Secret struct is a container for sensitive data that needs to be sustained in memory for an extended period. Holds locked and encrypted heap-allocated bytes that are decrypted on demand to protect against inspection techniques.

Please keep in mind that this is not a silver bullet, but rather an additional layer of protection. For example, when the peek closure is executing, the plaintext secret will exist transiently in CPU registers and caches, which is unavoidable.

Example

//! Long lived secret

extern crate wtx;

use crate::wtx::rng::SeedableRng;
use std::{env, sync::OnceLock};
use wtx::{
  collection::Vector,
  misc::{Secret, SensitiveBytes},
  rng::ChaCha20,
};

static SECRET: OnceLock<Secret> = OnceLock::new();

fn main() -> wtx::Result<()> {
  let data = env::args().nth(1).ok_or(wtx::Error::Generic(Box::new("No data".into())))?;
  let mut rng = ChaCha20::from_os()?;
  let secret = Secret::new(SensitiveBytes::new_locked(data.into_bytes().as_mut())?, &mut rng)?;
  let _rslt = SECRET.set(secret);
  std::thread::spawn(|| {
    let mut buffer = Vector::new();
    SECRET.wait().peek(&mut buffer, |_data| {
      // Sign documents, pass API keys, etc...
    })?;
    wtx::Result::Ok(())
  })
  .join()??;
  Ok(())
}






UI Tools
wtx-ui is a standalone crate intended to allow interactions with the wtx project through an user interface. At the current time only CLI interfaces are available.

Embeds SQL migrations for schema-manager. Activation feature is called embed-migrations.
Runs SQL migrations managed by schema-manager. Activation feature is called schema-manager or schema-manager-dev.
Performs very basic WebSocket Client/Server operations. Activation feature is called web-socket.
Makes requests to arbitrary URIs mimicking the interface of cURL. Activation feature is called http-client.






WebSocket
Implementation of RFC6455 and RFC7692. WebSocket is a communication protocol that enables full-duplex communication between a client (typically a web browser) and a server over a single TCP connection. Unlike traditional HTTP, which is request-response based, WebSocket allows real-time data exchange without the need for polling.

In-house benchmarks are available at https://c410-f3r.github.io/wtx-bench. If you are aware of other benchmark tools, please open a discussion in the GitHub project.

To use this functionality, it is necessary to activate the web-socket feature.

WebSocket Benchmark

Autobahn Reports
fuzzingclient
fuzzingserver
Compression
The “permessage-deflate” extension is the only supported compression format and is backed by the zlib-rs project that performs as well as zlib-ng.

At the current time WTX is the only crate that allows lock-free reader and writer parts with compression support.

To get the most performance possible, try compiling your program with RUSTFLAGS='-C target-cpu=native' to allow zlib-rs to use more efficient SIMD instructions.

No masking
Although not officially endorsed, the no-masking parameter described at https://datatracker.ietf.org/doc/html/draft-damjanovic-websockets-nomasking-02 is supported to increase performance. If such a thing is not desirable, please make sure to check the handshake parameters to avoid accidental scenarios.

To make everything work as intended both parties, client and server, need to implement this feature. For example, web browsers won’t stop masking frames.

Ping and Close frames
A received Ping frame automatically triggers an internal Pong response. Similarly, when a Close frame is received an automatic Close frame response is also sent.

//! WebSocket CLI client that enables real-time communication by allowing users to send and
//! receive messages through typing.

extern crate tokio;
extern crate wtx;
extern crate wtx_instances;

use tokio::net::TcpStream;
use wtx::{
  collection::Vector,
  misc::Uri,
  web_socket::{OpCode, WebSocketConnector, WebSocketPayloadOrigin},
};

#[tokio::main]
async fn main() -> wtx::Result<()> {
  let uri = Uri::new("SOME_URI");
  let mut ws = WebSocketConnector::default()
    .headers([("custom-key", "CUSTOM_VALUE")]) // Headers are optional. This method can be omitted.
    .connect(TcpStream::connect(uri.hostname_with_implied_port()).await?, &uri.to_ref())
    .await?;
  let mut buffer = Vector::new();
  loop {
    let frame = ws.read_frame(&mut buffer, WebSocketPayloadOrigin::Adaptive).await?;
    match (frame.op_code(), frame.text_payload()) {
      // `read_frame` internally already sent a Close response
      (OpCode::Close, _) => {
        break;
      }
      // `read_frame` internally already sent a Pong response
      (OpCode::Ping, _) => {}
      // For any other type, `read_frame` doesn't automatically send frames
      (_, text) => {
        if let Some(elem) = text {
          println!("Received text frame: {elem}")
        }
      }
    }
  }
  Ok(())
}
The same automatic behavior does not happen with concurrent instances because there are multiple ways to synchronize resources. In other words, you are responsible for managing replies.

//! Encrypted WebSocket client that reads and writes frames in different tasks.
//!
//! Replies aren't automatically handled by the system in concurrent scenarios because there are
//! multiple ways to synchronize resources. In this example, reply frames are managed in the same
//! task but you can also utilize any other method.

extern crate tokio;
extern crate tokio_rustls;
extern crate wtx;
extern crate wtx_instances;

use tokio::net::TcpStream;
use wtx::{
  collection::Vector,
  misc::{TokioRustlsConnector, Uri},
  web_socket::{Frame, OpCode, WebSocketConnector, WebSocketPartsOwned, WebSocketPayloadOrigin},
};

#[tokio::main]
async fn main() -> wtx::Result<()> {
  let uri = Uri::new("SOME_TLS_URI");
  let tls_connector = TokioRustlsConnector::from_auto()?.push_certs(wtx_instances::ROOT_CA)?;
  let stream = TcpStream::connect(uri.hostname_with_implied_port()).await?;
  let ws = WebSocketConnector::default()
    .connect(
      tls_connector.connect_without_client_auth(uri.hostname(), stream).await?,
      &uri.to_ref(),
    )
    .await?;
  let WebSocketPartsOwned { mut reader, replier, mut writer } = ws.into_parts(tokio::io::split)?;

  let reader_fut = async {
    let mut buffer = Vector::new();
    loop {
      let frame = reader.read_frame(&mut buffer, WebSocketPayloadOrigin::Adaptive).await?;
      match (frame.op_code(), frame.text_payload()) {
        // A special version of this frame has already been sent to the replier
        (OpCode::Close, _) => break,
        // A `Pong` frame with the same content has already been sent to the replier
        (OpCode::Ping, _) => {}
        (_, text) => {
          if let Some(elem) = text {
            println!("Received text frame: {elem}")
          }
        }
      }
    }
    wtx::Result::Ok(())
  };

  let writer_fut = async {
    writer.write_frame(&mut Frame::new_fin(OpCode::Close, *b"Bye")).await?;
    loop {
      let mut control_frame = replier.reply_frame().await;
      if writer.write_reply_frame(&mut control_frame).await? {
        break;
      }
    }
    wtx::Result::Ok(())
  };

  let (reader_rslt, writer_rslt) = tokio::join!(reader_fut, writer_fut);
  reader_rslt?;
  writer_rslt?;
  Ok(())
}
Alternative replying methods can be found at web-socket-examples in the wtx-instances crate.

Server Example

//! Serves requests using low-level WebSockets resources along side self-made certificates.

extern crate tokio;
extern crate tokio_rustls;
extern crate wtx;
extern crate wtx_instances;

use tokio::net::TcpStream;
use tokio_rustls::server::TlsStream;
use wtx::{
  collection::Vector,
  http::OptionedServer,
  misc::TokioRustlsAcceptor,
  rng::Xorshift64,
  web_socket::{OpCode, WebSocket, WebSocketBuffer, WebSocketPayloadOrigin},
};

#[tokio::main]
async fn main() -> wtx::Result<()> {
  OptionedServer::web_socket_tokio(
    &wtx_instances::host_from_args(),
    None,
    || {},
    |error| eprintln!("{error}"),
    handle,
    (
      || {
        TokioRustlsAcceptor::without_client_auth()
          .build_with_cert_chain_and_priv_key(wtx_instances::CERT, wtx_instances::KEY)
      },
      |acceptor, stream| async move { Ok(acceptor.accept(stream).await?) },
    ),
  )
  .await
}

async fn handle(
  mut ws: WebSocket<(), Xorshift64, TlsStream<TcpStream>, &mut WebSocketBuffer, false>,
) -> wtx::Result<()> {
  let (mut common, mut reader, mut writer) = ws.parts_mut();
  let mut buffer = Vector::new();
  loop {
    let mut frame =
      reader.read_frame(&mut buffer, &mut common, WebSocketPayloadOrigin::Adaptive).await?;
    match frame.op_code() {
      OpCode::Binary | OpCode::Text => {
        writer.write_frame(&mut common, &mut frame).await?;
      }
      OpCode::Close => break,
      _ => {}
    }
  }
  Ok(())
}











WebSocket over HTTP/2
At the current time only servers support the handshake procedure defined in RFC8441.

While HTTP/2 inherently supports full-duplex communication, web browsers typically don’t expose this functionality directly to developers and that is why WebSocket tunneling over HTTP/2 is important.

Servers can efficiently handle multiple concurrent streams within a single TCP connection
Client applications can continue using existing WebSocket APIs without modification
For this particular scenario the no-masking parameter defined in https://datatracker.ietf.org/doc/html/draft-damjanovic-websockets-nomasking-02 is also supported.

To use this functionality, it is necessary to activate the http2 and web-socket features.

Example

//! Low-level HTTP/2 server that uses optioned parameters.
//!
//! Automatic streams are handled by the system while manual stream are handled by the user. In
//! this particular example all manual streams are considered to be WebSocket connections over
//! HTTP/2.
//!
//! Please note that it is much easier to just use the HTTP server framework.

extern crate tokio;
extern crate tokio_rustls;
extern crate wtx;
extern crate wtx_instances;

use tokio::{io::WriteHalf, net::TcpStream};
use tokio_rustls::server::TlsStream;
use wtx::{
  collection::Vector,
  http::{
    AutoStream, ManualServerStream, OperationMode, OptionedServer, ReqResBuffer, Response,
    StatusCode, is_web_socket_handshake,
  },
  http2::{Http2Buffer, Http2Params, WebSocketOverStream},
  misc::TokioRustlsAcceptor,
  rng::{Xorshift64, simple_seed},
  web_socket::{Frame, OpCode},
};

#[tokio::main]
async fn main() -> wtx::Result<()> {
  OptionedServer::http2_tokio(
    (
      TokioRustlsAcceptor::without_client_auth()
        .http2()
        .build_with_cert_chain_and_priv_key(wtx_instances::CERT, wtx_instances::KEY)?,
      &wtx_instances::host_from_args(),
      (),
      (),
    ),
    |_| Ok(()),
    |acceptor, stream| async move { Ok(tokio::io::split(acceptor.accept(stream).await?)) },
    |error| eprintln!("{error}"),
    |_| {
      Ok((
        (),
        Http2Buffer::new(&mut Xorshift64::from(simple_seed())),
        Http2Params::default()
          .set_enable_connect_protocol(true)
          .set_max_hpack_len((128 * 1024, 128 * 1024)),
      ))
    },
    |_| Ok(Vector::new()),
    |_, _, protocol, req, _| {
      Ok((
        (),
        if is_web_socket_handshake(&req.rrd.headers, req.method, protocol) {
          OperationMode::Manual
        } else {
          OperationMode::Auto
        },
      ))
    },
    |error| eprintln!("{error}"),
    auto,
    manual,
  )
  .await
}

async fn auto(
  _: (),
  mut ha: AutoStream<(), Vector<u8>>,
) -> Result<Response<ReqResBuffer>, wtx::Error> {
  ha.req.clear();
  Ok(ha.req.into_response(StatusCode::Ok))
}

async fn manual(
  _: (),
  mut hm: ManualServerStream<(), Http2Buffer, Vector<u8>, WriteHalf<TlsStream<TcpStream>>>,
) -> Result<(), wtx::Error> {
  let rng = Xorshift64::from(simple_seed());
  hm.req.rrd.headers.clear();
  let mut wos = WebSocketOverStream::new(&hm.req.rrd.headers, false, rng, hm.stream).await?;
  loop {
    let mut frame = wos.read_frame(&mut hm.stream_aux).await?;
    match (frame.op_code(), frame.text_payload()) {
      (_, Some(elem)) => println!("{elem}"),
      (OpCode::Close, _) => break,
      _ => {}
    }
    wos.write_frame(&mut Frame::new_fin(OpCode::Text, frame.payload_mut())).await?;
  }
  wos.close().await?;
  Ok(())
}











