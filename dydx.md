# File: v4-documentation/README.md

## Development

This is a [Vocs](https://vocs.dev) project bootstrapped with the Vocs CLI.

```
pnpm install
pnpm dev
```


## Deploy Vocs on Vercel (Quick Guide)

You can easily deploy Vocs using [Vercel](https://vercel.com). Follow these simple steps:

* Go to your Vercel dashboard and click **Add New** > **Project**.
* Select **Import Git Repository** and choose your forked Vocs repository.
* In the **New Project** setup:

  * Set **Framework Preset** to `Other`.
  * Set the **Root Directory** to `.` (root directory).
* Click **Deploy**.

After deployment is complete, your Vocs instance will be live on your Vercel domain. 🎉


## Documentation Guidelines

1. **Adding Sections to the Table of Contents (TOC)**

    To add new sections to the Table of Contents, update the configuration file `vocs.config.ts`. Make sure to modify the appropriate section of the config so that your new pages or sections appear correctly in the TOC.

2. **Pages Location**

    All documentation pages are located in the `docs/pages` directory. Each page should be added there, following the structure defined in the TOC configuration.

3. **Types Location**

    All types are stored in a separate folder: `docs/pages/types`. The types are used in tables of parameters for methods.

4. **Using the Template**

    A predefined template is available and should be used as the basis for creating all new pages. This ensures consistency in structure and style throughout the documentation.

    `docs/pages/templates/method.mdx`



# File: v4-documentation/docs/pages/concepts/trading/isolated-positions.md

# Isolated Positions

**Isolated positions** on the **dYdX frontend** are perpetual positions held in subaccounts with a subaccount number greater than 127, up to the limit of 128,000. Each isolated position is held in a separate subaccount.

:::tip
**Isolated positions** are a feature provided and managed by the **dYdX frontend** (web) interface. This page provides information on how to integrate this feature into your API-based implementation.
:::

## Mapping of isolated positions to subaccounts

The dYdX frontend implementation separates subaccounts (0 - 128,000) into 2 separate types.

### Parent subaccounts

Subaccounts 0 to 127 are parent subaccounts. Parent subaccounts can have multiple positions opened and all positions are cross-margined.

### Child subaccounts

Subaccounts 128 to 128,000 are child subaccounts. Child subaccounts will only ever have up to 1 position open. Each open isolated position on the frontend is held by a separate child subaccount.
Once an isolated position is closed in the frontend, the subaccount associated with isolated position can be re-used for the next isolated position.

Child subaccounts are mapped to parent subaccounts using the formula:
e.g. parent subaccount 0 has child subaccounts 128, 256,...
parent subaccount 1 has child subaccounts 129, 257,...

```
parent_subaccount_number = child_subaccount_number % 128
```

:::note
Note that currently only parent subaccount 0 is exposed via the frontend and so isolated positions will be held in subaccounts number 128, 256, ...
:::

:::note
Note that the above "types" of subaccounts are not enforced at a protocol level, and only on the frontend. Any subaccount can hold any number of positions in cross-marginable markets which all will cross-margined at the protocol level.
:::

:::note
When you are using the dYdX frontend, any margin transferred to an empty child subaccount that isn’t used for placing a trade will get sent back to the cross subaccount after some time.
:::

## Getting data for parent subaccount

API endpoints exist to get data for a parent subaccount and all it's child subaccounts on the Indexer.

> Currently all data for an account viewable on the frontend can be fetched by using the parent subaccount APIs to fetch data for parent subaccount number 0.

See the [Indexer API](/indexer-client/http#get-parent-subaccount) page for more details of the parent subaccount APIs.


# File: v4-documentation/old-docs/README.md

<p align="center"><img src="https://dydx.exchange/icon.svg?" width="256" /></p>

<h1 align="center">dYdX Chain Documentation</h1>

<div align="center">
  <a href='https://github.com/dydxprotocol/v4-documentation/blob/024e1b35537ba619b79576d07464a8cb4eb2de66/LICENSE'>
    <img src='https://img.shields.io/badge/License-AGPL_v3-blue.svg' alt='License' />
  </a>
</div>

## Local Development

Install `pnpm` and project dependencies:

```bash
nvm install 22 && nvm use 22
npm install -g pnpm
pnpm i
```

Start development server on localhost:3000:

```bash
pnpm dev
```

## Formatting

To format .mdx files, you can use the [Prettier](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode) extension in VSCode.

## Github Actions

Upon push of a commit, the following checks are made:

- [markdown-link-check](https://github.com/gaurav-nelson/github-action-markdown-link-check) checks that all links work.
  - If you are configuring a link that is erroring out, considering adding something to the [mlc_config.json](./mlc_config.json) using [these options](https://github.com/tcort/markdown-link-check#config-file-format).


# File: v4-documentation/old-docs/slate-docs/CHANGELOG.md

# Changelog

## Version 2.7.0

*June 21, 2020*

* __[security]__ Bumped rack in Gemfile.lock from 2.2.2 to 2.2.3
* Bumped bundled jQuery from 3.2.1 to 3.5.1
* Bumped bundled lunr from 0.5.7 to 2.3.8
* Bumped imagesloaded from 3.1.8 to 4.1.4
* Bumped rouge from 3.17.0 to 3.20.0
* Bumped redcarpet from 3.4.0 to 3.5.0
* Fix color of highlighted code being unreadable when printing page
* Add clipboard icon for "Copy to Clipboard" functionality to code boxes (see note below)
* Fix handling of ToC selectors that contain punctutation (thanks @gruis)
* Fix language bar truncating languages that overflow screen width
* Strip HTML tags from ToC title before displaying it in title bar in JS (backup to stripping done in Ruby code) (thanks @atic)

To enable the new clipboard icon, you need to add `code_clipboard: true` to the frontmatter of source/index.html.md.
See [this line](https://github.com/slatedocs/slate/blame/main/source/index.html.md#L19) for an example of usage.

## Version 2.6.1

*May 30, 2020*

* __[security]__ update child dependency activesupport in Gemfile.lock to 5.4.2.3
* Update Middleman in Gemfile.lock to 4.3.7
* Replace Travis-CI with GitHub actions for continuous integration
* Replace Spectrum with GitHub discussions

## Version 2.6.0

*May 18, 2020*

__Note__: 2.5.0 was "pulled" due to a breaking bug discovered after release. It is recommended to skip it, and move straight to 2.6.0.

* Fix large whitespace gap in middle column for sections with codeblocks
* Fix highlighted code elements having a different background than rest of code block
* Change JSON keys to have a different font color than their values
* Disable asset hashing for woff and woff2 elements due to middleman bug breaking woff2 asset hashing in general
* Move Dockerfile to Debian from Alpine
* Converted repo to a [GitHub template](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/creating-a-template-repository)
* Update sassc to 2.3.0 in Gemfile.lock

## Version 2.5.0

*May 8, 2020*

* __[security]__ update nokogiri to ~> 1.10.8
* Update links in example docs to https://github.com/slatedocs/slate from https://github.com/lord/slate
* Update LICENSE to include full Apache 2.0 text
* Test slate against Ruby 2.5 and 2.6 on Travis-CI
* Update Vagrantfile to use Ubuntu 18.04 (thanks @bradthurber)
* Parse arguments and flags for deploy.sh on script start, instead of potentially after building source files
* Install nodejs inside Vagrantfile (thanks @fernandoaguilar)
* Add Dockerfile for running slate (thanks @redhatxl)
* update middleman-syntax and rouge to ~>3.2
* update middleman to 4.3.6

## Version 2.4.0

*October 19, 2019*

- Move repository from lord/slate to slatedocs/slate
- Fix documentation to point at new repo link, thanks to [Arun](https://github.com/slash-arun), [Gustavo Gawryszewski](https://github.com/gawry), and [Daniel Korbit](https://github.com/danielkorbit)
- Update `nokogiri` to 1.10.4
- Update `ffi` in `Gemfile.lock` to fix security warnings, thanks to [Grey Baker](https://github.com/greysteil) and [jakemack](https://github.com/jakemack)
- Update `rack` to 2.0.7 in `Gemfile.lock` to fix security warnings, thanks to [Grey Baker](https://github.com/greysteil) and [jakemack](https://github.com/jakemack)
- Update middleman to `4.3` and relax constraints on middleman related gems, thanks to [jakemack](https://github.com/jakemack)
- Add sass gem, thanks to [jakemack](https://github.com/jakemack)
- Activate `asset_cache` in middleman to improve cacheability of static files, thanks to [Sam Gilman](https://github.com/thenengah)
- Update to using bundler 2 for `Gemfile.lock`, thanks to [jakemack](https://github.com/jakemack)

## Version 2.3.1

*July 5, 2018*

- Update `sprockets` in `Gemfile.lock` to fix security warnings

## Version 2.3

*July 5, 2018*

- Allows strikethrough in markdown by default.
- Upgrades jQuery to 3.2.1, thanks to [Tomi Takussaari](https://github.com/TomiTakussaari)
- Fixes invalid HTML in `layout.erb`, thanks to [Eric Scouten](https://github.com/scouten) for pointing out
- Hopefully fixes Vagrant memory issues, thanks to [Petter Blomberg](https://github.com/p-blomberg) for the suggestion
- Cleans HTML in headers before setting `document.title`, thanks to [Dan Levy](https://github.com/justsml)
- Allows trailing whitespace in markdown files, thanks to [Samuel Cousin](https://github.com/kuzyn)
- Fixes pushState/replaceState problems with scrolling not changing the document hash, thanks to [Andrey Fedorov](https://github.com/anfedorov)
- Removes some outdated examples, thanks [@al-tr](https://github.com/al-tr), [Jerome Dahdah](https://github.com/jdahdah), and [Ricardo Castro](https://github.com/mccricardo)
- Fixes `nav-padding` bug, thanks [Jerome Dahdah](https://github.com/jdahdah)
- Code style fixes thanks to [Sebastian Zaremba](https://github.com/vassyz)
- Nokogiri version bump thanks to [Grey Baker](https://github.com/greysteil)
- Fix to default `index.md` text thanks to [Nick Busey](https://github.com/NickBusey)

Thanks to everyone who contributed to this release!

## Version 2.2

*January 19, 2018*

- Fixes bugs with some non-roman languages not generating unique headers
- Adds editorconfig, thanks to [Jay Thomas](https://github.com/jaythomas)
- Adds optional `NestingUniqueHeadCounter`, thanks to [Vladimir Morozov](https://github.com/greenhost87)
- Small fixes to typos and language, thx [Emir Ribić](https://github.com/ribice), [Gregor Martynus](https://github.com/gr2m), and [Martius](https://github.com/martiuslim)!
- Adds links to Spectrum chat for questions in README and ISSUE_TEMPLATE

## Version 2.1

*October 30, 2017*

- Right-to-left text stylesheet option, thanks to [Mohammad Hossein Rabiee](https://github.com/mhrabiee)
- Fix for HTML5 history state bug, thanks to [Zach Toolson](https://github.com/ztoolson)
- Small styling changes, typo fixes, small bug fixes from [Marian Friedmann](https://github.com/rnarian), [Ben Wilhelm](https://github.com/benwilhelm), [Fouad Matin](https://github.com/fouad), [Nicolas Bonduel](https://github.com/NicolasBonduel), [Christian Oliff](https://github.com/coliff)

Thanks to everyone who submitted PRs for this version!

## Version 2.0

*July 17, 2017*

- All-new statically generated table of contents
  - Should be much faster loading and scrolling for large pages
  - Smaller Javascript file sizes
  - Avoids the problem with the last link in the ToC not ever highlighting if the section was shorter than the page
  - Fixes control-click not opening in a new page
  - Automatically updates the HTML title as you scroll
- Updated design
  - New default colors!
  - New spacings and sizes!
  - System-default typefaces, just like GitHub
- Added search input delay on large corpuses to reduce lag
- We even bumped the major version cause hey, why not?
- Various small bug fixes

Thanks to everyone who helped debug or wrote code for this version! It was a serious community effort, and I couldn't have done it alone.

## Version 1.5

*February 23, 2017*

- Add [multiple tabs per programming language](https://github.com/lord/slate/wiki/Multiple-language-tabs-per-programming-language) feature
- Upgrade Middleman to add Ruby 1.4.0 compatibility
- Switch default code highlighting color scheme to better highlight JSON
- Various small typo and bug fixes

## Version 1.4

*November 24, 2016*

- Upgrade Middleman and Rouge gems, should hopefully solve a number of bugs
- Update some links in README
- Fix broken Vagrant startup script
- Fix some problems with deploy.sh help message
- Fix bug with language tabs not hiding properly if no error
- Add `!default` to SASS variables
- Fix bug with logo margin
- Bump tested Ruby versions in .travis.yml

## Version 1.3.3

*June 11, 2016*

Documentation and example changes.

## Version 1.3.2

*February 3, 2016*

A small bugfix for slightly incorrect background colors on code samples in some cases.

## Version 1.3.1

*January 31, 2016*

A small bugfix for incorrect whitespace in code blocks.

## Version 1.3

*January 27, 2016*

We've upgraded Middleman and a number of other dependencies, which should fix quite a few bugs.

Instead of `rake build` and `rake deploy`, you should now run `bundle exec middleman build --clean` to build your server, and `./deploy.sh` to deploy it to Github Pages.

## Version 1.2

*June 20, 2015*

**Fixes:**

- Remove crash on invalid languages
- Update Tocify to scroll to the highlighted header in the Table of Contents
- Fix variable leak and update search algorithms
- Update Python examples to be valid Python
- Update gems
- More misc. bugfixes of Javascript errors
- Add Dockerfile
- Remove unused gems
- Optimize images, fonts, and generated asset files
- Add chinese font support
- Remove RedCarpet header ID patch
- Update language tabs to not disturb existing query strings

## Version 1.1

*July 27, 2014*

**Fixes:**

- Finally, a fix for the redcarpet upgrade bug

## Version 1.0

*July 2, 2014*

[View Issues](https://github.com/tripit/slate/issues?milestone=1&state=closed)

**Features:**

- Responsive designs for phones and tablets
- Started tagging versions

**Fixes:**

- Fixed 'unrecognized expression' error
- Fixed #undefined hash bug
- Fixed bug where the current language tab would be unselected
- Fixed bug where tocify wouldn't highlight the current section while searching
- Fixed bug where ids of header tags would have special characters that caused problems
- Updated layout so that pages with disabled search wouldn't load search.js
- Cleaned up Javascript


# File: v4-documentation/old-docs/slate-docs/CODE_OF_CONDUCT.md

# Contributor Covenant Code of Conduct

## Our Pledge

In the interest of fostering an open and welcoming environment, we as contributors and maintainers pledge to making participation in our project and our community a harassment-free experience for everyone, regardless of age, body size, disability, ethnicity, gender identity and expression, level of experience, nationality, personal appearance, race, religion, or sexual identity and orientation.

## Our Standards

Examples of behavior that contributes to creating a positive environment include:

* Using welcoming and inclusive language
* Being respectful of differing viewpoints and experiences
* Gracefully accepting constructive criticism
* Focusing on what is best for the community
* Showing empathy towards other community members

Examples of unacceptable behavior by participants include:

* The use of sexualized language or imagery and unwelcome sexual attention or advances
* Trolling, insulting/derogatory comments, and personal or political attacks
* Public or private harassment
* Publishing others' private information, such as a physical or electronic address, without explicit permission
* Other conduct which could reasonably be considered inappropriate in a professional setting

## Our Responsibilities

Project maintainers are responsible for clarifying the standards of acceptable behavior and are expected to take appropriate and fair corrective action in response to any instances of unacceptable behavior.

Project maintainers have the right and responsibility to remove, edit, or reject comments, commits, code, wiki edits, issues, and other contributions that are not aligned to this Code of Conduct, or to ban temporarily or permanently any contributor for other behaviors that they deem inappropriate, threatening, offensive, or harmful.

## Scope

This Code of Conduct applies both within project spaces and in public spaces when an individual is representing the project or its community. Examples of representing a project or community include using an official project e-mail address, posting via an official social media account, or acting as an appointed representative at an online or offline event. Representation of a project may be further defined and clarified by project maintainers.

## Enforcement

Instances of abusive, harassing, or otherwise unacceptable behavior may be reported by contacting the project team at hello@lord.io. The project team will review and investigate all complaints, and will respond in a way that it deems appropriate to the circumstances. The project team is obligated to maintain confidentiality with regard to the reporter of an incident. Further details of specific enforcement policies may be posted separately.

Project maintainers who do not follow or enforce the Code of Conduct in good faith may face temporary or permanent repercussions as determined by other members of the project's leadership.

## Attribution

This Code of Conduct is adapted from the [Contributor Covenant][homepage], version 1.4, available at [http://contributor-covenant.org/version/1/4][version]

[homepage]: http://contributor-covenant.org
[version]: http://contributor-covenant.org/version/1/4/


# File: v4-documentation/old-docs/slate-docs/README.md

<p align="center"><img src="https://s3.amazonaws.com/dydx-assets/logo_large_white.png" width="256" /></p>

**Documentation Powered by Slate and Presented on [docs.dydx.exchange](https://dydxprotocol.github.io/teacher)**

Getting Started with Slate & Running Changes Locally
------------------------------

Quick start on MacOS:

```bash
# install ruby version manager
\curl -sSL https://get.rvm.io | bash -s stable --ruby
# version 2.6.6 required to run v3-teacher (set CFLAGS due to commmon error: https://github.com/rvm/rvm/issues/5039#issuecomment-774577714)
CFLAGS="-Wno-error=implicit-function-declaration" rvm install 2.6.6
gem install bundler
bundle install
# Will run on http://localhost:4567
bundle exec middleman server 
```

To get started with Slate, please check out the [Getting Started](https://github.com/slatedocs/slate/wiki#getting-started)
section in the Slate [wiki](https://github.com/slatedocs/slate/wiki).

Slate supports running Slate in three different ways:
* [Natively](https://github.com/slatedocs/slate/wiki/Using-Slate-Natively)
* [Using Vagrant](https://github.com/slatedocs/slate/wiki/Using-Slate-in-Vagrant)
* [Using Docker](https://github.com/slatedocs/slate/wiki/Using-Slate-in-Docker)

------------------------------

Quick start on docker-compose:

### Install

[Install docker](https://docs.docker.com/engine/installation/#supported-platforms)

[Install Docker Compose](https://docs.docker.com/compose/install/) or on mac `brew install docker-compose`

### Run

Start server on http://localhost:4567/

```
docker-compose up
```


# File: v4-documentation/old-docs/slate-docs/source/index.html.md

---
title: v3 dYdX Documentation

language_tabs: # must be one of https://git.io/vQNgJ
  - python: Python
  - typescript: TypeScript
  - json: HTTP

includes:
  - general-v3
  - perpetual-contracts-v3
  - clients-v3
  - private-v3
  - public-v3
  - websocket-v3
  - security-v3

search: true

code_clipboard: true
---


# File: v4-documentation/old-docs/slate-docs/source/includes/_clients-v3.md

# Clients

Python and TypeScript clients are available, allowing programmatic usage of dYdX.

## Python Client

### Installation

Install `dydx-v3-python` from [PyPI](https://pypi.org/project/dydx-v3-python) using `pip`:

<pre class="center-column">
pip install dydx-v3-python
</pre>

### Usage

See [dydxprotocol/dydx-v3-python](https://github.com/dydxprotocol/dydx-v3-python).

See the [examples](https://github.com/dydxprotocol/dydx-v3-python/tree/master/examples) folder for simple python examples.

## TypeScript Client

### Installation

Install `@dydxprotocol/v3-client` from [NPM](https://www.npmjs.com/package/@dydxprotocol/v3-client):

<pre class="center-column">
npm i -s @dydxprotocol/v3-client
</pre>

### Usage

See [dydxprotocol/v3-client](https://github.com/dydxprotocol/v3-client).

See the [examples](https://github.com/dydxprotocol/v3-client/tree/master/examples) folder for simple typescript examples.

## Client Initialization

> Initialize

```python
client = Client(
    host='https://api.dydx.exchange',
    web3=Web3('...'),
    stark_private_key='01234abcd...',
)
```

```typescript
const client: DydxClient = new Client(
    'host',
    {
        apiTimeout: 3000,
        starkPrivateKey: '01234abcd...',
    },
);
```

The client is organized into modules, based on the type of authentication needed for different requests. The configuration options passed into the client determine which modules are available. See [Authentication](#authentication) for more information.

<aside class="notice">
Multiple methods of authorization are available, so users never need to provide private keys directly to the client, if so desired. Ethereum signatures are needed only for onboarding and managing API keys, not trading, and may be provided via a web3 provider. STARK key signatures are required for trading, and the STARK key can be held either in the client or elsewhere.
</aside>

| Module     | Description                                                      |
|------------|------------------------------------------------------------------|
| public     | Public API endpoints. Does not require authentication.           |
| onboarding | Endpoint to create a new user, authenticated via Ethereum key.   |
| api_keys   | Endpoints for managing API keys, authenticated via Ethereum key. |
| private    | All other private endpoints, authenticated via API key.          |
| eth        | Calling and querying L1 Ethereum smart contracts.                |

The following configuration options are available:

| Parameter                | Description                                                                                                                                                                          |
|--------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| host                     | The HTTP API host.                                                                                                                                                                   |
| api_timeout              | Timeout for HTTP requests, in milliseconds.                                                                                                                                          |
| default_ethereum_address | (Optional) The default account for Ethereum key auth and sending Ethereum transactions.                                                                                              |
| eth_private_key          | (Optional) May be used for Ethereum key auth.                                                                                                                                        |
| eth_send_options         | (Optional) Options for Ethereum transactions, see [`sendTransaction`](https://web3py.readthedocs.io/en/stable/web3.eth.html?highlight=signTransaction#web3.eth.Eth.sendTransaction). |
| network_id               | (Optional) Chain ID for Ethereum key auth and smart contract addresses. Defaults to `web3.net.version` if available, or `1` (mainnet).                                               |
| stark_private_key        | (Optional) STARK private key, used to sign orders and withdrawals.                                                                                                                   |
| web3                     | (Optional) Web3 object used for Ethereum key auth and/or smart contract interactions.                                                                                                |
| web3_account             | (Optional) May be used for Ethereum key auth.                                                                                                                                        |
| web3_provider            | (Optional) Web3 provider object, same usage as `web3`.                                                                                                                               |
| api_key_credentials      | (Optional) Dictionary containing the key, secret and passphrase required for the private module to sign requests.                                                                    |
| crypto_c_exports_path    | (Optional) For python only, will use faster C++ code to run hashing, signing and verifying. It's expected to be compiled from the `crypto_c_exports` target from Starkware's [repository](https://github.com/starkware-libs/crypto-cpp/blob/master/src/starkware/crypto/ffi/CMakeLists.txt). See [section on this below for more information](#c-methods-for-faster-stark-signing).|


### C++ Methods for Faster STARK Signing

<aside class="notice">
This optimization is only available for the Python client currently.
</aside>

The C++ wrapper methods in the client expect an absolute path to a [Shared Object](https://www.cprogramming.com/tutorial/shared-libraries-linux-gcc.html). This has to be compiled from [Starkware's crypto C++ library](https://github.com/starkware-libs/crypto-cpp/blob/master/src/starkware/crypto/ffi/CMakeLists.txt).


# File: v4-documentation/old-docs/slate-docs/source/includes/_general-v3.md

# Terms of Service and Privacy Policy

By using any API provided by dYdX Trading Inc., you agree to its [Terms of Use](https://dydx.exchange/terms) and [Privacy Policy](https://dydx.exchange/privacy). If you do not agree to the foregoing, then do not use any such API.

# General

These docs describe the v3 API for the dYdX decentralized perpetual contracts exchange. The exchange runs on an L2 (layer-2) blockchain system, and operates independently of previous dYdX protocols and systems, including the v1 and v2 APIs.

Like the previous iteration of dYdX perpetuals, the exchange uses a centralized order book, but remains non-custodial, and settles trades and liquidations in a trustless manner.

<aside class="notice">
These docs describe the dYdX <a href="https://trade.dydx.exchange">layer-2 perpetuals exchange</a>.
</aside>

## Layer 2: ZK-Rollups

Trades are settled in an L2 (layer-2) system, which publishes ZK (zero-knowledge) proofs periodically to an Ethereum smart contract in order to prove that state transitions within L2 are valid. Funds must be deposited to the Ethereum smart contract before they can be used to trade on dYdX.

By settling trades on L2, the exchange is able to offer much higher trade throughput and lower minimum order sizes, compared with systems settling trades directly on Ethereum (i.e. L1). This is achieved while maintaining decentralization, and the exchange is fully non-custodial.

The L2 system was developed with, and is operated jointly with, Starkware. More information about the L2 design can be found in [Starkware's documentation](https://docs.starkware.co/starkex-docs/). (Note: Some of the details described there may be specific to Starkware's previous StarkEx system and may not apply to the dYdX system.)

## Data Centers

Our data centers are located in the AWS AP-NORTHEAST-1 region (Tokyo).

<aside class="warning">
It is strictly against our <a href="https://dydx.exchange/terms">Terms of Use</a> to use United States based IPs to trade on dYdX.
</aside>

## Number Formats

All amounts and prices in the clients and API are represented in “human readable,” natural units. For example, an amount of 1.25 ETH is represented as `1.25`, and a price of $31,000.50 per BTC is represented as `31000.5`.

## Base URLs

Base URLs for API endpoints are as follows:

* **Production (Mainnet)**: `https://api.dydx.exchange`
* **Staging (Goerli)**: `https://api.stage.dydx.exchange`

## Testnet

We have one testnet which is on `Goerli`. To use the testnet, use the above Staging URL for your endpoint. Also use a `networkId` of `5` (Goerli) instead of `1` (Mainnet).

The user interface for testnet can be found [here](https://trade.stage.dydx.exchange).

The `dYdX Goerli USDC` token address is `0xF7a2fa2c2025fFe64427dd40Dc190d47ecC8B36e`. Users can deposit via the Testnet website.

## Rate-Limits

All rate-limits are subject to change.

Please make use of the WebSockets API if you need real-time data.

### Rate Limit - API

Limits are enforced by IP Address for public endpoints, and by both IP Address and Account for private endpoints.

Each request consumes 1 point towards the rate limit. [`POST v3/orders`](#place-order-rate-limits) consumes variable points based on the order. Points refresh at the end of each time window. Please take note of the `RateLimit-Remaining` header to track points usage.

#### Response Headers

Field                                   | Description
----------------------------------------| -----------
`RateLimit-Remaining`                   | Points remaining in the time window.
`RateLimit-Reset`                       | Timestamp that the time window ends, in Epoch milliseconds.
`Retry-After`                           | Milliseconds until the next time window. Header included only when the limit has been reached.
`RateLimit-Limit`                       | The maximum amount of points allowed per time window.

Request                                 | Limit
----------------------------------------| -----------
`GET v3/*`                              | 175 requests per 10 seconds.
`PUT v3/emails/send-verification-email` | 2 requests for 10 minutes.
`DELETE v3/orders`                      | See `Cancel-Order Rate Limits`
`POST v3/orders`                        | See `Place-Order Rate-Limits`
`POST v3/testnet/tokens`                | 5 requests per 24 hours.
`GET v3/active-orders`                  | See `Active-Order Rate-Limits`
`DELETE v3/active-orders`               | See `Active-Order Rate-Limits`
`All other requests`                    | 10 requests per minute.

### Rate Limit - Websocket

Limits are enforced per `connectionId`.

<aside class="warning">
If your connection exceeds the request limit, we will terminate the connection, and you will need to reconnect to the websocket. Additionally, sending too many invalid messages will also result in your websocket being disconnected.
</aside>

Request                                 | Limit
----------------------------------------| -----------
`subscribe v3_accounts, v3_markets`     | 2 requests per 1 second.
`subscribe v3_orderbook, v3_trades`     | 2 requests for 1 second per market.
`ping`                                  | 5 requests per 1 second.

### Cancel-Order Rate Limits

Canceling orders is limited per asset-pair and is intended to be higher than the limit on placing orders.

`DELETE v3/orders` requests are limited to `3` requests per `10` seconds per asset-pair.

`DELETE v3/orders/:id` requests are limited to `250` requests per `10` seconds per asset-pair.

### Place-Order Rate-Limits

Order rate limits are limited to `maxPoints` spent (per asset-pair) in a fixed window of `windowSec` seconds.

We want to give priority to those who are making the largest orders and who are contributing the most liquidity to the exchange.
Therefore, placing larger orders is subject to higher limits (i.e. larger orders carry a lower point cost).
The point cost is based on the `orderNotional` which is equal to the `size * price` of the order.

Limit-order point consumption is equal to:

<pre class="center-column">
orderConsumption = clamp(
  ceil(targetNotional / orderNotional),
  minOrderConsumption,
  maxOrderConsumption
)
</pre>

The `minOrderConsumption` is different for each order type, and can be one of `minLimitConsumption`, `minMarketConsumption`, or `minTriggerableConsumption`. Limit orders that are Fill-or-Kill or Immediate-or-Cancel are considered to be market orders for the purposes of rate limiting.

The values of the above variables as of March 15th, 2022 are listed below, but the most up-to-date values can be found in the [v3/config endpoint](#get-global-configuration-variables).

Variable         | Value
---------------- | -------
`maxPoints`      | `1,750`
`windowSec`      | `10`
`targetNotional` | `40,000`
`minLimitConsumption` | `4`
`minMarketConsumption` | `20`
`minTriggerableConsumption` | `100`
`maxOrderConsumption` | `100`

### Active-Order Rate-Limits

Querying active orders is limited per endpoint and per asset and is intended to be higher than the respective DELETE and GET endpoints these new endpoints replace.

#### DELETE Active-Orders Rate Limits

`DELETE v3/active-orders/*`

- 425 points allotted per 10 seconds per market.
- 1 point consumed if order id included.
- 25 points consumed if order side included.
- 50 points consumed otherwise.

#### GET Active-Orders Rate Limits

`GET v3/active-orders/*`

- 175 points allotted per 10 seconds per market.
- 1 point consumed if order id included.
- 3 points consumed if order side included.
- 5 points consumed otherwise.

## Other Limits

Accounts may only have up to 20 open orders for a given market/side pair at any one time. (For example up to 20 open `BTC-USD` bids).


# File: v4-documentation/old-docs/slate-docs/source/includes/_perpetual-contracts-v3.md

# Perpetual Contracts

The dYdX Perpetual is a non-custodial, decentralized margin product that offers synthetic exposure to a variety of assets.

## Margin

Collateral is held as USDC, and the quote asset for all perpetual markets is USDC. Cross-margining is used by default, meaning an account can open multiple positions that share the same collateral. Isolated margin can be achieved by creating separate accounts (sub-accounts) under the same user.

Each market has three risk parameters, the `initialMarginFraction`, `maintenanceMarginFraction` and `incrementalInitialMarginFraction`, which determine the max leverage available within that market. These are used to calculate the value that must be held by an account in order to open or increase positions (in the case of initial margin) or avoid liquidation (in the case of maintenance margin).

### Risk Parameters and Related Fields

| Risk                               | Description                                                                                                                  |
|------------------------------------|------------------------------------------------------------------------------------------------------------------------------|
| `initialMarginFraction`            | The margin fraction needed to open a position.                                                                               |
| `maintenanceMarginFraction`        | The margin fraction required to prevent liquidation.                                                                         |
| `incrementalInitialMarginFraction` | The increase of `initialMarginFraction` for each `incrementalPositionSize` above the `baselinePositionSize` the position is. |
| baselinePositionSize               | The max position size (in base token) before increasing the initial-margin-fraction.                                         |
| incrementalPositionSize            | The step size (in base token) for increasing the `initialMarginFraction` by (`incrementalInitialMarginFraction` per step).   |

### Portfolio Margining

There is no distinction between realized and unrealized PnL for the purposes of margin calculations. Gains from one position will offset losses from another position within the same account, regardless of whether the profitable position is closed.

### Margin Calculation

The margin requirement for a single position is calculated as follows:

<pre class="center-column">
Initial Margin Requirement = abs(S &times; P &times; I)
Maintenance Margin Requirement = abs(S &times; P &times; M)
</pre>

Where:

* `S` is the size of the position (positive if long, negative if short)
* `P` is the oracle price for the market
* `I` is the initial margin fraction for the market
* `M` is the maintenance margin fraction for the market

The margin requirement for the account as a whole is the sum of the margin requirement over each market `i` in which the account holds a position:

<pre class="center-column">
Total Initial Margin Requirement = Σ abs(S<sub>i</sub> &times; P<sub>i</sub> &times; I<sub>i</sub>)
Total Maintenance Margin Requirement = Σ abs(S<sub>i</sub> &times; P<sub>i</sub> &times; M<sub>i</sub>)
</pre>

The total margin requirement is compared against the total value of the account, which incorporates the quote asset (USDC) balance of the account as well as the value of the positions held by the account:

<pre class="center-column">
Total Account Value = Q + Σ (S<sub>i</sub> &times; P<sub>i</sub>)
</pre>

The Total Account Value is also referred to as equity.

Where:

* `Q` is the account's USDC balance (note that `Q` may be negative). In the API, this is called `quoteBalance`. Every time a transfer, deposit or withdrawal occurs for an account, the balance changes. Also, when a position is modified for an account, the `quoteBalance` changes. Also funding payments and liquidations will change an account's `quoteBalance`.
* `S` and `P` are as defined above (note that `S` may be negative)

An account cannot open new positions or increase the size of existing positions if it would lead the total account value of the account to drop below the total initial margin requirement. If the total account value ever falls below the total maintenance margin requirement, the account may be liquidated.

Free collateral is calculated as:

<pre class="center-column">
Free collateral = Total Account Value - Total Initial Margin Requirement
</pre>

Equity and free collateral can be tracked over time using the latest oracle price (obtained from the markets websocket).

## Liquidations

Accounts whose total value falls below the maintenance margin requirement (described above) may have their positions automatically closed by the liquidation engine. Positions are closed at the close price described below. Profits or losses from liquidations are taken on by the insurance fund.

### Close Price for Liquidations

The close price for a position being liquidated is calculated as follows, depending  whether it is a short or long position:

<pre class="center-column">
Close Price (Short) = P &times; (1 + (M &times; V / W))
Close Price (Long) = P &times; (1 &minus; (M &times; V / W))
</pre>

Where:

* `P` is the oracle price for the market
* `M` is the maintenance margin fraction for the market
* `V` is the total account value, as defined above
* `W` is the total maintentance margin requirement, as defined above

This formula is chosen such that the ratio `V / W` is unchanged as individual positions are liquidated.

## Funding

Funding payments are exchanged between long and short traders to encourage the price of a perpetual contract to trade close to the price of the underlying. If the perpetual trades at a premium relative to the index, long traders will typically make payments to short traders, whereas if the perpetual trades at a discount relative to the index, short traders will typically make payments to long traders.

The payments are credited or debited at the start of each hour, and are included in the realized PnL for the position.

Funding payments can be found by calling [Get /v3/funding](#get-funding-payments) and the predicted funding rate can be found by calling [Get v3/markets](#get-markets).

### Funding Rate Units

Since funding payments are exchanged every hour, the dYdX funding rate is usually represented as a 1-hour rate, which represents the return a position may expect to earn or pay every hour.

When calculating the funding rate, the premium is scaled to have a realization period of 8 hours. That means, for example, that if a certain perpetual market trades consistently at a 0.1% premium relative to the underlying, long traders may expect to pay ~0.1% every 8 hours, and short traders may expect to earn a ~0.1% return every 8 hours (not accounting for the interest rate component).

### Funding Payment Calculation

At the start of each hour, an account receives USDC (if `F` is positive) or pays USDC (if `F` is negative) in an amount equal to:

<pre class="center-column">
F = (-1) &times; S &times; P &times; R
</pre>

Where:

* `S` is the size of the position (positive if long, negative if short)
* `P` is the oracle price for the market
* `R` is the funding rate (as a 1-hour rate)

### Funding Rate Calculation

The main component of the funding rate is a premium that takes into account market activity for the perpetual. It is calculated for each market, every minute (at a random point within the minute) using the formula:

<pre class="center-column">
Premium = (Max(0, Impact Bid Price - Index Price) - Max(0, Index Price - Impact Ask Price)) / Index Price
</pre>

Where the impact bid and impact ask prices are defined as:

<pre class="center-column">
Impact Bid Price = Average execution price for a market sell of the impact notional value
Impact Ask Price = Average execution price for a market buy of the impact notional value
</pre>

And the impact notional amount for a market is:

<pre class="center-column">
Impact Notional Amount = 500 USDC / Initial Margin Fraction
</pre>

For example, for a market with a 10% initial margin fraction, the impact notional value is 5,000 USDC.

At the end of each hour, the premium component is calculated as the simple average (i.e. TWAP) of the 60 premiums calculated over the course of the last hour. In addition to the premium component, each market has a fixed interest rate component that aims to account for the difference in interest rates of the base and quote currencies. The funding rate is then:

<pre class="center-column">
Funding Rate = (Premium Component / 8) + Interest Rate Component
</pre>

Currently, the interest rate component for all dYdX markets is `0.00125%` (equivalent to `0.01%` per 8 hours).

## Contract Loss Mechanisms

During periods of high volatility in the markets underlying the perpetual contracts, the value of some accounts may drop below zero before they can be liquidated.

The insurance fund is the first backstop to maintain the solvency of the system when an account has a negative balance. The account will be liquidated, and the insurance fund will take on the loss.

In the event that the insurance fund is depleted, positions with the most profit and leverage may be used to offset negative-balance accounts, in order to maintain the stability of the system.

## Oracle Prices

The `Oracle Price` for each trading pair is used for the following:

* Ensuring that each account is well-collateralized after each trade
* Determining when an account should be liquidated

### Calculation

Oracle prices are equal to the median of the reported prices of 15 independent Chainlink nodes.

### Node Providers

* Chainlayer
* Inotel
* LinkForest
* SimplyVC
* DexTrac
* Fiews
* dMakers
* linkPool
* SDL
* Ztake
* stakFacils
* infStones
* 01node
* Syncnode
* Vulcan

## Index Prices

The `Index Price` for each trading pair is used for the following:

* Calculating the funding rate
* Triggering "triggerable" order types such as Stop-Limit and Take-Profit orders

### Calculation

Index prices are equal to the median of several exchanges' spot prices.

Each exchange's spot price is calculated as the median of the best-ask, best-bid, and last-traded prices of its spot pair.

If the exchange's quote-asset is a non-USD asset (including USDT), the price is adjusted by our index price for that asset.

### Exchange Sources

#### USDT-USD

For `USDT` pairs where `USDT` is the quote asset, the implied price of `USDT` is taken to be the reciprocal of: the exchange price divided by the index price of the base asset.

* Binance: `USDT-USDC`
* Bitstamp: `USDT-USD`
* Bybit: `USDC-USDT`
* CoinbasePro: `USDT-USD`
* Crypto: `USDT-USD`
* Huobi: `ETH-USDT`
* Kraken: `USDT-USD`
* KuCoin: `BTC-USDT`
* MEXC: `ETH-USDT`
* OKX: `BTC-USDT`

#### ETH-USD

* Binance: `ETH-USDT`
* Bitstamp: `ETH-USD`
* Bybit: `ETH-USDT`
* CoinbasePro: `ETH-USD`
* Kraken: `ETH-USD`
* KuCoin: `ETH-USDT`
* OKX: `ETH-USDT`

#### BTC-USD

* Binance: `BTC-USDT`
* Bitstamp: `BTC-USD`
* Bybit: `BTC-USDT`
* CoinbasePro: `BTC-USD`
* Kraken: `BTC-USD`
* KuCoin: `BTC-USDT`
* OKX: `BTC-USDT`

#### LINK-USD

* Binance: `LINK-USDT`
* Bybit: `LINK-USDT`
* CoinbasePro: `LINK-USD`
* Huobi: `LINK-USDT`
* Kraken: `LINK-USD`
* KuCoin: `LINK-USDT`
* MEXC: `LINK-USDT`
* OKX: `LINK-USDT`

#### AAVE-USD

* Binance: `AAVE-USDT`
* Bybit: `AAVE-USDT`
* CoinbasePro: `AAVE-USD`
* Huobi: `AAVE-USDT`
* Kraken: `AAVE-USD`
* KuCoin: `AAVE-USDT`
* MEXC: `AAVE-USDT`
* OKX: `AAVE-USDT`

#### UNI-USD

* Binance: `UNI-USDT`
* Bybit: `UNI-USDT`
* CoinbasePro: `UNI-USD`
* Gate: `UNI-USDT`
* Huobi: `UNI-USDT`
* Kraken: `UNI-USD`
* MEXC: `UNI-USDT`
* OKX: `UNI-USDT`

#### SUSHI-USD

* Binance: `SUSHI-USDT`
* Bybit: `SUSHI-USDT`
* CoinbasePro: `SUSHI-USD`
* Gate: `SUSHI-USDT`
* Huobi: `SUSHI-USDT`
* Kraken: `SUSHI-USD`
* KuCoin: `SUSHI-USDT`
* MEXC: `SUSHI-USDT`
* OKX: `SUSHI-USDT`

#### SOL-USD

* Binance: `SOL-USDT`
* Bybit: `SOL-USDT`
* CoinbasePro: `SOL-USD`
* Huobi: `SOL-USDT`
* Kraken: `SOL-USD`
* KuCoin: `SOL-USDT`
* MEXC: `SOL-USDT`
* OKX: `SOL-USDT`

#### YFI-USD

* Binance: `YFI-USDT`
* Bybit: `YFI-USDT`
* CoinbasePro: `YFI-USD`
* Gate: `YFI-USDT`
* Huobi: `YFI-USDT`
* Kraken: `YFI-USD`
* MEXC: `YFI-USDT`
* OKX: `YFI-USDT`

#### 1INCH-USD

* Binance: `1INCH-USDT`
* Bybit: `1INCH-USDT`
* CoinbasePro: `1INCH-USD`
* Gate: `1INCH-USDT`
* Huobi: `1INCH-USDT`
* KuCoin: `1INCH-USDT`
* MEXC: `1INCH-USDT`
* OKX: `1INCH-USDT`

#### AVAX-USD

* Binance: `AVAX-USDT`
* Bybit: `AVAX-USDT`
* Coinbase: `AVAX-USD`
* Gate: `AVAX-USDT`
* Huobi: `AVAX-USDT`
* Kraken: `AVAX-USD`
* KuCoin: `AVAX-USDT`
* OKX: `AVAX-USDT`

#### SNX-USD

* Binance: `SNX-USDT`
* Bybit: `SNX-USDT`
* CoinbasePro: `SNX-USD`
* Gate: `SNX-USDT`
* Huobi: `SNX-USDT`
* Kraken: `SNX-USD`
* Kucoin: `SNX-USDT`
* MEXC: `SNX-USDT`
* OKX: `SNX-USDT`

#### CRV-USD

* Binance: `CRV-USDT`
* Bybit: `CRV-USDT`
* CoinbasePro: `CRV-USD`
* Gate: `CRV-USDT`
* Huobi: `CRV-USDT`
* Kraken: `CRV-USD`
* Kucoin: `CRV-USDT`
* MEXC: `CRV-USDT`
* OKX: `CRV-USDT`

#### UMA-USD

* Binance: `UMA-USDT`
* Bybit: `UMA-USDT`
* CoinbasePro: `UMA-USD`
* Gate: `UMA-USDT`
* Huobi: `UMA-USDT`
* KuCoin: `UMA-USDT`
* MEXC: `UMA-USDT`
* OKX: `UMA-USDT`

#### DOT-USD

* Binance: `DOT-USDT`
* Bybit: `DOT-USDT`
* Coinbase: `DOT-USD`
* Gate: `DOT-USDT`
* Huobi: `DOT-USDT`
* Kraken: `DOT-USD`
* KuCoin: `DOT-USDT`
* OKX: `DOT-USDT`

#### DOGE-USD

* Binance: `DOGE-USDT`
* Bybit: `DOGE-USDT`
* Coinbase: `DOGE-USD`
* Gate: `DOGE-USDT`
* Huobi: `DOGE-USDT`
* Kraken: `DOGE-USD`
* KuCoin: `DOGE-USDT`
* OKX: `DOGE-USDT`

#### MATIC-USD

* Binance: `MATIC-USDT`
* Bybit: `MATIC-USDT`
* CoinbasePro: `MATIC-USD`
* Gate: `MATIC-USDT`
* Huobi: `MATIC-USDT`
* Kraken: `MATIC-USD`
* KuCoin: `MATIC-USDT`
* OKX: `MATIC-USDT`

#### MKR-USD

* Binance: `MKR-USDT`
* Bybit: `MKR-USDT`
* CoinbasePro: `MKR-USD`
* Gate: `MKR-USDT`
* Huobi: `MKR-USDT`
* Kraken: `MKR-USD`
* KuCoin: `MKR-USDT`
* OKX: `MKR-USDT`

#### FIL-USD

* Binance: `FIL-USDT`
* Bybit: `FIL-USDT`
* CoinbasePro: `FIL-USD`
* Gate: `FIL-USDT`
* Huobi: `FIL-USDT`
* Kraken: `FIL-USD`
* KuCoin: `FIL-USDT`
* OKX: `FIL-USDT`

#### ADA-USD

* Binance: `ADA-USDT`
* Bybit: `ADA-USDT`
* CoinbasePro: `ADA-USD`
* Gate: `ADA-USDT`
* Huobi: `ADA-USDT`
* Kraken: `ADA-USD`
* KuCoin: `ADA-USDT`
* OKX: `ADA-USDT`

#### ATOM-USD

* Binance: `ATOM-USDT`
* ByBit: `ATOM-USDT`
* CoinbasePro: `ATOM-USD`
* Huobi: `ATOM-USDT`
* Kraken: `ATOM-USD`
* KuCoin: `ATOM-USDT`
* MEXC: `ATOM-USDT`
* OKX: `ATOM-USDT`

#### COMP-USD

* Binance: `COMP-USDT`
* ByBit: `COMP-USDT`
* CoinbasePro: `COMP-USD`
* Huobi: `COMP-USDT`
* Kraken: `COMP-USD`
* KuCoin: `COMP-USDT`
* MEXC: `COMP-USDT`
* OKX: `COMP-USDT`

#### BCH-USD

* Binance: `BCH-USDT`
* Bybit: `BCH-USDT`
* CoinbasePro: `BCH-USD`
* Huobi: `BCH-USDT`
* Kraken: `BCH-USD`
* KuCoin: `BCH-USDT`
* MEXC: `BCH-USDT`
* OKX: `BCH-USDT`

#### LTC-USD

* Binance: `LTC-USDT`
* ByBit: `LTC-USDT`
* CoinbasePro: `LTC-USD`
* Huobi: `LTC-USDT`
* Kraken: `LTC-USD`
* KuCoin: `LTC-USDT`
* MEXC: `LTC-USDT`
* OKX: `LTC-USDT`

#### EOS-USD

* Binance: `EOS-USDT`
* Bybit: `EOS-USDT`
* CoinbasePro: `EOS-USD`
* Huobi: `EOS-USDT`
* Kraken: `EOS-USD`
* KuCoin: `EOS-USDT`
* MEXC: `EOS-USDT`
* OKX: `EOS-USDT`

#### ALGO-USD

* Binance: `ALGO-USDT`
* Bybit: `ALGO-USDT`
* CoinbasePro: `ALGO-USD`
* Gate: `ALGO-USDT`
* Huobi: `ALGO-USDT`
* Kraken: `ALGO-USD`
* KuCoin: `ALGO-USDT`
* OKX: `ALGO-USDT`

#### ZRX-USD

* Binance: `ZRX-USDT`
* Bybit: `ZRX-USDT`
* CoinbasePro: `ZRX-USD`
* Gate: `ZRX-USDT`
* Huobi: `ZRX-USDT`
* Kraken: `ZRX-USD`
* MEXC: `ZRX-USDT`
* OKX: `ZRX-USDT`

#### XMR-USD

* Gate: `XMR-USDT`
* Huobi: `XMR-USDT`
* Kraken: `XMR-USD`
* KuCoin: `XMR-USDT`
* MEXC: `XMR-USDT`

#### ZEC-USD

* Binance: `ZEC-USDT`
* CoinbasePro: `ZEC-USD`
* Gate: `ZEC-USDT`
* HTX: `ZEC-USDT`
* Kraken: `ZEC-USD`
* KuCoin: `ZEC-USDT`
* MEXC: `ZEC-USDT`

#### ENJ-USD

* Binance: `ENJ-USDT`
* CoinbasePro: `ENJ-USD`
* Gate: `ENJ-USDT`
* Huobi: `ENJ-USDT`
* Kraken: `ENJ-USD`
* MEXC: `ENJ-USDT`

#### ETC-USD

* Binance: `ETC-USDT`
* Bybit: `ETC-USDT`
* CoinbasePro: `ETC-USD`
* Gate: `ETC-USDT`
* Huobi: `ETC-USDT`
* Kraken: `ETC-USD`
* KuCoin: `ETC-USDT`
* OKX: `ETC-USDT`

#### XLM-USD

* Binance: `XLM-USDT`
* Bybit: `XLM-USDT`
* CoinbasePro: `XLM-USD`
* Gate: `XLM-USDT`
* Kraken: `XLM-USD`
* KuCoin: `XLM-USDT`
* OKX: `XLM-USDT`

#### TRX-USD

* Binance: `TRX-USDT`
* Bybit: `TRX-USDT`
* Gate: `TRX-USDT`
* Huobi: `TRX-USDT`
* KuCoin: `TRX-USDT`
* MEXC: `TRX-USDT`
* OKX: `TRX-USDT`

#### XTZ-USD

* Binance: `XTZ-USDT`
* Bybit: `XTZ-USDT`
* CoinbasePro: `XTZ-USD`
* Gate: `XTZ-USDT`
* Huobi: `XTZ-USDT`
* Kraken: `XTZ-USD`
* KuCoin: `XTZ-USDT`
* OKX: `XTZ-USDT`

#### ICP-USD

* Binance: `ICP-USDT`
* Bybit: `ICP-USDT`
* CoinbasePro: `ICP-USD`
* Gate: `ICP-USDT`
* Huobi: `ICP-USDT`
* KuCoin: `ICP-USDT`
* OKX: `ICP-USDT`

#### RUNE-USD

* Binance: `RUNE-USDT`
* Bybit: `RUNE-USDT`
* Bitget: `RUNE-USDT`
* Gate: `RUNE-USDT`
* Kraken: `RUNE-USD`
* KuCoin: `RUNE-USDT`

#### NEAR-USD

* Binance: `NEAR-USDT`
* ByBit: `NEAR-USDT`
* CoinbasePro `NEAR-USD`
* Gate: `NEAR-USDT`
* Huobi: `NEAR-USDT`
* KuCoin: `NEAR-USDT`
* OKX: `NEAR-USDT`

#### CELO-USD

* Binance: `CELO-USDT`
* Bybit: `CELO-USDT`
* CoinbasePro: `CELO-USD`
* Gate: `CELO-USDT`
* KuCoin: `CELO-USDT`
* MEXC: `CELO-USDT`
* OKX: `CELO-USDT`


# File: v4-documentation/old-docs/slate-docs/source/includes/_private-v3.md

# Private HTTP API

## Authentication

There are three levels of authentication to be considered when using dYdX. All signing can be handled directly by the client libraries.

### Ethereum Key Authentication

The highest level of authentication is via an account's Ethereum private key. The Ethereum key remains in control of an account's funds while they are within the L2 system. This includes the ability to forcibly close an account's positions and exit the system, in the event that the L2 operators (dYdX and Starkware) were to unexpectedly go offline or otherwise censor requests.

Ethereum key authentication is required for the following operations:

* Register a new user or STARK key
* Create or revoke API keys
* Request a forced withdrawal or forced trade

### STARK Key Authentication

Within the L2 system, authentication is handled by a separate key pair, known as the account's STARK key pair.

STARK key authentication is required for the following operations:

* Place an order
* Withdraw funds

### API Key Authentication

The third level of authentication consists of the API key, secret and passphrase which are used solely to authenticate API requests made to dYdX. This includes operations such as canceling orders or retrieving an account's fills, which do not affect the L2 system.

When a user onboards via `POST v3/onboarding`, the server will use the signature as a seed to determinstically generate default API key credentials. An API key includes three fields:

* `key`: UUID identifying the credentials.
* `secret`: Secret string used to generate HMACs, not sent with requests.
* `passphrase`: Secret string sent with each request, used to encrypt/decrypt the secret in our DB, and never stored in our DB.

API keys can be added and managed via the `/v3/api-keys` endpoints.

All requests which are not signed by an Ethereum key and which are made to private endpoints require an API key signature.

### STARK Key Cryptography

The STARK and API keys are ECDSA key pairs on the [STARK curve](https://docs.starkware.co/starkex-docs/crypto/stark-curve). More info on the cryptography used on L2 is available in [Starkware's documentation](https://docs.starkware.co/starkex-docs/crypto/signatures).

## Creating and Signing Requests

<aside class="success">
Note that the Python and TypeScript clients can generate all required signatures.
</aside>

Within the private HTTP API, there are three groups of endpoints which each require different headers and authentication.

(Separately, and in addition to the above, STARK signatures are required for orders and withdrawals. For details, please refer to the [Python](https://github.com/dydxprotocol/dydx-v3-python/tree/master/dydx3/starkex) and [TypeScript](https://github.com/dydxprotocol/starkex-lib/tree/master/src/signable) reference implementations.)

### Onboarding Endpoint: `POST v3/onboarding`

**Request Headers**

| Header                | Required? | Description                  |
|-----------------------|-----------|------------------------------|
| DYDX-SIGNATURE        | yes       | Ethereum key authentication  |
| DYDX-ETHEREUM-ADDRESS | yes       | Ethereum address of the user |

**Signing**

The header `DYDX-SIGNATURE` is an EIP-712 Ethereum signature on a static message containing the fields:

* `action`: The string `DYDX-ONBOARDING`.
* `onlySignOn`: The string `https://trade.dydx.exchange`.

See reference implementations: [[Python]](https://github.com/dydxprotocol/dydx-v3-python/blob/master/dydx3/modules/onboarding.py) [[TypeScript]](https://github.com/dydxprotocol/v3-client/blob/master/src/modules/onboarding.ts)

### Ethereum Key Private Endpoints

This group includes the `POST` and `DELETE` `v3/api-keys` endpoints for managing API keys. Like the onboarding endpoint, requests to these endpoints require signatures by the user's Ethereum key. 

**Request Headers**

| Header                | Required? | Description                                                                                 |
|-----------------------|-----------|---------------------------------------------------------------------------------------------|
| DYDX-SIGNATURE        | yes       | Ethereum key authentication                                                                 |
| DYDX-ETHEREUM-ADDRESS | yes       | Ethereum address of the user                                                                |
| DYDX-TIMESTAMP        | yes       | ISO timestamp of when the request was signed. Must be within 30 seconds of the server time. |

**Signing**

The header `DYDX-SIGNATURE` is an EIP-712-compliant Ethereum signature on a message containing the fields:

* `method`: The name of the HTTP method used, uppercase (e.g. `GET`).
* `requestPath`: The API endpoint path, beginning with `/v3/`.
* `body`: The HTTP request body (normally empty for `GET` and `DELETE`).
* `timestamp`: Equal to the header `DYDX-TIMESTAMP`.

See reference implementations: [[Python]](https://github.com/dydxprotocol/dydx-v3-python/blob/master/dydx3/modules/api_keys.py) [[TypeScript]](https://github.com/dydxprotocol/v3-client/blob/master/src/modules/keys.ts)

### API Key Private Endpoints

All private endpoints not listed above fall in this category, and must be authenticated via an API key.

**Request Headers**

| Header                | Required? | Description                                                                                 |
|-----------------------|-----------|---------------------------------------------------------------------------------------------|
| DYDX-SIGNATURE        | yes       | HMAC of the request.                                                                         |
| DYDX-API-KEY          | yes       | Api key for the account.                                                                |
| DYDX-TIMESTAMP        | yes       | ISO timestamp of when the request was signed. Must be within 30 seconds of the server time. |
| DYDX-PASSPHRASE       | yes       | The `passphrase` field of the API key.                                                      |
| DYDX-ACCOUNT-NUMBER	  | no        | Account number used to scope the request. Defaults to zero.                                 |

**Signing**

The `DYDX-SIGNATURE` is a SHA-256 HMAC produced as described below, and encoded as a `Base64` string.

A SHA-256 HMAC is created using the API key `secret` and the message `timestamp + method + requestPath + body` defined as follows:

* `timestamp`: The `DYDX-TIMESTAMP` header, which must be within 30 seconds of the server time.
* `method`: The name of the HTTP method used, uppercase (e.g. `GET`).
* `requestPath`: The API endpoint path, beginning with `/v3/`.
* `body`: The HTTP request body (normally empty for `GET` and `DELETE`).

The HMAC should be encoded as a Base64 string and sent as the `DYDX-SIGNATURE` header.

See reference implementations: [[Python]](https://github.com/dydxprotocol/dydx-v3-python/blob/master/dydx3/modules/private.py) [[TypeScript]](https://github.com/dydxprotocol/v3-client/blob/master/src/modules/private.ts)

## Onboarding

### Overview

A few steps are required of all accounts before they can begin trading:

1. [Create a user](#onboarding), providing a STARK public key to be associated with the main account.
1. [Request registration](#get-registration) signature from dYdX.
1. Send registration request to the L1 smart contract.
1. Approve collateral token allowance on the L1 smart contract.
1. Deposit collateral token to the L1 smart contract.

All of these steps are supported by the Python and TypeScript clients. See the Python [integration tests](https://github.com/dydxprotocol/dydx-v3-python/blob/master/integration_tests/test_integration.py) for an example of onboarding and usage of various endpoints.

> Create User

```python
onboarding_information = client.onboarding.create_user(
  # Optional if stark_private_key was provided.
  stark_public_key='012340bcd...',
  stark_public_key_y_coordinate='01234abcd...',
  # Optional if eth_private_key or web3.eth.defaultAccount was provided.
  ethereum_address='ethereumAddress',
  country='SG',
)
```

```typescript
const onboardingInformation: {
  apiKey: ApiKeyCredentials,
  user: UserResponseObject,
  account: AccountResponseObject,
}  = await client.onboarding.createUser(
  {
    starkKey: '71234abcd...',
    starkKeyYCoordinate: '01234abcd...',
    country: 'SG',
  },
  ethereumAddress: 'ethereumAddress',
);
```

```json
{
  "apiKey": {
    "key": "290decd9-548b-62a8-d603-45a988386fc8",
    "passphrase": "S6a8lUhACPY2L5MWDvPl",
    "secret": "KQ3s2VSLYqjWA0WpiDhvyEumvJVIQAj2Ni-TFg7z"
  },
  "user": {
    "ethereumAddress": "0x0913017c740260fea4b2c62828a4008ca8b0d6e4",
    "isRegistered": true,
    "email": "email@dydx.exchange",
    "username": "supersam15o",
    "referredByAffiliateLink": null,
    "makerFeeRate": "0.01",
    "takerFeeRate": "0.01",
    "makerVolume30D": "1000.00",
    "takerVolume30D": "1000.00",
    "fees30D": "00.50",
    "userData": {},
    "dydxTokenBalance": "0",
    "stakedDydxTokenBalance": "0",
    "isEmailVerified": false,
    "isSharingUsername": null,
    "isSharingAddress": true,
    "country": "SG",
  },
  "account": {
    "starkKey": "180913017c740260fea4b2c62828a4008ca8b0d6e4",
    "positionId": "1812",
    "equity": "10000",
    "freeCollateral": "10000",
    "quoteBalance": "10000",
    "pendingDeposits": "0",
    "pendingWithdrawals": "0",
    "createdAt": "2021-04-09T21:08:34.984Z",
    "openPositions": {
      "BTC-USD": {
        "market": "BTC-USD",
        "status": "OPEN",
        "side": "LONG",
        "size": "1000",
        "maxSize": "1050",
        "entryPrice": "100",
        "exitPrice": null,
        "unrealizedPnl": "50",
        "realizedPnl": "100",
        "createdAt": "2021-01-04T23:44:59.690Z",
        "closedAt": null,
        "netFunding": "500",
        "sumOpen": "1050",
        "sumClose": "50"
      }
    },
    "accountNumber": "5",
    "id": "id"
  }
}
```

### HTTP Request
`POST v3/onboarding`

<aside class="warning">
Programmatic users of the API must take care to store private STARK and API keys securely. dYdX does not store any private keys. Using the default key generation methods (such as `derive_stark_key`) ensures keys can be easily recovered by Ethereum key holder. If you generate your STARK key through other means, you must be careful not to lose it, or your funds may be inaccessible for a period of time.
</aside>

Description: Onboard a user so they can begin using dYdX V3 API. This will generate a user, account and derive a key, passphrase and secret from the signature.

### Request

Parameter              | Description
---------------------- | -----------
starkKey               | Public starkKey associated with the key-pair you created.
starkKeyYCoordinate    | Public starkKey Y-Coordinate associated with the key-pair you created.
ethereumAddress        | Ethereum address associated with the user being created.
referredByAffiliateLink| (Optional) Link to affiliate the user was referred by.
country                | (Optional) Country of the user's residence. Must be [ISO 3166-1 Alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) compliant.


### Response

Parameter      | Description
---------------| -----------
apiKey         | See [ApiKeyCredentials](#post-api-keys).
user           | See [User](#get-user).
account        | See [Account](#get-account).

## Derive StarkKey
> Derive StarkKey

```python
key_pair_with_y_coordinate = client.onboarding.derive_stark_key(
  # Optional if eth_private_key or web3.eth.defaultAccount was provided.
  ethereum_address='ethereumAddress',
)
```

```typescript
const keyPairWithYCoordinate: KeyPairWithYCoordinate = await client.onboarding.deriveStarkKey(
  'ethereumAddress',
);
```

<aside class="success">
This method does not access the dYdX API. This is used by the frontend app to derive the STARK key pair in a way that is recoverable. Programmatic traders may optionally derive their STARK key pair in the same way.
</aside>

### Request

Parameter          | Description
------------------ | -----------
ethereumAddress    | Ethereum address associated with the user being created.

### Response

Parameter             | Description
----------------------| -----------
keyPairWithYCoordinate| KeyPairWithYCoordinate.

### KeyPairWithYCoordinate

|field|type|description|
|-----|----|-----------|
|publicKey|string|The x-coordinate of the publicKey.|
|publicKeyYCoordinate|string|The y-coordinate of the publicKey.|
|privateKey|string|The privateKey for the key pair.|

## Recover Default API Credentials
> Recover Default API Credentials

```python
api_credentials = client.onboarding.recover_default_api_key_credentials(
  # Optional if eth_private_key or web3.eth.defaultAccount was provided.
  ethereum_address='ethereumAddress',
)
```

```typescript
const apiCredentials: ApiKeyCredentials = await client.onboarding.recoverDefaultApiCredentials(
  'ethereumAddress',
);
```

<aside class="success">
This method does not access the dYdX API. This can be used to recover the default API key credentials, which are
the same set of credentials used in the dYdX frontend.
</aside>

### Request

Parameter          | Description
------------------ | -----------
ethereumAddress    | Ethereum address associated with the user being created.

### Response

Parameter      | Description
---------------| -----------
apiCredentials | ApiKeyCredentials.

### ApiKeyCredentials

|field|type|description|
|-----|----|-----------|
|key|string|UUID identifying the credentials.|
|secret|string|Secret string used to generate HMACs.|
|passphrase|string|Secret string sent with each request.|

## Recover StarkKey, QuoteBalance and Open Positions
> Recovery

```python
recovery = client.eth_private.recovery(
  # Optional if eth_private_key or web3.eth.defaultAccount was provided.
  ethereum_address='ethereumAddress',
)
```

```typescript
const recovery: {
  starkKey: string,
  positionId: string,
  quoteBalance: string,
  positions: PositionResponseObject[],
} = client.ethPrivate.recovery(
  'ethereumAddress',
);
```

```json
{
  "starkKey": "180913017c740260fea4b2c62828a4008ca8b0d6e4",
  "positionId": "1812",
  "equity": "10000",
  "freeCollateral": "10000",
  "quoteBalance": "10000",
  "positions": [
    {
      "market": "BTC-USD",
      "status": "OPEN",
      "side": "LONG",
      "size": "1000",
      "maxSize": "1050",
      "entryPrice": "100",
      "exitPrice": null,
      "unrealizedPnl": "50",
      "realizedPnl": "100",
      "createdAt": "2021-01-04T23:44:59.690Z",
      "closedAt": null,
      "netFunding": "500",
      "sumOpen": "1050",
      "sumClose": "50"
    }
  ]
}
```

### HTTP Request
`GET v3/recovery`

Description: This is for if you can't recover your starkKey or apiKey and need an additional way to get your starkKey and balance on our exchange, both of which are needed to call the L1 solidity function needed to recover your funds.

### Response

Parameter     | Description
------------- | ----------
starkKey      | Public starkKey associated with the key-pair you created.
positionId    | Starkware-specific positionId.
equity        | The amount of equity (value) in the account. Uses balances and oracle-prices to calculate.
freeCollateral| The amount of collateral that is withdrawable from the account.
quoteBalance  | Human readable quote token balance. Can be negative.
positions     | See [Positions](#get-positions). Note, only open position are returned.

## Get Registration
> Get Registration

```python
signature = client.private.get_registration()
```

```typescript
const signature: { signature: string } = await client.private.getRegistration();
```

```json
{
  "signature": "foo"
}
```

### HTTP Request
`GET v3/registration`

Description: Gets the dYdX provided Ethereum signature required to send a registration transaction to the Starkware smart contract.

### Response

Parameter      | Description
---------------| -----------
signature      | Ethereum signature authorizing the user's Ethereum address to register for the corresponding position id.

## Register API Key
> Register API Key

```python
api_key_response = client.eth_private.create_api_key(
  # Optional if eth_private_key or web3.eth.defaultAccount was provided.
  ethereum_address='0x0123...',
)
```

```typescript
const apiKey: { apiKey: ApiKeyCredentials } = await client.ethPrivate.createApiKey(
  '0x0123...',
);
```

```json
{
  "apiKey": {
    "key": "290decd9-548b-62a8-d603-45a988386fc8",
    "passphrase": "S6a8lUhACPY2L5MWDvPl",
    "secret": "KQ3s2VSLYqjWA0WpiDhvyEumvJVIQAj2Ni-TFg7z"
  }
}
```

### HTTP Request
`POST v3/api-keys`

Description: Create new API key credentials for a user.
Limit: 20 API keys per user.

### Response

Parameter      | Description
---------------| -----------
apiKey         | [ApiKeyCredentials](#apikeycredentials).

## Get API Keys
> Get API Keys

```python
api_keys = client.private.get_api_keys()
```

```typescript
const apiKeys: { keys: string[] } = await client.private.getApiKeys();
```

```json
{
  "apiKeys": [
    "290decd9-548b-62a8-d603-45a988386fc8",
    "390decd9-548b-62a8-d603-45a988386fc8",
    ...
  ]
}
```

### HTTP Request
`GET v3/api-keys`


Description: Get all api keys associated with an Ethereum address.

<aside class="warning">
Note that this endpoint is in the private module, unlike the methods to create or revoke API keys.
</aside>

### Response

Parameter      | Description
---------------| -----------
apiKeys        | Array of apiKey strings corresponding to the ethereumAddress in the request.

## Delete API Key
> Delete API Key

```python
client.eth_private.delete_api_key(
  api_key='290decd9-548b-...',
  # Optional if eth_private_key or web3.eth.defaultAccount was provided.
  ethereum_address='0x0123...',
)
```

```typescript
await client.ethPrivate.delete_api_key(
  '290decd9-548b-...', // API key
  '0x0123...', // Ethereum address
);
```

```json
{
  "apiKey": "foo"
}
```

### HTTP Request
`DELETE v3/api-keys`

Description: Delete an api key by key and Ethereum address.

<aside class="warning">
Deleting your API keys may cause you to be locked out of your account. dYdX will only prevent deleting your last API Key. Proceed with caution when using this endpoint.
</aside>

### Request

Parameter       | Description
----------------| -----------
apiKey          | Public api key being deleted.
ethereumAdddress| Ethereum address the api key is associated with.

### Response

Returns a 200 on success.

## Get User
> Get User

```python
user = client.private.get_user()
```

```typescript
const user: { user: UserResponseObject } = await client.private.getUser();
```

```json
{
  "user": {
    "ethereumAddress": "0x0913017c740260fea4b2c62828a4008ca8b0d6e4",
    "isRegistered": true,
    "email": "email@dydx.exchange",
    "username": "supersam15o",
    "referredByAffiliateLink": null,
    "makerFeeRate": "0.01",
    "takerFeeRate": "0.01",
    "makerVolume30D": "1000.00",
    "takerVolume30D": "1000.00",
    "fees30D": "00.50",
    "userData": {},
    "dydxTokenBalance": "0",
    "stakedDydxTokenBalance": "0",
    "isEmailVerified": false,
    "hedgiesHeld": [1, 2, 3000],
    "country": "CN",
    "languageCode": "zh-CN"
  }
}
```

### HTTP Request
`GET v3/users`

Description: return the user and user information.

### Response

Parameter               | Description
------------------------| -----------
ethereumAddress         | The 20-byte Ethereum address.
isRegistered            | True if the user is registered on the starkware smart contract. This is false otherwise.
email                   | Email address.
username                | User defined username.
referredByAffiliateLink | The affiliate link that referred this user, or null if the user was not referred.
makerFeeRate            | The fee rate the user would be willing to take as the maker. Fee rates are rounded to a 100th of a basis point, or 0.0001%. Note, 1% would be represented as 0.01.
takerFeeRate            | The fee rate the user would be willing to take as the taker. Fee rates are rounded to a 100th of a basis point, or 0.0001%. Note, 1% would be represented as 0.01.
makerVolume30D          | The user's trailing-thirty-day maker volume in USD.
takerVolume30D          | The user's trailing-thirty-day taker volume in USD.
fees30D                 | The user's trailing-thirty-day fees in USD.
userData                | The user's unstructured user data.
dydxTokenBalance        | The user's DYDX token holdings.
stakedDydxTokenBalance  | The user's staked DYDX token holdings
isEmailVerified         | If the user's email address is verified to receive emails from dYdX.
hedgiesHeld             | Indices of all Hedgies held by the user.
country                 | Country of the user's residence. Must be [ISO 3166-1 Alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) compliant.
languageCode            | The user's preferred language. Must be [ISO 639-1](https://en.wikipedia.org/wiki/ISO_639-1) compliant, including 'zh-CN'.

## Update User
> Update user

```python
user = client.private.update_user(
  user_data={},
  email='user@example.com',
  username='username',
  is_sharing_email=False,
  is_sharing_address=True,
  country='SG',
  language_code='en',
)
```

```typescript
const user: { user: UserResponseObject } = await client.private.updateUser({
  email: 'user@example.com',
  username: 'username',
  isSharingEmail: false,
  isSharingAddress: false,
  userData: {},
  country: 'SG',
  languageCode: 'en',
});
```

```json
{
  "user": {
    "ethereumAddress": "0x0913017c740260fea4b2c62828a4008ca8b0d6e4",
    "isRegistered": true,
    "email": "email@dydx.exchange",
    "username": "supersam15o",
    "referredByAffiliateLink": null,
    "makerFeeRate": "0.01",
    "takerFeeRate": "0.01",
    "makerVolume30D": "1000.00",
    "takerVolume30D": "1000.00",
    "fees30D": "00.50",
    "userData": {},
    "dydxTokenBalance": "0",
    "stakedDydxTokenBalance": "0",
    "isEmailVerified": false,
    "country": "SG",
    "languageCode": "en"
  }
}
```

### HTTP Request
`PUT v3/users`

Description: Update user information and return the updated user.

Parameter         | Description
------------------| -----------
userData          | User metadata in a JSON blob.
email             | (Optional) Email to be used with the user.
username          | (Optional) Username to be used for the user.
isSharingUsername | (Optional) Share username publically on leaderboard rankings.
isSharingAddress  | (Optional) Share ETH address publically on leaderboard rankings.
country           | (Optional) Country of the user's residence. Must be [ISO 3166-1 Alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) compliant.
languageCode      | (Optional) The user's preferred language. Must be [ISO 639-1](https://en.wikipedia.org/wiki/ISO_639-1) compliant, including 'zh-CN'.

### Response

Parameter      | Description
---------------| -----------
user           | See [User](#get-user).

## Get User Active Links
> Get User Active Links

```python
links = client.private.get_user_links()
```

```typescript
const userLinks: UserLinksResponseObject = await client.private.getUserLinks();
```

```json
{
  "userType": "SECONDARY",
  "primaryAddress": "0x0913017c740260fea4b2c62828a4008ca8b0d6e4",
  "secondaryAddresses": null
}
```

### HTTP Request
`GET v3/users/links`

Description: return active user links.

### Response

Parameter               | Description
------------------------| -----------
userType                | `PRIMARY`, `SECONDARY`, or null if no active links.
primaryAddress          | Address of the `PRIMARY` user if `userType = SECONDARY`. null otherwise.
linkedAddresses         | Addresses of the `SECONDARY` users if `userType = PRIMARY`. null otherwise.

## Send User Link Request
> Send User Link Request

```python
pending_links = client.private.send_link_request('CREATE_SECONDARY_REQUEST', '0x0913017c740260fea4b2c62828a4008ca8b0d6e4')
```

```typescript
const res: {} = await client.private.sendLinkRequest({
  action: LinkAction.REMOVE,
  address: "0x0913017c740260fea4b2c62828a4008ca8b0d6e4"
});
```

```json
{}
```

### HTTP Request
`POST v3/users/links`

Description: Send a new request to link users, respond to a pending request, or remove a link.

All DYDX rewards will be calculated and distributed to the primary address following the current rewards formulas.

For trading rewards, all formula terms will be summed and aggregated across linked addresses, including fees paid, open interest, and stkDYDX.
For liquidity provider rewards, all formula terms will be summed and aggregated across linked addresses, including depth/score score, stkDYDX, and maker volume. For each market, the max uptime across linked addresses will be used.

### Request

Parameter          | Description
------------------ | -----------
action             | `CREATE_SECONDARY_REQUEST`, `DELETE_SECONDARY_REQUEST`, `ACCEPT_PRIMARY_REQUEST`, `REJECT_PRIMARY_REQUEST`, or `REMOVE`.
address            | Address that the link is with (should not be your own).

### Response

Parameter               | Description
------------------------| -----------
{}                      | Empty object upon success.

### Link Actions

Action                     | Description
-------------------------- | -----------
`CREATE_SECONDARY_REQUEST` | Create a pending link request for the address to become `SECONDARY`, and your address to become `PRIMARY`. Request will be rejected if either address is already linked.
`DELETE_SECONDARY_REQUEST` | Delete an outgoing link request from your address.
`ACCEPT_PRIMARY_REQUEST`   | Accept a pending link request for your address to become `SECONDARY` and their address to become `PRIMARY`.
`REJECT_PRIMARY_REQUEST`   | Reject an incoming pending link request.
`REMOVE`                   | Remove an active link between your address and the other's.

## Get User Pending Link Requests
> Get User Pending Link Requests

```python
pending_links = client.private.get_user_pending_link_requests()
```

```typescript
const userPendingLinks: UserLinkRequestsResponseObject = await client.private.getUserPendingLinkRequests();
```

```json
{
  "userType": null,
  "outgoingRequests": [],
  "incomingRequests": [
    {
      "primaryAddress": "0x99b0599952a4fd2d1a1561fa4c010827ead30354",
      "secondaryAddress": "0x0913017c740260fea4b2c62828a4008ca8b0d6e4"
    }
  ]
}
```

### HTTP Request
`GET v3/users/links/requests`

Description: return pending user links.

### Response

Parameter               | Description
------------------------| -----------
userType                | `PRIMARY`, `SECONDARY`, or null if no active links.
outgoingRequests        | Outgoing requests for another user to be linked as `SECONDARY` to this user. null if `userType = SECONDARY`.
incomingRequests        | Incoming requests for this user to be linked as `SECONDARY` to another user. null if `userType != null`.

## Create An Account
> Create Account

```python
client.private.create_account(
  stark_public_key='701234abcd...',
  stark_public_key_y_coordinate='1234abcd...',
)
```

```typescript
const account: { account: AccountResponseObject } = await client.private.createAccount(
  '701234abcd...', // starkKey
  '1234abcd...', // starkKeyYCoordinate
);
```

```json
{
  "account": {
    "starkKey": "180913017c740260fea4b2c62828a4008ca8b0d6e4",
    "positionId": "1812",
    "equity": "10000",
    "freeCollateral": "10000",
    "quoteBalance": "10000",
    "pendingDeposits": "0",
    "pendingWithdrawals": "0",
    "createdAt": "2021-04-09T21:08:34.984Z",
    "openPositions": {
      "BTC-USD": {
        "market": "BTC-USD",
        "status": "OPEN",
        "side": "LONG",
        "size": "1000",
        "maxSize": "1050",
        "entryPrice": "100",
        "exitPrice": null,
        "unrealizedPnl": "50",
        "realizedPnl": "100",
        "createdAt": "2021-01-04T23:44:59.690Z",
        "closedAt": null,
        "netFunding": "500",
        "sumOpen": "1050",
        "sumClose": "50"
      }
    },
    "accountNumber": "5",
    "id": "id"
  }
}
```

<aside class="warning">
An account will be created automatically during onboarding so this call is not necessary to get started.
</aside>

### HTTP Request
`POST v3/accounts`

Description: Create an account with a given starkKey.

### Request

Parameter          | Description
------------------ | -----------
starkKey           | Public starkKey associated with the key-pair you created.
starkKeyYCoordinate| Public starkKey Y-Coordinate associated with the key-pair you created.


### Response

Parameter      | Description
---------------| -----------
account        | See [Account](#get-account).

## Get Account
> Get Account

```python
account = client.private.get_account(
  # Optional if eth_private_key or web3.eth.defaultAccount was provided.
  ethereum_address='0x0123...',
)
```

```typescript
const account: { account: AccountResponseObject } = await client.private.getAccount(
  '0x0123...',
);
```

```json
{
  "account": {
    "starkKey": "180913017c740260fea4b2c62828a4008ca8b0d6e4",
    "positionId": "1812",
    "equity": "10000",
    "freeCollateral": "10000",
    "quoteBalance": "10000",
    "pendingDeposits": "0",
    "pendingWithdrawals": "0",
    "createdAt": "2021-04-09T21:08:34.984Z",
    "openPositions": {
      "BTC-USD": {
        "market": "BTC-USD",
        "status": "OPEN",
        "side": "LONG",
        "size": "1000",
        "maxSize": "1050",
        "entryPrice": "100",
        "exitPrice": null,
        "unrealizedPnl": "50",
        "realizedPnl": "100",
        "createdAt": "2021-01-04T23:44:59.690Z",
        "closedAt": null,
        "netFunding": "500",
        "sumOpen": "1050",
        "sumClose": "50"
      }
    },
    "accountNumber": "5",
    "id": "id"
  }
}
```

### HTTP Request
`GET v3/accounts/:id`

Description: Get an account for a user by id. Using the client, the id will be generated with client
information and an Ethereum address.

### Request

Parameter      | Description
---------------| -----------
ethereumAddress| Ethereum address associated with an account.

### Response

Parameter         | Description
------------------| -----------
starkKey          | Public StarkKey associated with an account.
positionId        | Starkware-specific positionId.
equity            | The amount of equity (value) in the account. Uses balances and oracle-prices to calculate.
freeCollateral    | The amount of collateral that is withdrawable from the account.
quoteBalance      | Human readable quote token balance. Can be negative.
pendingDeposits   | The sum amount of all pending deposits.
pendingWithdrawals| The sum amount of all pending withdrawal requests.
createdAt         | When the account was first created in UTC.
openPositions     | See [Positions](#get-positions). Note, markets where the user has no position are not returned in the map.
accountNumber     | Unique accountNumber for the account.
id                | Unique id of the account hashed from the userId and the accountNumber.

## Get Account Leaderboard PNLs
> Get Account Leaderboard PNLs

```typescript
const account: { accountPnls: AccountLeaderboardPnlResponseObject } = await client.private.getAccountLeaderboardPnl(
  period=LeaderboardPnlPeriod.DAILY,
);
```

```json
{
  "absolutePnl": "100.000000",
  "percentPnl": "100.000000",
  "absoluteRank": 10,
  "percentRank": 10,
  "startedAt": "2021-08-01T00:00:00.000Z",
  "endsAt": "2021-08-10T00:00:00.000Z",
  "updatedAt": "2021-08-02T22:53:45.659Z",
  "accountId": "afoo",
  "period": "BRONZE",
  "seasonExpectedOutcome": "PROMOTION",
  "seasonNumber": 16,
  "hedgieWon": null,
  "prizeWon": "100000"
}
```

### HTTP Request
`GET v3/accounts/leaderboard-pnl/:period`

Description: Get an account's personal leaderboard pnls.

### Request

Parameter          | Description
-------------------| -----------
period             | "DAILY", "WEEKLY", "MONTHLY", "ALLTIME", "COMPETITION", "DAILY_COMPETITION", or "LEAGUES".
startingBeforeOrAt | (Optional) Latest the leaderboard starts at.

### Response

Parameter             | Description
----------------------| -----------
absolutePnl           | The account's latest updated absolute PNL.
percentPnl            | The account's latest updated percent PNL.
absoluteRank          | User's absolute PNL rank. `null` if not ranked.
percentRank           | User's percent PNL rank. `null` if not ranked.
startedAt             | Starting time for this pnl. Note: will only be set if being used for a competition or leagues. Otherwise, this value will always be `null`.
endsAt                | Ending time for this pnl. Note: will only be set if being used for a competition or leagues. Otherwise, this value will always be `null`. (Can be a future time.)
updatedAt             |	When these leaderboard PNLs were last updated.
accountId             | The account the PNLs are for.
period                | "DAILY", "WEEKLY", "MONTHLY", "ALLTIME", "COMPETITION", "BRONZE", "SILVER", "GOLD", "PLATINUM", "DIAMOND".
seasonExpectedOutcome | User's expected outcome of latest season. "PROMOTION", "DEMOTION", or "SAME_LEAGUE". `null` if not "LEAGUES".
seasonNumber          | Leagues season number. Starts at 1. `null` if not "LEAGUES".
hedgieWon             | Index of hedgie won. `null` if no hedgie won.
prizeWon              | Amount of cash prize won in dollars. `null` if no prize won.


## Get Account Historical Leaderboard PNLs
> Get Account Historical Leaderboard PNLs

```python
historical_leaderboard_pnls = client.private.get_historical_leaderboard_pnls("LEAGUES")
```

```typescript
const historicalLeaderboardPnls: HistoricalLeaderboardPnlsResponseObject = await client.private.getAccountHistoricalLeaderboardPnl(
  period=AccountLeaderboardPnlPeriod.DAILY,
);
```

```json
{
  "leaderboardPnls" : [
    {
      "absolutePnl": "100.000000",
      "percentPnl": "100.000000",
      "absoluteRank": 10,
      "percentRank": 10,
      "startedAt": "2021-08-01T00:00:00.000Z",
      "endsAt": "2021-08-10T00:00:00.000Z",
      "updatedAt": "2021-08-02T22:53:45.659Z",
      "accountId": "afoo",
      "period": "BRONZE",
      "seasonOutcome": "PROMOTION",
      "seasonNumber": 16,
      "hedgieWon": null,
      "prizeWon": "100000"
    },
    ...
  ],
}
```

### HTTP Request
`GET v3/accounts/historical-leaderboard-pnls/:period`

Description: Get an account's historical leaderboard pnls.

### Request

Parameter          | Description
-------------------| -----------
period             | Leaderboard period. "LEAGUES", "DAILY", or "DAILY_COMPETITION".
limit              | Integer between 1 to 10, which indicates the number of most recent leaderboard pnls to be returned. By default this value will be 10.

### Response

Parameter             | Description
----------------------| -----------
leaderboardPnls       | Array of "LeaderboardPnl" from oldest to most recent. See "LeaderboardPnl" below.

### LeaderboardPnl

Parameter             | Description
----------------------| -----------
absolutePnl           | The account's latest updated absolute PNL.
percentPnl            | The account's latest updated percent PNL.
absoluteRank          | User's absolute PNL rank. `null` if not ranked.
percentRank           | User's percent PNL rank. `null` if not ranked.
startedAt             | Starting time for this pnl. Note: will only be set if being used for a competition or leagues. Otherwise, this value will always be `null`.
endsAt                | Ending time for this pnl. Note: will only be set if being used for a competition or leagues. Otherwise, this value will always be `null`. (Can be a future time.)
updatedAt             |	When these leaderboard PNLs were last updated.
accountId             | The account the PNLs are for.
period             | Leaderboard period. "LEAGUES", "DAILY", or "DAILY_COMPETITION".
seasonExpectedOutcome | User's expected outcome of latest season. "PROMOTION", "DEMOTION", or "SAME_LEAGUE". `null` if not "LEAGUES".
seasonNumber          | Leagues season number. Starts at 1. `null` if not "LEAGUES".
hedgieWon             | Index of hedgie won. `null` if no hedgie won.
prizeWon              | Amount of cash prize won in dollars. `null` if no prize won.

## Get Accounts
> Get Account

```python
accounts = client.private.get_accounts()
```

```typescript
const accounts: { accounts: AccountResponseObject[] } = await client.private.getAccounts();
```

```json
{ "accounts": [{
    "starkKey": "180913017c740260fea4b2c62828a4008ca8b0d6e4",
    "positionId": "1812",
    "equity": "10000",
    "freeCollateral": "10000",
    "quoteBalance": "10000",
    "pendingDeposits": "0",
    "pendingWithdrawals": "0",
    "createdAt": "2021-04-09T21:08:34.984Z",
    "openPositions": {
      "BTC-USD": {
        "market": "BTC-USD",
        "status": "OPEN",
        "side": "LONG",
        "size": "1000",
        "maxSize": "1050",
        "entryPrice": "100",
        "exitPrice": null,
        "unrealizedPnl": "50",
        "realizedPnl": "100",
        "createdAt": "2021-01-04T23:44:59.690Z",
        "closedAt": null,
        "netFunding": "500",
        "sumOpen": "1050",
        "sumClose": "50"
      }
    },
    "accountNumber": "5",
    "id": "id"
  }]
}
```

### HTTP Request
`GET v3/accounts`

Description: Get all accounts for a user.

### Response

Parameter      | Description
---------------| -----------
accounts        | See [Account](#get-account). Returns an array of Accounts.

## Get Positions
>Get Positions

```python
from dydx3.constants import MARKET_BTC_USD
from dydx3.constants import POSITION_STATUS_OPEN

all_positions = client.private.get_positions(
  market=MARKET_BTC_USD,
  status=POSITION_STATUS_OPEN,
)
```

```typescript
const positions: { positions: PositionResponseObject[] } = await client.private.getPositions(
  {
    market: Market.BTC_USD,
    status: PositionStatus.OPEN,
  },
);
```

```json
{
  "market": "BTC-USD",
  "status": "OPEN",
  "side": "LONG",
  "size": "1000",
  "maxSize": "1050",
  "entryPrice": "100",
  "exitPrice": null,
  "unrealizedPnl": "50",
  "realizedPnl": "100",
  "createdAt": "2021-01-04T23:44:59.690Z",
  "closedAt": null,
  "netFunding": "500",
  "sumOpen": "1050",
  "sumClose": "50"
}
```

### HTTP Request
`GET v3/positions`

Description: Get all current positions for a user by specified query parameters.

For each market, a position is created with `status=OPEN`. A position is set to `status=CLOSED` when it goes to market-neutral (i.e. `size=0`). On a per-market basis, there should be at most one `status=OPEN` position at any given time.

### Request

Parameter         | Description
------------------| -----------
market            | (Optional) Market of the position.
status            | (Optional) Status of the position. Can be <code>OPEN</code>, <code>CLOSED</code> or <code>LIQUIDATED</code>.
limit             | (Optional) The maximum number of positions that can be fetched via this request. Note, this cannot be greater than 100.
createdBeforeOrAt | (Optional) Set a date by which the positions had to be created.

### Response

Parameter         | Description
------------------| -----------
market            | The market of the position.
status            | The status of the position.
side              | The side of the position. <code>LONG</code> or <code>SHORT</code>.
size              | The current size of the position. Positive if long, negative if short, 0 if closed.
maxSize           | The maximum (absolute value) size of the position. Positive if long, negative if short.
entryPrice        | Average price paid to enter the position.
exitPrice         | Average price paid to exit the position.
unrealizedPnl     | The unrealized pnl of the position in quote currency using the market's [index-price](#index-price-sources) for the position to calculate.
realizedPnl       | The realized pnl of the position in quote currency.
createdAt         | Timestamp of when the position was opened.
closedAt          | Timestamp of when the position was closed.
netFunding        | Sum of all funding payments for this position.
sumOpen           | Sum of all trades sizes that increased the size of this position.
sumClose          | Sum of all trades sizes that decreased the size of this position.

## Get Transfers
> Get Transfers

```python
from dydx3.constants import ACCOUNT_ACTION_DEPOSIT

transfers = client.private.get_transfers(
  transfer_type=ACCOUNT_ACTION_DEPOSIT,
  limit=50,
)
```

```typescript
const transfers: { transfers: TransferResponseObject[] } = await client.private.getTransfers(
  {
    type: AccountAction.DEPOSIT,
    limit: 50,
  },
);
```

```json
{
  "transfers": [{
    "id": "foo",
    "type": "DEPOSIT",
    "debitAsset": "USDC",
    "creditAsset": "USDT",
    "debitAmount": "3000",
    "creditAmount": "2800",
    "transactionHash": "hash",
    "status": "PENDING",
    "createdAt": "2021-01-04T23:44:59.690Z",
    "confirmedAt": null,
    "clientId": "foo",
    "fromAddress": "0x0913017c740260fea4b2c62828a4008ca8b0d6e4",
    "toAddress": null
  }]
}
```

### HTTP Request
`GET v3/transfers`

Description: Get transfers for a user, limited by query parameters.

### Request

Parameter         | Description
------------------| -----------
transferType      | (Optional) Type of the transfer. Can be <code>DEPOSIT</code>, <code>WITHDRAWAL</code> or <code>FAST_WITHDRAWAL</code>.
limit             | (Optional) The maximum number of transfers that can be fetched via this request. Note, this cannot be greater than 100.
createdBeforeOrAt | Latest that the transfers could have been created.

### Response

Parameter         | Description
------------------| -----------
id                | Unique id assigned by dYdX.
type              | Type of the transfer. Will be <code>DEPOSIT</code>, <code>WITHDRAWAL</code> or <code>FAST_WITHDRAWAL</code>.
debitAsset        | Asset that was debited (USDC, USDT, USD, etc).
creditAsset       | Asset that was credited (USDC, USDT, USD, etc).
debitAmount       | Amount that was sent in for the deposit in debitAsset.
creditAmount      | Amount that was credited to the account in creditAsset.
transactionHash   | Ethereum transaction hash of the transfer.
status            | Status of the transfer. Will be <code>PENDING</code> or <code>CONFIRMED</code>.
createdAt         | Timestamp when created.
confirmedAt       | Timestamp when confirmed.
clientId          | ClientId of transfer.
fromAddress       | The Ethereum address the transfer is from.
toAddress         | The Ethereum address the transfer is for.

## Fast vs. Slow Withdrawal

The normal process for withdrawing from L2 to L1 requires waiting for a block of L2 transactions to be collected, and the zero-knowledge proof for the block to be constructed and verified onchain.

Using the fast withdrawal process, users can get their funds on L1 much faster by essentially trading their L2 funds to an “LP” account operated by dYdX, in order to receive immediate liquidity on L1. Since the LP must then recycle these funds from L2 to L1 via the regular withdrawal process, dYdX is only able to process a certain volume of fast withdrawals within a given period of time.

## Create Withdrawal
> Create Withdrawal

```python
from dydx3.constants import ASSET_USDC

withdrawal = client.private.create_withdrawal(
  position_id=1, # required for creating the withdrawal signature
  amount='100',
  asset=ASSET_USDC,
  expiration_epoch_seconds=1613988637,
)
```

```typescript
const withdrawal: { withdrawal: TransferResponseObject } = await client.private.createWithdrawal(
  {
    amount: '100',
    asset: Asset.USDC,
    expiration: '2020-12-28T22:49:31.588Z',
  },
  '1', // positionId required for creating the withdrawal signature
);
```

```json
{
  "withdrawal": {
    "id": "foo",
    "type": "WITHDRAWAL",
    "debitAsset": "USDC",
    "creditAsset": "USDC",
    "debitAmount": "3000",
    "creditAmount": "2800",
    "transactionHash": "hash",
    "status": "PENDING",
    "createdAt": "2021-01-04T23:44:59.690Z",
    "confirmedAt": null,
    "clientId": "foo",
    "fromAddress": "0x0913017c740260fea4b2c62828a4008ca8b0d6e4",
    "toAddress": null
  }
}
```

### HTTP Request
`POST v3/withdrawals`

Description: Create a withdrawal from an account.

<aside class="notice">
If not withdrawing the entirety of your balance, there is a minimum withdrawal amount. Currently that amount is 100 USDC.
</aside>

An additional L1 transaction has to be sent to the Starkware contract to retrieve funds after a slow withdrawal. This cannot be done until the zero-knowledge proof for the block has been constructed and verified onchain. For the L1 transaction, the Ethereum address that the starkKey is registered to must call either the [withdraw](https://github.com/dydxprotocol/starkex-eth/blob/master/src/contracts/starkware-perpetual-abi.json#L1802) or [withdrawTo](https://github.com/dydxprotocol/starkex-eth/blob/master/src/contracts/starkware-perpetual-abi.json#L1907) smart-contract functions. The contract ABI is not tied to a particular client but can be accessed via a [client](https://github.com/dydxprotocol/starkex-eth). All withdrawable funds are withdrawn at once.

Both Layer 1 withdrawal methods can be accessed from [starkex-eth](https://github.com/dydxprotocol/starkex-eth/blob/master/src/modules/Exchange.ts).

### Request

Parameter         | Description
------------------| -----------
amount            | Amount to be withdrawn.
asset             | Asset being withdrawn. Can currently only be <code>USDC</code>.
expiration        | Datetime at which the withdrawal expires if it has not been completed. Expiration must be at least seven days in the future.
clientId          | Unique id of the client associated with the withdrawal. Must be <= 40 characters. When using the client, if not included, will be randomly generated by the client.
signature         | The signature for the withdrawal, signed with the account's STARK private key. When using the client, if not included, will be done by the client. For more information see [above](#creating-and-signing-requests).

### Response

Parameter         | Description
------------------| -----------
withdrawal        | See [Transfers](#get-transfers).

## Create Fast Withdrawal
> Create Fast Withdrawal

```python
from dydx3.constants import ASSET_USDC

fast_withdrawal = client.private.create_fast_withdrawal(
  position_id='1', # required for creating the fast-withdrawal signature
  credit_asset=ASSET_USDC,
  credit_amount='100',
  debit_amount='110',
  to_address='0x98ab...',
  lp_position_id='2',
  expiration_epoch_seconds=1613988637,
  signature='0abc12...',  # Optional if stark_private_key was provided to client.
)
```

```typescript
const fastWithdrawal: { withdrawal: TransferResponseObject } = await client.private.createFastWithdrawal(
  {
    creditAsset: Asset.USDC,
    creditAmount: '100',
    debitAmount: '110',
    toAddress: '0x98ab...',
    lpPositionId: '2',
    clientId: 'client',
    signature: '0abc12...', // Optional if starkPrivateKey was provided to client.
  },
  '1', // positionId required for creating the fast-withdrawal signature
);
```

```json
{
  "withdrawal": {
    "id": "foo",
    "type": "FAST_WITHDRAWAL",
    "debitAsset": "USDC",
    "creditAsset": "USDC",
    "debitAmount": "3000",
    "creditAmount": "2800",
    "transactionHash": "hash",
    "status": "PENDING",
    "createdAt": "2021-01-04T23:44:59.690Z",
    "confirmedAt": null,
    "clientId": "foo",
    "fromAddress": "0x0913017c740260fea4b2c62828a4008ca8b0d6e4",
    "toAddress": null
  }
}
```

### HTTP Request
`POST v3/fast-withdrawals`

Description: Create a fast-withdrawal. [dYdX article on how fast withdrawals work](https://help.dydx.exchange/en/articles/4797387-how-do-deposits-and-withdrawals-work).

### Request

Parameter         | Description
------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
creditAsset       | Asset being withdrawn. Can currently only be <code>USDC</code>.
creditAmount      | Amount that is expected.
debitAmount       | Amount offered in <code>USDC</code> for the credit amount.
toAddress         | Address to be credited.
lpPositionId      | LP Position Id of the debit account.
expiration        | Datetime at which the withdrawal expires if it has not been completed. Expiration must be at least seven days in the future.
signature         | Signature for the fast-withdrawal, signed with the account's STARK private key. When using the client, if not included, will be done by the client. For more information see [above](#creating-and-signing-requests).
clientId          | Unique id of the client associated with the fast-withdrawal. Must be <= 40 characters. When using the client, if not included, will be randomly generated by the client.

`expectedCredit` is the result of computing `debitAmount` - min(`gas_fee`).

### Response

Parameter         | Description
------------------| -----------
withdrawal        | See [Transfers](#get-transfers).

Returns 400 if `expectedCredit` != `creditAmount`.

## Order Types

Type           | Description
-------------- | -----------
MARKET         | Market order (must be FOK or IOC).
LIMIT          | Limit order.
STOP           | Stop limit order.
TRAILING_STOP  | Trailing stop limit order.
TAKE_PROFIT    | Take-profit order.
LIQUIDATED     | Indicates the account was liquidated (fills only).
LIQUIDATION    | Indicates the account took over a liquidated account (fills only).

## Create A New Order

> Create Order

```python
from dydx3.constants import MARKET_BTC_USD
from dydx3.constants import ORDER_SIDE_SELL
from dydx3.constants import ORDER_TYPE_LIMIT
from dydx3.constants import TIME_IN_FORCE_GTT

placed_order = client.private.create_order(
  position_id=1, # required for creating the order signature
  market=MARKET_BTC_USD,
  side=ORDER_SIDE_SELL,
  order_type=ORDER_TYPE_LIMIT,
  post_only=False,
  size='100',
  price='18000',
  limit_fee='0.015',
  expiration_epoch_seconds=1613988637,
  time_in_force=TIME_IN_FORCE_GTT,
)
```

```typescript
const order: { order: OrderResponseObject } = await client.private.createOrder(
  {
    side: OrderSide.SELL,
    type: OrderType.LIMIT,
    timeInForce: TimeInForce.GTT,
    postOnly: false,
    size: '100',
    price: '18000',
    limitFee: '0.015',
    expiration: '2022-12-21T21:30:20.200Z',
  },
  '1', // required for creating the order signature
);
```

```json
{
  "order": {
    "id": "foo",
    "clientId": "foo",
    "accountId": "afoo",
    "market": "BTC-USD",
    "side": "SELL",
    "price": "18000",
    "triggerPrice": null,
    "trailingPercent": null,
    "size": "100",
    "remainingSize": "100",
    "type": "LIMIT",
    "createdAt": "2021-01-04T23:44:59.690Z",
    "unfillableAt": null,
    "expiresAt": "2022-12-21T21:30:20.200Z",
    "status": "PENDING",
    "timeInForce": "GTT",
    "postOnly": false,
    "reduceOnly": false,
    "cancelReason": null
  }
}
```

### HTTP Request
`POST v3/orders`

Description: Create a new order.

### Request

Parameter      | Description
-------------- | -----------
market         | Market of the order.
side           | Either <code>BUY</code> or <code>SELL</sell>.
type           | The type of order. This can be <code>MARKET</code>, <code>LIMIT</code>, <code>STOP_LIMIT</code>, <code>TRAILING_STOP</code> or <code>TAKE_PROFIT</code>.
postOnly       | Whether the order should be canceled if it would fill immediately on reaching the matching-engine.
size           | Size of the order, in base currency (i.e. an ETH-USD position of size 1 represents 1 ETH).
price          | Worst accepted price of the base asset in USD.
limitFee       | Is the highest accepted fee for the trade. See [below](#order-limitfee) for more information.
expiration     | Time at which the order will expire if not filled. This is the Good-Til-Time and is accurate to a granularity of about 15 seconds.
timeInForce    | (Optional) One of <code>GTT</code> (Good til time), <code>FOK</code>(Fill or kill) or <code>IOC</code> (Immediate or cancel). This will default to <code>GTT</code>.
cancelId       | (Optional) The id of the order that is being replaced by this one.
triggerPrice   | (Optional) The triggerPrice at which this order will go to the matching-engine.
trailingPercent| (Optional) The percent that the triggerPrice trails the [index price](#index-price-sources) of the market.
reduceOnly     | (Optional) Whether the order should be [reduce-only](#reduce-only). Only supported on <code>FOK</code>(Fill or kill) or <code>IOC</code> (Immediate or cancel) orders.
clientId       | Unique id of the client associated with the order. Must be <= 40 characters. When using the client, if not included, will be randomly generated by the client.
signature      | Signature for the order, signed with the account's STARK private key. When using the client, if not included, will be done by the client. For more information see [above](#creating-and-signing-requests).

<aside class="notice">
Specifying cancelId will cause the order matching cancelId to be canceled **atomically** (and immediately before) with the new order being placed. This can be used to always have available liquidity on the book when market making. The new order will still be placed even if the old order was already filled.
</aside>

### Response

Parameter    | Description
------------ | -----------
order        | See [order](#get-orders).

## Order LimitFee

The `limitFee` is the highest fee a user would be willing to accept on an order. This should be in decimal form (i.e. 0.1 is 10%). To see current fees, call [GET /v3/users](#get-user) and the maker/taker fee rates show what fees will be. If the order is `postOnly` dYdX will validate against `makerFeeRate` only. The opposite is true if the order is `FOK` or `IOC` - dYdX will only validate against `takerFeeRate`. Otherwise, dYdX assesses against the maximum of maker and taker fee rate.

## Tick Size and Minimum Size

### Tick Size

Each market has a specified <code>tickSize</code>. Order <code>price</code> must be a multiple of the tickSize. The same applies to <code>triggerPrice</code> and <code>trailingPercent</code> if either of these are not null.

### Minimum Size

Each market has a specified <code>minOrderSize</code>. Order <code>size</code> must be not be less than the minOrderSize.

## Order Deletion

Canceled orders older than one month are deleted from the dYdX database.

## Reduce Only

A reduce-only order can only reduce an existing position.

- When user holds no open position, a reduce-only order will always be rejected.
- When user holds an open position, a reduce-only order can only be placed on the other side of the book, with size smaller or equal to the existing position size.

The reduce-only option can be combined with any order type (Limit, Market, Stop Loss, Take Profit, Trailing Stop), but is only available for taker orders (Immediate-or-Cancel and Fill-or-Kill).

`UNTRIGGERED` reduce-only orders are either resized or canceled (with cancel reason `REDUCE_ONLY_RESIZED`) if the underlying position shrinks or no longer exists. When there are multiple `UNTRIGGERED` reduce-only orders and the total order size exceeds the existing position, they will be resized/canceled starting from the order that will be filled last.

<aside class="notice">
Under extremely rare circumstances during outages, reduce-only orders may not execute as expected. During these cases, placing multiple reduce-only orders may result in an opposite position.
</aside>

## Cancel An Order
> Cancel an order

```python
client.private.cancel_order(order_id='0x0000')
```

```typescript
await client.private.cancelOrder('0x0000');
```

```json
{}
```

### HTTP Request
`DELETE v3/orders/:id`

Description: Cancel an order by its unique id.

### Request

Parameter        | Description
---------------- | -----------
orderId          | Unique id of the order to be canceled.

### Response

<aside class="success">
The endpoint returns with status code 200 once the order has been queued for cancelation. The order's status will be updated after the cancelation has been processed by the matching engine.
</aside>

Parameter    | Description
------------ | -----------
cancelOrder  | See [order](#get-orders).

## Cancel Orders
> Cancel Orders

```python
from dydx3.constants import MARKET_BTC_USD

client.private.cancel_all_orders(market=MARKET_BTC_USD)
```

```typescript
await client.private.cancelAllOrders(Market.BTC_USD);
```


```json
{}
```

### HTTP Request
`DELETE v3/orders`

Description: Either bulk cancel all orders or just all orders for a specific market.

### Request

Parameter       | Description
--------------- | -----------
market          | (Optional) Market of the orders being canceled.

### Response

<aside class="success">
The endpoint returns with status code 200 once the orders have been queued for cancelation. The orders' statuses will be updated after the cancelations have been processed by the matching engine.
</aside>

Parameter    | Description
------------ | -----------
cancelOrders | Returns an array of orders to be canceled. See [order](#get-orders).

## Cancel Active Orders
> Cancel Active Orders

```python
from dydx3.constants import MARKET_BTC_USD
from dydx3.constants import ORDER_SIDE_SELL

market_side_orders = client.private.cancel_active_orders(
  market=MARKET_BTC_USD,
  side=ORDER_SIDE_SELL,
)
```

```typescript
const marketSideOrders: {
  cancelOrders: ActiveOrderResponseObject[],
} = await client.private.cancelActiveOrders(
  {
    market: Market.BTC_USD,
    side: OrderSide.SELL,
  },
);
```

```json
{
  "cancelOrders": [
    {
      "id": "id",
      "accountId": "afoo",
      "market": "BTC-USD",
      "side": "SELL",
      "price": "29000",
      "remainingSize": "0.500",
    },
    ...
  ]
}
```

### HTTP Request
`DELETE v3/active-orders`

Description: Cancel active orders that match request parameters.

<aside class="success">
Note that rate-limiting is more generous for this endpoint than DELETE v3/orders. When including side, the rate-limiting becomes even more permissive and when id is included as well as side, the rate-limiting is its most permissive.
</aside>

### Request

Parameter        | Description
---------------- | -----------
market           | Market of the order.
side             | (Optional) Either <code>BUY</code> or <code>SELL</sell>. This parameter is required if `id` is included.
id               | (Optional) The unique id assigned by dYdX. Note, if id is not found, will return a 400.


### Response

<aside class="success">
The endpoint returns with status code 200 once the orders have been queued for cancelation. The orders' statuses will be updated after the cancelations have been processed by the matching engine.
</aside>


Parameter        | Description
---------------- | -----------
cancelOrders | Returns an array of active orders to be canceled. See [activeOrder](#get-active-orders).

## Get Orders
> Get Orders

```python
from dydx3.constants import MARKET_BTC_USD
from dydx3.constants import ORDER_SIDE_SELL
from dydx3.constants import ORDER_TYPE_LIMIT
from dydx3.constants import ORDER_STATUS_OPEN

all_orders = client.private.get_orders(
  market=MARKET_BTC_USD,
  status=ORDER_STATUS_OPEN,
  side=ORDER_SIDE_SELL,
  type=ORDER_TYPE_LIMIT,
  limit=50,
)
```

```typescript
const allOrders: { orders: OrderResponseObject[] } = await client.private.getOrders(
  {
    market: Market.BTC_USD,
    status: OrderStatus.OPEN,
    side: OrderSide.SELL,
    type: OrderType.LIMIT,
    limit: 50,
  },
);
```

```json
{
  "orders": [
    {
      "id": "id",
      "clientId": "foo",
      "accountId": "afoo",
      "market": "BTC-USD",
      "side": "SELL",
      "price": "29000",
      "triggerPrice": null,
      "trailingPercent": null,
      "size": "0.500",
      "remainingSize": "0.500",
      "type": "LIMIT",
      "createdAt": "2021-01-04T23:44:59.690Z",
      "unfillableAt": null,
      "expiresAt": "2021-02-04T23:44:59.690Z",
      "status": "OPEN",
      "timeInForce": "GTT",
      "postOnly": false,
      "cancelReason": null
    },
    ...
  ]
}
```

### HTTP Request
`GET v3/orders`

Description: Get active (not filled or canceled) orders for a user by specified parameters.

### Request

Parameter        | Description
---------------- | -----------
market           | (Optional) Market of the order.
status           | (Optional) A list of statuses to filter by. Must be in the subset <code>PENDING|OPEN|UNTRIGGERED</code>.
side             | (Optional) Either <code>BUY</code> or <code>SELL</sell>.
type             | (Optional) The expected type of the order. This can be <code>LIMIT</code>, <code>STOP</code>, <code>TRAILING_STOP</code> or <code>TAKE_PROFIT</code>.
limit            | (Optional) The maximum number of orders that can be fetched via this request. Note, this cannot be greater than 100.
createdBeforeOrAt| (Optional) Set a date by which the orders had to be created.
returnLatestOrders| (Optional) Returns the most recently created orders instead of the oldest and the order is from most recent to least recent (up to `limit`).

### Response

Parameter        | Description
---------------- | -----------
orders           | An array of orders. See order below.

### Order

Parameter        | Description
---------------- | -----------
id               | The unique id assigned by dYdX.
clientId         | The unique id assigned by the client.
accountId        | The id of the account.
market           | Market of the fill.
side             | Either <code>BUY</code> or <code>SELL</sell>.
price            | The price of the order. Must adhere to the market's tick size.
triggerPrice     | The trigger price of the order. Must adhere to the market's tick size.
trailingPercent  | Used for trailing stops. Percent drop from maximum price that will trigger the order.
size             | Total size (base currency) of the order
remainingSize    | Size of order not yet filled.
type             | The [type](#order-types) of the fill.
createdAt        | Timestamp when the fill was created.
unfillableAt     | Time order was either filled or canceled.
expiresAt        | Time order will expire.
status           | See order statuses below.
timeInForce      | One of <code>GTT</code> (Good til time), <code>FOK</code>(Fill or kill) or <code>IOC</code> (Immediate or cancel). This will default to <code>GTT</code>.
postOnly         | If the order will cancel if it would take the position of <code>TAKER</code>.
cancelReason     | See cancel reasons below.

### Order Statuses

Status           | Description
---------------- | -----------
PENDING          | Order has yet to be processed by the matching engine.
OPEN             | Order is active and on the orderbook. Could be partially filled.
FILLED           | Fully filled.
CANCELED         | Canceled, for one of the cancel reasons. Could be partially filled.
UNTRIGGERED      | Triggerable order that has not yet been triggered.

### Cancel Reasons

Reason           | Description
-------------------- | -----------
UNDERCOLLATERALIZED  | Order would have led to an undercollateralized state for the user.
EXPIRED              | Order expired.
USER_CANCELED        | Order was canceled by the user.
SELF_TRADE           | Order would have resulted in a self trade for the user.
FAILED               | An internal issue caused the order to be canceled.
COULD_NOT_FILL       | A FOK or IOC order could not be fully filled.
POST_ONLY_WOULD_CROSS| A post-only order would cross the orderbook.

## Get Active Orders
> Get Active Orders

```python
from dydx3.constants import MARKET_BTC_USD
from dydx3.constants import ORDER_SIDE_SELL

market_side_orders = client.private.get_active_orders(
  market=MARKET_BTC_USD,
  side=ORDER_SIDE_SELL,
)
```

```typescript
const marketSideOrders: {
  orders: ActiveOrderResponseObject[],
} = await client.private.getActiveOrders(
  {
    market: Market.BTC_USD,
    side: OrderSide.SELL,
  },
);
```

```json
{
  "orders": [
    {
      "id": "id",
      "accountId": "afoo",
      "market": "BTC-USD",
      "side": "SELL",
      "price": "29000",
      "remainingSize": "0.500",
    },
    ...
  ]
}
```

### HTTP Request
`GET v3/active-orders`

Description: Get active (not filled or canceled) orders for a user by specified parameters.

<aside class="success">
Note that rate-limiting is more generous for this endpoint than GET v3/orders. When including side, the rate-limiting becomes even more permissive and when id is included as well as side, the rate-limiting is its most permissive.
</aside>

### Request

Parameter        | Description
---------------- | -----------
market           | Market of the order.
side             | (Optional) Either <code>BUY</code> or <code>SELL</sell>. This parameter is required if `id` is included.
id               | (Optional) The unique id assigned by dYdX. Note, if id is not found, will return a 400.


### Response

Parameter        | Description
---------------- | -----------
orders           | An array of activeOrders. See activeOrder below.

### ActiveOrder

Parameter        | Description
---------------- | -----------
id               | The unique id assigned by dYdX.
accountId        | The id of the account.
market           | Market of the fill.
side             | Either <code>BUY</code> or <code>SELL</sell>.
price            | The price of the order. Must adhere to the market's tick size.
remainingSize    | Size of order not yet filled.

## Get Order By Id
>Get Order By Id

```python
order = client.private.get_order_by_id('foo')
```

```typescript
const orderResponse: { order: OrderResponseObject } = await client.private.getOrderById('foo');
```

```json
{
  "order": {
    "id": "foo",
    "clientId": "foo",
    "accountId": "afoo",
    "market": "BTC-USD",
    "side": "SELL",
    "price": "29000",
    "triggerPrice": null,
    "trailingPercent": null,
    "size": "0.500",
    "remainingSize": "0.500",
    "type": "LIMIT",
    "createdAt": "2021-01-04T23:44:59.690Z",
    "unfillableAt": null,
    "expiresAt": "2021-02-04T23:44:59.690Z",
    "status": "OPEN",
    "timeInForce": "GTT",
    "postOnly": false,
    "cancelReason": null
  }
}
```

### HTTP Request
`GET v3/orders/:id`

Description: Get an order by <code>id</code> from the active orderbook and order history.

### Request

Parameter    | Description
------------ | -----------
id           | Unique id of the order

### Response

Parameter    | Description
------------ | -----------
order        | See [order](#get-orders).

## Get Order by ClientId
>Get Order By ClientId

```python
order = client.private.get_order_by_client_id('clientId')
```

```typescript
const allOrders: { order: OrderResponseObject } = await client.private.getOrderByClientId('clientId');
```

```json
{
  "order": {
    "id": "foo",
    "clientId": "foo",
    "accountId": "afoo",
    "market": "BTC-USD",
    "side": "SELL",
    "price": "29000",
    "triggerPrice": null,
    "trailingPercent": null,
    "size": "0.500",
    "remainingSize": "0.500",
    "type": "LIMIT",
    "createdAt": "2021-01-04T23:44:59.690Z",
    "unfillableAt": null,
    "expiresAt": "2021-02-04T23:44:59.690Z",
    "status": "OPEN",
    "timeInForce": "GTT",
    "postOnly": false,
    "cancelReason": null
  }
}
```

### HTTP Request
`GET v3/orders/client/:id`

Description: Get an order by <code>clientId</code> from the active orderbook and order history. Only the latest 1 hour of orders can be fetched from this endpoint.

### Request

Parameter    | Description
------------ | -----------
id           | Unique clientId of the order

### Response

Parameter    | Description
------------ | -----------
order        | See [order](#get-orders).

## Get Fills
>Get Fills

```python
from dydx3.constants import MARKET_BTC_USD

all_fills = client.private.get_fills(
  market=MARKET_BTC_USD,
)
```

```typescript
const allFills: { fills: FillResponseObject[] } = await client.private.getFills(
  {
    market: Market.BTC_USD,
  },
);
```

```json
{
  "fills": [
    {
      "id": "foo",
      "side": "BUY",
      "liquidity": "TAKER",
      "type": "LIMIT",
      "market": "BTC-USD",
      "orderId": "id",
      "price": "29000",
      "size": "0.001",
      "fee": "100",
      "createdAt": "2021-01-05T16:33:43.163Z"
    },
    ...
  ]
}
```

### HTTP Request
`GET v3/fills`

Description: Get Fills for a user by specified parameters.

### Request

Parameter        | Description
---------------- | -----------
market           | (Optional) Market of the fills.
orderId          | (Optional) Unique order id. Will only fetch a single order.
limit            | (Optional) The maximum number of fills that can be fetched via this request. Note, this cannot be greater than 100.
createdBeforeOrAt| (Optional) Set a date by which the fills had to be created.

### Response

Parameter        | Description
---------------- | -----------
fills            | Array of fills. See below for an individual example.

### Fill

Parameter        | Description
---------------- | -----------
id               | The unique id assigned by dYdX.
side             | Either <code>BUY</code> or <code>SELL</sell>.
liquidity        | Either <code>MAKER</code> or <code>TAKER</sell>.
type             | The [type](#order-types) of the fill.
market           | Market of the fill.
orderId          | Id of the order which caused this fill. null if type is <code>LIQUIDATED</code> or <code>LIQUIDATION`</code>.
price            | The price the fill occurred at (in quote / base currency).
size             | Size that was filled (in base currency).
fee              | Fee that was charged (in quote currency).
createdAt        | Timestamp when the fill was created.

## Get Funding Payments
> Get Funding Payments

```python
from dydx3.constants import MARKET_BTC_USD

funding_payments = client.private.get_funding_payments(
  market=MARKET_BTC_USD,
  limit=75,
)
```

```typescript
const fundingPayments: { fundingPayments: FundingResponseObject } = await client.private.getFundingPayments(
  {
    market: Market.BTC_USD,
    limit: 75,
  },
);
```

```json
{
  "fundingPayments": [{
    "market": "BTC-USD",
    "payment": "10000",
    "rate": "0.0000125000",
    "positionSize": "500",
    "price": "90",
    "effectiveAt": "2021-01-04T23:44:59.690Z"
  }]
}
```

### HTTP Request
`GET v3/funding`

Description: Get Funding Payments made to an account.

### Request

Parameter          | Description
-------------------| -----------
market             | (Optional) Market of the funding payments.
limit              | (Optional) The maximum number of funding payments that can be fetched via this request. Note, this cannot be greater than 100.
effectiveBeforeOrAt| (Optional) Set a date by which the funding payments had to be created.

### Response

Parameter          | Description
-------------------| -----------
market             | Market corresponding to the funding payment.
payment            | Change in the `quoteBalance` of the account. Positive if the user received funding and negative if the user paid funding.
rate               | Funding rate at the time of this payment (as a 1-hour rate).
positionSize       | User's position size at the time of this funding payment. positive if long, negative if short.
price              | Oracle price used to calculate this funding payment.
effectiveAt        | Time of this funding payment.

## Get Historical PNL Ticks
> Get Historical PNL Ticks

```python
historical_pnl = client.private.get_historical_pnl(
  created_before_or_at='2021-04-09T22:02:46+0000',
)
```

```typescript
const historicalPnlTicks: {
  historicalPnl: HistoricalPnlResponseObject[],
} = await client.private.getHistoricalPnl(
  {
    createdBeforeOrAt: '2021-04-09T22:02:46+0000',
  },
);
```

```json
{
  "historicalPnl": [{
    "equity": "0.0000",
    "totalPnl": "0.0000",
    "createdAt": "2021-04-09T21:08:34.984Z",
    "netTransfers": "0.0000",
    "accountId": "49979004..."
  }]
}
```

### HTTP Request
`GET v3/historical-pnl`

Description: Get Historical PNL for an account during an interval.

<aside class="warning">
The max interval of ticks is 1 month. If a single time value is provided, the other value will default to one month away from said value (i.e. set createdBeforeOrAt and createdOnOrAfter will be a month before). If neither value is set, the interval will be the current past roughly 30 days.
</aside>

### Request

Parameter          | Description
-------------------| -----------
createdBeforeOrAt  | (Optional) Used for setting a ending bounds on the ticks.
createdOnOrAfter   | (Optional) Used for setting a starting bounds on the ticks.

### Response

Parameter          | Description
-------------------| -----------
historicalPnl      | Array of HistoricalAggregatedPnl. See "HistoricalAggregatedPnl" below.

### HistoricalAggregatedPnl
Parameter          | Description
-------------------| -----------
equity             | The total account equity.
totalPnl           | The total PNL for the account since inception.
createdAt          | When the tick was recorded.
netTransfers       | The value into or out of the account of transfers since the last interval.
accountId          | Account the tick is for.

## Get Trading Rewards
> Get Trading Rewards

```python
rewards = client.private.get_trading_rewards(
  epoch=0,
)
```

```typescript
const rewards: {
  tradingRewards: TradingRewardsResponseObject,
} = await client.private.getTradingRewards(
  {
    epoch: 5,
  },
);
```

```json
{
  "epoch": 5,
  "epochStart": "2021-12-21T15:00:00.000Z",
  "epochEnd": "2022-01-18T15:00:00.000Z",
  "fees": {
    "feesPaid": "0.1",
    "totalFeesPaid": "1"
  },
  "openInterest": {
    "averageOpenInterest": "10",
    "totalAverageOpenInterest": "100"
  },
  "stakedDYDX": {
    "primaryStakedDYDX": "0",
    "averageStakedDYDX": "200",
    "averageStakedDYDXWithFloor": "200",
    "totalAverageStakedDYDX": "2000"
  },
  "weight": {
    "weight": "0.1",
    "totalWeight": "1"
  },
  "totalRewards": "383561.6",
  "estimatedRewards": "3835616"
}
```

### HTTP Request
`GET v3/rewards/weight`

Description: Get the rewards weight of a given epoch.

### Request

Parameter          | Description
-------------------| -----------
epoch              | (Optional) Epoch number to request rewards data for. Defaults to current epoch.
secondaryAddress   | (Optional) Get rewards for a linked, `SECONDARY` address.

### Response

Parameter          | Description
-------------------| -----------
epoch              | ID of the epoch.
epochStart         | Time when the epoch starts.
epochEnd           | Time when the epoch ends.
fees               | See "Fees" below.
openInterest       | See "OpenInterest" below.
weight             | See "Weight" below.
stakedDYDX         | See "StakedDYDX" below.
totalRewards       | The total number of tokens that will be given out at the end of the epoch.
estimatedRewards   | The user's estimated number of dYdX tokens as rewards.

### Weight
Parameter          | Description
-------------------| -----------
weight             | The user's current weight score for this epoch.
totalWeight        | The sum of the weight score of all users for this epoch.

### Fees
Parameter          | Description
-------------------| -----------
feesPaid           | The USD amount of fees paid by the user in the epoch.
totalFeesPaid      | The total USD amount of fees paid by all users in the epoch.

### OpenInterest
Parameter                | Description
-------------------------| -----------
averageOpenInterest	     | The average open interest for the user.
totalAverageOpenInterest | The total average open interest for all users.

### StakedDYDX
Parameter                  |Description
---------------------------|-----------
primaryStakedDYDX          | The average staked DYDX of the primary user if own user `linkType = SECONDARY` or `secondaryAddress` is included. `'0'` for epochs 0-4 (old rewards formula). `null` otherwise.
averageStakedDYDX          | The average staked DYDX for the user. This value is `'0'` for epochs 0-4 (old rewards formula does not take into account stakedDYDX).
averageStakedDYDXWithFloor | The average staked DYDX for the user, taking into account both `primaryStakedDYDX` and the [rewards formula's](https://commonwealth.im/dydx/proposal/discussion/2940-drc-update-trading-liquidity-provider-rewards-formulas-to-include-holding-of-stkdydx) floor stakedDYDX value. This value is `'0'` for epochs 0-4 (old rewards formula does not take into account stakedDYDX).
totalAverageStakedDYDX     | The total average staked DYDX for all users. This value is `'0'` for epochs 0-4 (old rewards formula does not take into account stakedDYDX).

## Get Liquidity Provider Rewards
> Get Liquidity Provider Rewards

<aside class="warning">
This API is only supported for epochs 13+. For previous epochs, please use the `Get Liquidity Rewards` endpoint.
</aside>

```python
rewards = client.private.get_liquidity_provider_rewards_v2(
  epoch=13,
)
```

```typescript
const rewards: {
  liquidityRewards: LiquidityProviderRewardsV2ResponseObject,
} = await client.private.getLiquidityProviderRewardsV2(
  {
    epoch: 13,
  },
);
```

```json
{
  "epoch": 13,
  "epochStart": "2021-8-02T15:00:00.000Z",
  "epochEnd": "2022-08-30T15:00:00.000Z",
  "markets": {
    "BTC-USD": {
      "market": "BTC-USD",
      "depthSpreadScore": "0.5",
      "uptime": "500",
      "linkedUptime": "7500",
      "maxUptime": "10000",
      "score": "0.00098821176880261854125",
      "totalScore": "1",
      "makerVolume": "10000",
      "totalMakerVolume": "100000",
      "totalRewards": "230137",
      "estimatedRewards": "227.42409183692822322765125",
      "secondaryAllocation": "0"
    }
    ...
  },
  "stakedDYDX": {
    "averageStakedDYDX": "1000",
    "totalAverageStakedDYDX": "10000"
  },
  "linkedAddressRewards": {
    "0x0913017c740260fea4b2c62828a4008ca8b0d6e4": {
      "markets": {
        "BTC-USD": {
          "market": "BTC-USD",
          "depthSpreadScore": "0.5",
          "uptime": "500",
          "linkedUptime": "7500",
          "maxUptime": "10000",
          "score": "0.00098821176880261854125",
          "totalScore": "1",
          "makerVolume": "10000",
          "totalMakerVolume": "100000",
          "totalRewards": "230137",
          "estimatedRewards": "227.42409183692822322765125",
          "secondaryAllocation": "0.5"
        }
        ...
      },
      "averageStakedDYDX": "750"
    }
  }
}
```

### HTTP Request
`GET v3/rewards/liquidity-provider`

Description: Get the liquidity provider rewards of a given epoch (epochs 13+).

### Request

Parameter          | Description
-------------------| -----------
epoch              | (Optional) Epoch number to request rewards data for. Defaults to current epoch.

### Response

Parameter            | Description
---------------------| -----------
epoch                | ID of the epoch.
epochStart           | Time when the epoch starts.
epochEnd             | Time when the epoch ends.
markets              | Map of market name to liquidity rewards for that market. See "LiquidityRewards" below.
stakedDYDX           | See "StakedDYDX" below.
linkedAddressRewards | For a `PRIMARY` address, map of linked address to rewards data for that address. Includes the `PRIMARY` address. See "PerAddressRewards" below. 

### LiquidityRewards
Parameter           | Description
--------------------| -----------
market              | The market for which the rewards are for.
depthSpreadScore    | The user's depth and spread score for this market.
uptime              | The ratio of uptime (non-zero scores) that the user has for this market.
linkedUptime        | For a `SECONDARY` address, the max uptime of linked addresses, which will be used in rewards calculation. `0` otherwise.
maxUptime           | The number of samples taken for this market.
score               | The user's total score for this market.
totalScore          | The total score of all liquidity providers who are eligible for liquidity rewards.
makerVolume         | The maker volume for the user.
totalMakerVolume    | The total maker volume for all liquidity providers.
estimatedRewards    | The user's estimated number of dYdX tokens as rewards for this market. For a `SECONDARY` address, this field is the amount of rewards contributed to the `PRIMARY` address (`SECONDARY` addresses do not receive rewards).
totalRewards        | The total number of tokens that will be given out at the end of the epoch for this market.
secondaryAllocation | For a `SECONDARY` address, the proportion (0 to 1) of the `PRIMARY` address rewards that are based on this address contribution. `0` otherwise.

### StakedDYDX
Parameter              | Description
-----------------------| -----------
averageStakedDYDX      | The average staked DYDX for the user. For a `PRIMARY` address, this is the aggregate `averageStakedDYDX` across all linked addresses.
totalAverageStakedDYDX | The total average staked DYDX for all eligible users.

### PerAddressRewards
Parameter              | Description
-----------------------| -----------
markets                | Map of market name to liquidity rewards for that market for the respective address. See "LiquidityRewards" above.
averageStakedDYDX      | The average staked DYDX for the respective address.

## Get Liquidity Rewards (Deprecated)
> Get Liquidity Rewards

<aside class="warning">
This API is now deprecated. Please use it to fetch rewards for only epoch 0-12. For future epochs, please use the `Get Liquidity Provider Rewards` endpoint.
</aside>

```python
rewards = client.private.get_liquidity_provider_rewards(
  epoch=0,
)
```

```typescript
const rewards: {
  liquidityRewards: LiquidityProviderRewardsResponseObject,
} = await client.private.getLiquidityProviderRewards(
  {
    epoch: 5,
  },
);
```

```json
{
  "epoch": 5,
  "epochStart": "2021-12-21T15:00:00.000Z",
  "epochEnd": "2022-01-18T15:00:00.000Z",
  "markets": {
    "BTC-USD": {
      "market": "BTC-USD",
      "uptime": "0.5",
      "score": "0.00098821176880261854125",
      "totalScore": "1",
      "totalRewards": "230137",
      "estimatedRewards": "227.42409183692822322765125",
    }
    ...
  },
  "stakedDYDX": {
    "primaryStakedDYDX": "0",
    "averageStakedDYDX": "1000",
    "totalAverageStakedDYDX": "10000"
  }
}
```

### HTTP Request
`GET v3/rewards/liquidity`

Description: Get the liquidity rewards of a given epoch.

### Request

Parameter          | Description
-------------------| -----------
epoch              | (Optional) Epoch number to request rewards data for. Defaults to current epoch.
secondaryAddress   | (Optional) Get rewards for a linked, `SECONDARY` address.

### Response

Parameter          | Description
-------------------| -----------
epoch              | ID of the epoch.
epochStart         | Time when the epoch starts.
epochEnd           | Time when the epoch ends.
markets            | Map of market name to rewards for that market. See "LiquidityRewards" below.
stakedDYDX         | See "StakedDYDX" below.

### LiquidityRewards
Parameter          | Description
-------------------| -----------
market             | The market for which the rewards are for.
depthSpreadScore   | The user's depth and spread score for this market.
uptime             | The ratio of uptime (non-zero scores) that the user has for this market.
maxUptime          | The number of samples taken for this market.
score              | The user's total score for this market.
totalScore         | The total score of all liquidity providers who are eligible for liquidity rewards.
makerVolume        | The maker volume for the user. `0` for epochs 0-9 (old rewards formulas).
totalMakerVolume   | The total maker volume for all liquidity providers. `0` for epochs 0-4 (old rewards formula).
totalRewards       | The total number of tokens that will be given out at the end of the epoch for this market.
estimatedRewards   | The user's estimated number of dYdX tokens as rewards for this market.

### StakedDYDX
Parameter              | Description
-----------------------| -----------
primaryStakedDYDX      | The average staked DYDX of the primary user if own user `linkType = SECONDARY` or if `secondaryAddress` is included. `'0'` for epochs 0-4 (old rewards formula). `null` otherwise.
averageStakedDYDX      | The average staked DYDX for the user. This value is `'0'` for epochs 0-4 (old rewards formula does not take into account stakedDYDX).
totalAverageStakedDYDX | The total average staked DYDX for all eligible users. This value is `'0'` for epochs 0-4 (old rewards formula does not take into account stakedDYDX).

## Get Retroactive Mining Rewards
> Get Retroactive Mining Rewards

```python
rewards = client.private.get_retroactive_mining_rewards()
```

```typescript
const rewards: {
  retroactiveMiningRewards: RetroactiveMiningRewardsResponseObject,
} = await client.private.getRetroactiveMiningRewards();
```

```json
{
  "epoch": 0,
  "epochStart": "2021-08-03T15:00:00.000Z",
  "epochEnd": "2021-08-31T15:00:00.000Z",
  "retroactiveMining": {
    "allocation": "1000",
    "targetVolume": "500",
    "volume": "100"
  },
  "estimatedRewards": "500"
}
```

### HTTP Request
`GET v3/rewards/retroactive-mining`

Description: Get the retroactive mining rewards of a given epoch.

### Response

Parameter          | Description
-------------------| -----------
epoch              | Will always be '0'.
epochStart         | Time when the epoch starts.
epochEnd           | Time when the epoch ends.
retroactiveMining  | See "RetroactiveMiningRewards" below.
estimatedRewards   | The user's estimated number of dYdX tokens as rewards.

### RetroactiveMiningRewards
Parameter          | Description
-------------------| -----------
allocation         | The number of allocated dYdX tokens for the user.
targetVolume       | The user's required trade volume (in USD) to be able to claim the allocation.
volume             | The user's current total trade volume (in USD) in the epoch.

## Send Verification Email
> Send a verification email

```python
client.private.send_verification_email()
```

```typescript
await client.private.sendVerificationEmail();
```

```json
{}
```

### HTTP Request
`PUT v3/emails/send-verification-email`

Description: Send an email to the email address associated with the user, requesting that they click on a link to verify their email address.

### Response

On success, returns a `204` response with an empty body. Responds with a `400` error if no email address is on file for the user, or their email address has already been verified.

### Setting Notification Status

In addition to verifying an email, notifications must be set in `user.userData` to start receiving emails per category.

> Example userData:

```
user.userData = {
  notifications: {
    deposit: {
      email: true
    },
    trades: {
      email: true
    }
  }
}
```

## Request Testnet Tokens
> Request Testnet Tokens

```python
transfer = client.private.request_testnet_tokens()
```

```typescript
const transfer: { transfer: TransferResponseObject } = await client.private.requestTestnetTokens();
```

```json
{
    "transfer": {
        "id": "e5ed0207-27fe-5cfa-a74e-b3908a113dca",
        "type": "TRANSFER_OUT",
        "debitAsset": "USDC",
        "creditAsset": "USDC",
        "debitAmount": "10000",
        "creditAmount": "0",
        "transactionHash": null,
        "status": "PENDING",
        "createdAt": "2021-11-09T01:29:59.960Z",
        "confirmedAt": null,
        "clientId": "521ba97550e9299",
        "fromAddress": null,
        "toAddress": null
    }
}
```

### HTTP Request
`POST v3/testnet/tokens`

Description: Requests tokens on dYdX's staging server.

<aside class="notice">
This endpoint is only enabled on Staging/Goerli, and will not work on Mainnet/Production.
</aside>

A fixed number of tokens will be transferred to the account. Please take note of [rate limits](#rate-limit-api).

<aside class="notice">
Accounts with high equity that request tokens will have their requests denied.
</aside>

### Response

Parameter         | Description
------------------| -----------
transfer          | See [Transfers](#get-transfers).

## Get Private Profile
Get private profile data for the user. This is a superset of the `/v3/profile/:publicId` endpoint.

```python
profile_private = client.private.get_profile()
```

```typescript
const profilePrivate: ProfilePrivateResponseObject = await client.private.getProfilePrivate();
```

```json
{
    "username": "foo",
    "ethereumAddress": "0x0913017c740260fea4b2c62828a4008ca8b0d6e4",
    "DYDXHoldings": "250",
    "stakedDYDXHoldings": "250",
    "hedgiesHeld": [111],
    "twitterHandle": "bar",
    "affiliateLinks": [{
        "link": "mrAffiliate",
        "discountRate": "0.95",
    }],
    "affiliateApplicationStatus": "APPROVED",
    "publicId": "ABCDEFGH",
    "tradingLeagues": {
        "currentLeague": "SILVER",
        "currentLeagueRanking": 12,
    },
    "tradingPnls": {
        "absolutePnl30D": "324",
        "percentPnl30D": "25",
        "volume30D": "4000",
    },
    "tradingRewards": {
        "curEpoch": "8",
        "curEpochEstimatedRewards": 280,
        "prevEpochEstimatedRewards": 125,
    },
    "affiliateStatistics": {
        "currentEpoch": {
            "usersReferred": "12",
            "revenue": "12.50",
            "revenueShareRate": "0.24",
        },
        "previousEpochs": {
            "usersReferred": "20",
            "revenue": "1427.30",
        },
        "lastPaidEpoch": "9",
    }
}
```

### HTTP Request
`GET v3/profile/private`

Description: Get private profile data for the user.

### Response

Parameter                 | Description
--------------------------| -----------
username                  | Publically-displayed username.
publicId                  | User's public id used in the public profile endpoint
ethereumAddress           | User's associated ethereum address.
DYDXHoldings              | The user's DYDX token holdings. `null` if not sharing ethereum address.
stakedDYDXHoldings        | The user's stkDYDX token holdings. `null` if not sharing ethereum address.
hedgiesHeld               | Indices of all Hedgies held.
twitterHandle             | The username that appears at the end of a unique Twitter url.
affiliateLinks            | The affiliate links that the user can share and earn revenue on. [] if the user is not an affiliate. See "AffiliateLinkData" below.
affiliateApplicationStatus| The status of the affiliate application, can be `APPROVED`, `PENDING`, `REJECTED`, and `REJECTED_AND_BANNED`. `null` if no affiliate application had been submitted.
tradingLeagues            | See "TradingLeagues" below.
tradingPnls               | See "TradingPnls" below.
tradingRewards            | See "TradingRewards" below.
affiliateStatistics       | See "AffiliateStatistics" below.

### AffiliateLinkData

Parameter           | Description
--------------------| -----------
link                | The affiliate link. Ex: `mrAffiliate` in affiliate link `trade.dydx.exchange/r/mrAffiliate`.
discountRate        | The discount rate used to calculate the referred user's fee. Ex: `0.95` would mean that users get a 5% discount to their fees.

### TradingLeagues

Parameter           | Description
--------------------| -----------
currentLeague       | `null, "BRONZE", "SILVER", "GOLD", "PLATINUM", or "DIAMOND"`.
currentLeagueRanking| `null`, or positive integer ranking.

### TradingPnls

Parameter           | Description
--------------------| -----------
absolutePnl30D      | `null`, or user's 30 day absolute pnl (based on leaderboard formula).
percentPnl30D       | `null`, or user's 30 day percent pnl (based on leaderboard formula).
volume30D           | The sum of a user's 30 day maker and taker trading volume.

### TradingRewards

Parameter                | Description
-------------------------| -----------
curEpoch                 | Current epoch number.
curEpochEstimatedRewards | The user's estimated number of dYdX tokens as rewards for the current epoch.
prevEpochEstimatedRewards| The user's estimated number of dYdX tokens as rewards for the previous epoch.

### AffiliateStatistics

Parameter                | Description
-------------------------| -----------
currentEpoch             | See "CurrentEpochAffiliateStatistics" below.
previousEpochs           | See "PreviousEpochAffiliateStatistics" below.
lastEpochPaid            | The last epoch that has been paid out to affiliates.

### CurrentEpochAffiliateStatistics

Parameter                | Description
-------------------------| -----------
usersReferred            | Total number of users referred by this affiliate in this epoch.
revenue                  | Expected current affiliate payout in this epoch.
revenueShareRate         | Current revenue share rate for the user depending on their $stkDYDX and if manual override is enabled for the user. Will be a number between 0 and 1 inclusive, 0.1 would indicate that the affiliate will receive 10% of all net revenue generated by their referred users.

### PreviousEpochsAffiliateStatistics

Parameter                | Description
-------------------------| -----------
usersReferred            | Total number of users referred by this affiliate in all previous epochs.
revenue                  | Total amount of revenue this user has earned in all previous epochs.


# File: v4-documentation/old-docs/slate-docs/source/includes/_public-v3.md

# Public HTTP API

## Get Markets
> Get Markets

```python
markets = client.public.get_markets()
```

```typescript
const markets: { markets: MarketsResponseObject } = await client.public.getMarkets();
```

```json
{
  "markets": {
    "LINK-USD": {
    "market": "LINK-USD",
    "status": "ONLINE",
    "baseAsset": "LINK",
    "quoteAsset": "USD",
    "stepSize": "0.1",
    "tickSize": "0.01",
    "indexPrice": "12",
    "oraclePrice": "101",
    "priceChange24H": "0",
    "nextFundingRate": "0.0000125000",
    "nextFundingAt": "2021-03-01T18:00:00.000Z",
    "minOrderSize": "1",
    "type": "PERPETUAL",
    "initialMarginFraction": "0.10",
    "maintenanceMarginFraction": "0.05",
    "baselinePositionSize": "1000",
    "incrementalPositionSize": "1000",
    "incrementalInitialMarginFraction": "0.2",
    "volume24H": "0",
    "trades24H": "0",
    "openInterest": "0",
    "maxPositionSize": "10000",
    "assetResolution": "10000000",
    "syntheticAssetId": "0x4c494e4b2d37000000000000000000",
  },
  ...
}
```

### HTTP Request
`GET v3/markets`

Description: Get one or all markets as well as metadata about each retrieved market.

### Request

Parameter         | Description
------------------| -----------
market            | (Optional): Specific market to be fetched.

### Response

### Market

Parameter         | Description
------------------| -----------
markets           | Map of market objects. See below for individual market.

Parameter                | Description
-------------------------| -----------
market                   | Symbol of the market.
status                   | Status of the market. Can be one of <code>ONLINE</code>, <code>OFFLINE</code>, <code>POST_ONLY</code> or <code>CANCEL_ONLY</code>.
baseAsset                | Symbol of the base asset. e.g. "BTC".
quoteAsset               | Symbol of the quote asset. e.g. "BTC".
stepSize                 | The minimum step size (in base currency) of trade sizes for the market.
tickSize                 | The Tick size of the market.
indexPrice               | The current [index price](#index-price-sources) of the market.
oraclePrice              | The current oracle price of the market.
priceChange24H           | The absolute price change of the [index price](#index-price-sources) over the past 24 hours.
nextFundingRate          | The predicted next funding rate (as a 1-hour rate). Can be up to 5 seconds delayed.
nextFundingAt            | The timestamp of the next funding update.
minOrderSize             | Minimum order size for the market.
type                     | Type of the market. This will always be <code>PERPETUAL</code> for now.
initialMarginFraction    | The margin fraction needed to open a position.
maintenanceMarginFraction| The margin fraction required to prevent liquidation.
baselinePositionSize|The max position size (in base token) before increasing the initial-margin-fraction.
incrementalPositionSize|The step size (in base token) for increasing the `initialMarginFraction` by (`incrementalInitialMarginFraction` per step).
incrementalInitialMarginFraction|The increase of `initialMarginFraction` for each `incrementalPositionSize` above the `baselinePositionSize` the position is.
maxPositionSize          | The max position size for this market in base token.
volume24H                | The USD volume of the market in the previous 24 hours.
trades24H                | The number of trades in the market in the previous 24 hours.
openInterest             | The open interest in base token.
assetResolution          | The asset resolution is the number of quantums (Starkware units) that fit within one "human-readable" unit of the asset.
syntheticAssetId         | The id of the synthetic asset traded in the market. Only used for cryptographically signing orders.

## Get Orderbook
> Get Orderbook

```python
from dydx3.constants import MARKET_BTC_USD

orderbook = client.public.get_orderbook(
  market=MARKET_BTC_USD,
)
```

```typescript
const orderbook: OrderbookResponseObject = await client.public.getOrderbook(
  Market.BTC_USD,
);
```

```json
{
  "bids": [
    {
      "price": "29000",
      "size": "1"
    },
    ...
  ],
  "asks": [
    {
      "price": "29500",
      "size": "0.499"
    },
    ...
  ]
}
```

### HTTP Request
`GET v3/orderbook/:market`

<aside class="success">
Returns bids and asks which are each Orderbook order arrays (price and size).
</aside>

Description: Returns the active orderbook for a market. All bids and asks that are fillable are returned.

### Request

Parameter         | Description
----------------- | -----------
market            | Market of the Orderbook.

### Response

Parameter         | Description
----------------- | -----------
bids              | See Orderbook Order below. Sorted by price in descending order.
asks              | See Orderbook Order below. Sorted by price in ascending order.

### Orderbook Order

Parameter         | Description
----------------- | -----------
price             | The price of the order (in quote / base currency).
size              | The size of the order (in base currency).

## Get Trades
> Get Trades

```python
from dydx3.constants import MARKET_BTC_USD

all_trades = client.public.get_trades(
  market=MARKET_BTC_USD,
)
```

```typescript
const trades: { trades: Trade[] } = await client.public.getTrades({
  market: Market.BTC_USD,
  startingBeforeOrAt: "2021-01-05T17:33:43.163Z",
  limit: 1,
});
```

```json
{
  "trades": [
    {
      "side": "BUY",
      "size": "0.001",
      "price": "29000",
      "createdAt": "2021-01-05T16:33:43.163Z",
      "liquidation": false
    },
    ...
  ]
}
```

### HTTP Request
`GET v3/trades/:market`

Description: Get Trades by specified parameters. Passing in all query parameters to the HTTP endpoint would look like: `GET v3/trades/BTC-USD?startingBeforeOrAt=2021-09-05T17:33:43.163Z&limit=1`.

<aside class="notice">
Trades will include information for all users and as such includes less information on individual transactions than the fills endpoint.
</aside>

### Request

Parameter         | Description
----------------- | -----------
market            | Market of the trades.
startingBeforeOrAt| (Optional): Set a date by which the trades had to be created.
limit             | (Optional): The number of candles to fetch (Max 100).

### Response

Parameter         | Description
----------------- | -----------
trades            | An array of trades. See trade below

### Trade

Parameter         | Description
----------------- | -----------
side              | Either <code>BUY</code> or <code>SELL</sell>.
size              | The size of the trade.
price             | The price of the trade.
createdAt         | The time of the trade.
liquidation       | <code>true</code> if the trade was the result of a liquidation. <code>false</code> otherwise.

## Get Fast Withdrawal Liquidity
> Get Fast Withdrawal Liquidity

```python
fast_withdrawals_info = client.public.get_fast_withdrawal()
```

```typescript
const availableFundsMap: {
  liquidityProviders: {
    [positionId: string]: {
      availableFunds: string,
      starkKey: string,
      quote: {
        creditAsset: string,
        creditAmount: string,
        debitAmount: string,
      } | null,
    }
  }
} = await client.public.getFastWithdrawalAvailableFunds();
```

```json
{
  "liquidityProviders": {
    "1812": {
      "availableFunds": "1000",
      "starkKey": "180913017c740260fea4b2c62828a4008ca8b0d6e4",
      "quote": null,
    },
  }
}
```

### HTTP Request
`GET v3/fast-withdrawals`

Description: Returns a map of all LP provider accounts that have available funds for fast withdrawals. Given a `debitAmount` and asset the user wants sent to L1, this endpoint also returns amount of the desired asset the user will be credited on L1. Given a `creditAmount` and asset the user wants sent to L1, this endpoint also returns the amount the user will be debited on L2.

### Request

Parameter    | Description
-------------| -----------
creditAsset	 | (Optional): The asset that would be sent to the user. Required if creditAmount or debitAmount are set.
creditAmount | (Optional): Set this value if the user wants a quote based on the creditAmount.
debitAmount  | (Optional): Set this value if the user wants a quote based on the debitAmount.

<aside class="warning">
Both debitAmount and creditAmount cannot be provided in the same request.
</aside>

### Response

Parameter          | Description
-------------------| -----------
liquidityProviders | Map of LP position IDs to [Liquidity Provider](#liquidity-provider).

### Liquidity Provider

Field          | Description
---------------| -----------
availableFunds | The funds available for the LP.
starkKey       | The public stark key for the LP.
quote          | The [Liquidity Provider Quote](#liquidity-provider-quote) given the user's request. Null if no request from the user or the request is unfillable by this LP.

### Liquidity Provider Quote

Field        | Description
-------------| -----------
creditAsset	 | The asset that would be sent to the user on L1.
creditAmount | The amount of creditAsset that would be sent to the user (human readable).
debitAmount  | The amount of USD that would be deducted from the users L2 account (human readable).


## Get Market Stats
> Get Market Stats

```python
from dydx3.constants import MARKET_BTC_USD

market_statistics = client.public.get_stats(
  market=MARKET_BTC_USD,
  days=MARKET_STATISTIC_DAY_SEVEN,
)
```

```typescript
const marketStatistics = await client.public.getStats({
  market: Market.BTC_USD,
  days: MarketStatisticDay.SEVEN,
});
```

```json
{
  "markets": {
    "ETH-USD": {
      "market": "ETH-USD",
      "open": "1100",
      "close": "1100",
      "high": "1100",
      "low": "1095",
      "baseVolume": "10000",
      "quoteVolume": "100000",
      "type": "PERPETUAL",
      "fees": "1000"
    }
  }
}
```

### HTTP Request
`GET v3/stats/:market`

Description: Get an individual market's statistics over a set period of time or all available periods of time.

### Request

Parameter         | Description
------------------| -----------
market            | Market whose statistics are being fetched.
days              | (Optional): Specified day range for the statistics to have been compiled over. Can be one of `1`, `7`, `30`. Defaults to `1`.

### Response

Parameter         | Description
------------------| -----------
markets           | Map of market to MarketStats. See example below.

### MarketStats

Parameter         | Description
------------------| -----------
market            | The symbol of the market, e.g. ETH-USD.
open              | The open price of the market.
high              | The high price of the market.
low               | The low price of the market.
close             | The close price of the market.
baseVolume        | The total amount of base asset traded.
quoteVolume       | The total amount of quote asset traded.
type              | Type of the market. This will always be <code>PERPETUAL</code> for now.

## Get Historical Funding
> Get Historical Funding

```python
from dydx3.constants import MARKET_BTC_USD

historical_funding = client.public.get_historical_funding(
  market=MARKET_BTC_USD,
)
```

```typescript
const historicalFunding = await client.public.getHistoricalFunding({
  market: Market.BTC_USD,
});
```

```json
{
  "historicalFunding": [
    {
      "market": "BTC-USD",
      "rate": "0.0000125000",
      "price": "31297.5000008009374142",
      "effectiveAt": "2021-01-05T09:10:49.000Z"
    },
    ...
  ]
}
```

### HTTP Request
`GET v3/historical-funding/:market`

Description: Get the historical funding rates for a market.

### Request

Parameter          | Description
-------------------| -----------
market             | Market whose historical funding rates are being fetched.
effectiveBeforeOrAt| (Optional): Set a date by which the historical funding rates had to be created.

### Response

Parameter          | Description
-------------------| -----------
historicalFunding  | Array of HistoricalFunding. See below for individual example.

### Historical Funding

Parameter          | Description
-------------------| -----------
market             | Market for which to query historical funding.
rate               | The funding rate (as a 1-hour rate).
price              | Oracle price used to calculate the funding rate.
effectiveAt        | Time at which funding payments were exchanged at this rate.

## Get Candles for Market
> Get Candles for Market

```python
from dydx3.constants import MARKET_BTC_USD

candles = client.public.get_candles(
  market=MARKET_BTC_USD,
  resolution='1DAY',
)
```

```typescript
const candles: {
  candles: CandleResponseObject,
} = await client.public.getCandles({
  market: Market.BTC_USD,
  resolution: CandleResolution.1DAY,
})
```

```json
  "candles": [
    {
      "startedAt": "2021-01-05T00:00:00.000Z",
      "updatedAt": "2021-01-05T00:00:00.000Z",
      "market": "BTC-USD",
      "resolution": "1DAY",
      "low": "40000",
      "high": "45000",
      "open": "45000",
      "close": "40000",
      "baseTokenVolume": "1.002",
      "trades": "3",
      "usdVolume": "45085",
      "startingOpenInterest": "28"
    },
    ...
  ]
```

### HTTP Request
`GET v3/candles/:market`

Description: Get the candle statistics for a market.

### Request

Parameter          | Description
-------------------| -----------
market             | Market whose candles are being fetched.
resolution         | (Optional): Specific candle resolution being fetched. Can be one of <code>1DAY</code>, <code>4HOURS</code>, <code>1HOUR</code>, <code>30MINS</code>, <code>15MINS</code>, <code>5MINS</code>, <code>1MIN</code>.
fromISO            | (Optional): Starting point for the candles.
toISO              | (Optional): Ending point for the candles.
limit              | (Optional): The number of candles to fetch (Max 100).

### Response

Parameter            | Description
---------------------| -----------
startedAt            | When the candle started, time of first trade in candle.
updatedAt            | When the candle was last updated
market               | Market the candle is for.
resolution           | Time-period of candle (currently 1HOUR or 1DAY).
low                  | Low trade price of the candle.
high                 | High trade price of the candle.
open                 | Open trade price of the candle.
close                | Close trade price of the candle.
baseTokenVolume      | Volume of trade in baseToken currency for the candle.
trades               | Count of trades during the candle.
usdVolume            | Volume of trade in USD for the candle.
startingOpenInterest | The open interest in baseToken at the start of the candle.

## Get Global Configuration Variables

```python
config = client.public.get_config()
```

```typescript
const config: ConfigResponseObject = await client.public.getConfig();
```

```json
  {
    "collateralAssetId": "0x02c04d8b650f44092278a7cb1e1028c82025dff622db96c934b611b84cc8de5a",
    "collateralTokenAddress": "0x8707a5bf4c2842d46b31a405ba41b858c0f876c4",
    "defaultMakerFee": "0.0005",
    "defaultTakerFee": "0.001",
    "exchangeAddress": "0x014F738EAd8Ec6C50BCD456a971F8B84Cd693BBe",
    "maxExpectedBatchLengthMinutes": "240",
    "maxFastWithdrawalAmount": "200000",
    "cancelOrderRateLimiting": {
      "maxPointsMulti": 3,
      "maxPointsSingle": 8500,
      "windowSecMulti": 10,
      "windowSecSingle": 10
    },
    "placeOrderRateLimiting": {
      "maxPoints": 1750,
      "windowSec": 10,
      "targetNotional": 40000,
      "minLimitConsumption": 4,
      "minMarketConsumption": 20,
      "minTriggerableConsumption": 100,
      "maxOrderConsumption": 100
    }
  }
```

### HTTP Request
`GET v3/config`

Description: Get any global configuration variables for the exchange as a whole.

### Response

Parameter                     | Description
----------------------------- | -----------
collateralAssetId             | The assetId of the collateral asset in the Starkware system.
collateralTokenAddress        | The address of the token used as collateral.
defaultMakerFee               | The default maker fee for new accounts.
defaultTakerFee               | The default taker fee for new accounts.
exchangeAddress               | The address of the exchange contract.
maxExpectedBatchLengthMinutes | The maximum expected time between batches L2 (in minutes).
maxFastWithdrawalAmount       | The maximum amount (in USDC) allowed for fast withdrawals.
cancelOrderRateLimiting       | See `cancelOrderRateLimiting` below.
placeOrderRateLimiting        | See `placeOrderRateLimiting` below.

### cancelOrderRateLimiting

Parameter                     | Description
----------------------------- | -----------
maxPointsMulti                | The number of rate limiting points given per window for canceling multiple orders.
maxPointsSingle               | The number of rate limiting points given per window for canceling single orders.
windowSecMulti                | The length of a rate limiting window for canceling multiple orders, in seconds.
windowSecSingle               | The length of a rate limiting window for canceling single orders, in seconds.

### placeOrderRateLimiting

Parameter                     | Description
----------------------------- | -----------
maxPoints                     | The number of rate limiting points given per window.
windowSec                     | The length of a rate limiting window, in seconds.
targetNotional                | The `(size * price)` target used for determining points consumption.
minLimitConsumption           | The minimum number of points used when placing a limit order.
minMarketConsumption          | The minimum number of points used when placing a market order.
minTriggerableConsumption     | The minimum number of points used when placing a triggerable (e.g. stop-loss) order.
maxOrderConsumption           | The maximum number of points used when placing an order.

## Check If User Exists
> Check If User Exists

```python
user_exists = client.public.check_if_user_exists(
  ethereum_address='foo',
)
```

```typescript
const userExists: { exists: boolean } = await client.public.doesUserExistWithAddress(
  'foo',
);
```

```json
{
  "exists": true
}
```

### HTTP Request
`GET v3/users/exists`

Description: Check if a user exists for a given Ethereum address.

### Request

Parameter      | Description
-------------- | -----------
ethereumAddress| Ethereum address that the user would be associated with.

### Response

Parameter      | Description
-------------- | -----------
exists         | If a user exists for the given Ethereum address.

## Check If Username Exists
> Check If Username Exists

```python
username_exists = client.public.check_if_username_exists(
  username='username',
)
```

```typescript
const usernameExists: { exists: boolean } = await client.public.doesUserExistWithUsername(
  'username',
);
```

```json
{
  "exists": true
}
```

### HTTP Request
`GET v3/usernames`

Description: Check if a username has been taken by a user.

### Request

Parameter  | Description
---------- | -----------
username   | Unique username being checked.

### Response

Parameter      | Description
-------------- | -----------
exists         | If a username has been taken by any user.

## Get API Server Time
> Get API Server Time

```python
time_object = client.public.get_time()
```

```typescript
const time: { time: { iso: string, epoch: number } } = await client.public.getTime();
```

```json
{
  "iso": "2021-02-02T18:35:45Z",
  "epoch": "1611965998.515",
}
```

### HTTP Request
`GET v3/time`

Description: Get the current time of the API server.

### Response

Parameter      | Description
-------------- | -----------
iso            | ISO time of the server in UTC.
epoch          | Epoch time in seconds with milliseconds.

## Get Public Leaderboard PNLs
> Get Public Leaderboard PNLs

```typescript
const leaderboardPnls: { pnls: LeaderboardPnlResponseObject } = await client.public.getLeaderboardPnls(
  period=LeaderboardPnlPeriod.WEEKLY,
  sortBy=LeaderboardPnlSortBy.ABSOLUTE,
  limit=10,
);
```

```json
{
  "prizePool": 50000,
  "numHedgiesWinners": 1,
  "numPrizeWinners": 50,
  "ratioPromoted": 0.25,
  "ratioDemoted": 0.5,
  "minimumEquity": 500,
  "minimumDYDXTokens": 0,
  "seasonNumber": 16,
  "topPnls": [
    {
      "username": "user",
      "ethereumAddress": "0x3408105669f73e814be44cbf598679a50eb2f7ed",
      "publicId": "ABCDEFG",
      "absolutePnl": "10206.971314",
      "percentPnl": "0.409100",
      "absoluteRank": 20,
      "percentRank": 1,
      "seasonExpectedOutcome": "SAME_LEAGUE",
      "hedgieWon": null,
      "prizeWon": null
    },
    ...
  ],
    "numParticipants": 1,
    "updatedAt": "2022-02-02T15:31:10.813Z",
    "startedAt": "2022-02-01T15:30:00.000Z",
    "endsAt": "2022-02-02T15:30:00.000Z"
}
```

### HTTP Request
`GET v3/leaderboard-pnl`

<aside class="warning">
Only available for the typescript client and http requests
</aside>

Description: Get the top PNLs for a specified period and how they rank against each other.

### Request

Parameter          | Description
------------------ | -----------
period             | "DAILY", "WEEKLY", "MONTHLY", "ALLTIME", "COMPETITION", "DAILY_COMPETITION", or "LEAGUES".
startingBeforeOrAt | Latest the leaderboard starts at.
sortBy             | Which PNL to sort ranks by. "ABSOLUTE" or "PERCENT".
limit              | (Optional): The number of leaderboard PNLs to fetch (Max 100).

### Response

Parameter         | Description
----------------- | -----------
topPnls           | Array of PNLForPeriod (see below).
numParticipants   | Number of participants in this leaderboard. Includes ranked and unranked participants.
startedAt         | Starting time for this pnl. Note: will only be set if being used for a competition or leagues. Otherwise, this value will always be `null`.
endsAt            | Ending time for this pnl. Note: will only be set if being used for a competition or leagues. Otherwise, this value will always be `null`. (Can be a future time.)
updatedAt         | The time this pnl was updated.
seasonNumber      | Trading leagues season number. Starts at 1. `null` if not leagues.
prizePool         | Prize pool size for period. `null` if not "COMPETITION" or leagues.
numHedgiesWinners | Number of hedgies winners for league. `null` if not a leagues period.
numPrizeWinners   | Number of prize winners for league. `null` if not a leagues period.
ratioPromoted     | Ratio of users promoted for league. `null` if not a leagues period.
ratioDemoted      | Ratio of users demoted for league. `null` if not a leagues period.
minimumEquity     | Minimum account equity required to join league. `null` if not a leagues period.
minimumDYDXTokens | Minimum user DYDX + stkDYDX Token balance required to join league. `null` if not a leagues period.
numHedgiesWinners | Number of hedgies prizes for period. `null` if not leagues.

#### PNLForPeriod

Parameter             | Description
--------------------- | -----------
username              | Publically-displayed username. `null` if not sharing.
ethereumAddress       | User's associated ethereum address. `null` if not sharing.
publicId              | User's public id used in the public profile endpoint.
absolutePnl           | The PNL (in USD) for the specified period. Sorted DESC for "ABSOLUTE" sortBy.
percentPnl            | The percent PNL for the specified period. Sorted DESC for "PERCENT" sortBy.
absoluteRank          | User's absolute PNL rank.
percentRank           | User's percent PNL rank.
seasonExpectedOutcome | User's expected outcome of latest season. "PROMOTION", "DEMOTION", or "SAME_LEAGUE". `null` if not leagues.

## Get Public Retroactive Mining Rewards
> Get Public Retroactive Mining Rewards

```python
rewards = client.public.get_public_retroactive_mining_rewards(
  ethereum_address='foo',
)
```

```typescript
const rewards: PublicRetroactiveMiningRewardsResponseObject = await client.public.getPublicRetroactiveMiningRewards(
  'foo'
);
```

```json
{
  "allocation": "0",
  "targetVolume": "0"
}
```

### HTTP Request
`GET v3/rewards/public-retroactive-mining`

Description: Get the retroactive mining rewards for an ethereum address.

### Request

Parameter       | Description
--------------- | -----------
ethereumAddress | An Ethereum address.

### Response

Parameter          | Description
------------------ | -----------
allocation         | The number of allocated dYdX tokens for the address.
targetVolume       | The addresses' required trade volume (in USD) to be able to claim the allocation.

## Verify an Email Address
> Verify an Email Address

```python
client.public.verify_email(
  token='token',
)
```

```typescript
await client.public.verifyEmail('token');
```

```json
{}
```

### HTTP Request
`PUT v3/emails/verify-email`

Description: Verify an email address by providing the verification token sent to the email address.

### Request

Parameter       | Description
--------------- | -----------
token           | Confirmation token that was sent to a user's email.

### Response

On success, returns a `204` response with an empty body. After receiving a `204`, the user associated with the email the token was sent to will begin getting notification emails for all types [they have specified in their userData](#send-verification-email). Responds with a `400` error if the token is invalid.

## Get Currently Revealed Hedgies
> Get Currently Revealed Hedgies

```typescript
const currentlyRevealedHedgies: {
    daily?: HedgiePeriodResponseObject,
    weekly?: HedgiePeriodResponseObject,
} = await client.public.getCurrentlyRevealedHedgies();
```

```json
{
  "daily": {
    "blockNumber": 14135506,
    "competitionPeriod": 1,
    "tokenIds": [4100]
  },
  "weekly": {
    "blockNumber": 14135506,
    "competitionperiod": 0,
    "tokenIds": [2790, 3000, 4109]
  }
}
```

### HTTP Request
`GET v3/hedgies/current`

<aside class="warning">
Only available for the typescript client and http requests.
</aside>

Description: Get the currently revealed [Hedgies](https://hedgies.wtf/) for competition distribution.

### Response

Parameter          | Description
------------------ | -----------
daily              | NftPeriodInformation for daily Hedgie or undefined.
weekly             | NftPeriodInformation for weekly Hedgies or undefined.

### NftPeriodInformation

Parameter          | Description
------------------ | -----------
blockNumber        | The number of the block whose hash was used to randomly select the Hedgie tokenId from the remaining unrevealed Hedgies (or currently revealed Hedgies in the case of distributing weekly Hedgies).
competitionPeriod  | The zero-indexed period of the competition. Competition 0 was the very first day a Hedgie was revealed for competition winners.
tokenIds           | An array of the numeric tokenIds of the Hedgies.

## Get Historically Revealed Hedgies
> Get Historically Revealed Hedgies

```typescript
const historicallyRevealedHedgies: {
  historicalTokenIds: HedgiePeriodResponseObject[],
} = await client.public.getHistoricallyRevealedHedgies({
    nftRevealType: WEEK,
    start: 1,
  });
```

```json
{
  "historicalTokenIds": [{
    "blockNumber": 14135506,
    "competitionperiod": 0,
    "tokenIds": [2790, 3000, 4109]
  }]
}
```

### HTTP Request
`GET v3/hedgies/history`

<aside class="warning">
Only available for the typescript client and http requests.
</aside>

Description: Get the historically revealed [Hedgies](https://hedgies.wtf/) from competition distributions.

### Request

Parameter       | Description
--------------- | -----------
nftRevealType   | The competition type the Hedgies are being revealed for (`Day` or `Week`).
start           | (Optional): Oldest competition period to be looking from (inclusive).
end             | (Optional): Newest competition period to be looking up to (inclusive).

### Response

Parameter          | Description
------------------ | -----------
historicalTokenIds | [NftPeriodInformation](#get-currently-revealed-hedgies) array.

<aside class="warning">
Rows are returned from newest to oldest row. If start and end are not included, return most recent 100 rows. If only one of startingFrom or endingAt is present, get startingFrom and the 99 rows after or the 99 before and endingAt (both ordered newest row to oldest). If start and end are both present then window must be no greater than 100 inclusive or a 400 error will be returned. Also, competition periods are zero-indexed.
</aside>

## Get Insurance Fund Balance
> Get Insurance Fund Balance

```python
balance = client.public.get_insurance_fund_balance()
```

```typescript
const balance: { balance: number } = await client.public.getInsuranceFundBalance();
```

```json
{
  "balance":"9868319.469028"
}
```

### HTTP Request
`GET v3/insurance-fund/balance`

Description: Get the balance of the [dYdX insurance fund](https://help.dydx.exchange/en/articles/4797358-contract-loss-mechanisms).

### Response

Parameter          | Description
------------------ | -----------
balance            | Balance of the dYdX insurance fund in USD.

## Get Public Profile
Get Public Profile data. This is a subset of the `v3/profile/private` endpoint.

```python
balance = client.public.get_profile("publicId")
```

```typescript
const publicProfile: ProfilePublicResponseObject = await client.public.getProfilePublic("publicId");
```

```json
{
    "username": "foo",
    "ethereumAddress": "0x0913017c740260fea4b2c62828a4008ca8b0d6e4",
    "DYDXHoldings": "250",
    "stakedDYDXHoldings": "250",
    "hedgiesHeld": [111],
    "twitterHandle": "bar",
    "tradingLeagues": {
        "currentLeague": "SILVER",
        "currentLeagueRanking": 12,
    },
    "tradingPnls": {
        "absolutePnl30D": "324",
        "percentPnl30D": "25",
        "volume30D": "4000",
    },
    "tradingRewards": {
        "curEpoch": "8",
        "curEpochEstimatedRewards": 280,
        "prevEpochEstimatedRewards": 125,
    },
}
```

### HTTP Request
`GET v3/profile/:publicId`

Description: Get the public profile of a user given their public id.

### Response

Parameter          | Description
------------------ | -----------
balance            | Balance of the dYdX insurance fund in USD.

### Request

Parameter          | Description
-------------------| -----------
publicId           | Public id of the user

### Response
Parameter           | Description
--------------------| -----------
username            | Publically-displayed username.
publicId            | User's public id used in the public profile endpoint
ethereumAddress     | User's associated ethereum address.
DYDXHoldings        | The user's DYDX token holdings. `null` if not sharing ethereum address.
stakedDYDXHoldings  | The user's stkDYDX token holdings. `null` if not sharing ethereum address.
hedgiesHeld         | Indices of all Hedgies held.
twitterHandle       | The username that appears at the end of a unique Twitter url.
tradingLeagues      | See "TradingLeagues" below.
tradingPnls         | See "TradingPnls" below.
tradingRewards      | See "TradingRewards" below.

### TradingLeagues
Parameter           | Description
--------------------| -----------
currentLeague       | `null, "BRONZE", "SILVER", "GOLD", "PLATINUM", or "DIAMOND"`.
currentLeagueRanking| `null`, or positive integer ranking.

### TradingPnls
Parameter           | Description
--------------------| -----------
absolutePnl30D      | `null`, or user's 30 day absolute pnl (based on leaderboard formula).
percentPnl30D       | `null`, or user's 30 day percent pnl (based on leaderboard formula).
volume30D           | The sum of a user's 30 day maker and taker trading volume.

### TradingRewards
Parameter                | Description
-------------------------| -----------
curEpoch                 | Current epoch number.
curEpochEstimatedRewards | The user's estimated number of dYdX tokens as rewards for the current epoch.
prevEpochEstimatedRewards| The user's estimated number of dYdX tokens as rewards for the previous epoch.


# File: v4-documentation/old-docs/slate-docs/source/includes/_security-v3.md

# Security

## Independent Audits

The Starkware Perpetual smart contracts were audited independently by
[PeckShield](https://peckshield.com).

**[PeckShield Audit Report](https://github.com/starkware-libs/starkex-contracts/blob/master/audit/StarkPerpetual_v1.0_Audit_Report.pdf)**

## Vulnerability Disclosure Policy

The disclosure of security vulnerabilities helps us ensure the security of our users.

**How to report a security vulnerability?**

If you believe you’ve found a security vulnerability in one of our contracts or platforms,
send it to us by emailing [security@dydx.exchange](mailto:security@dydx.exchange).
Please include the following details with your report:

* A description of the location and potential impact of the vulnerability.

* A detailed description of the steps required to reproduce the vulnerability.

**Scope**

Any vulnerability not previously disclosed by us or our independent auditors in their reports.

**Guidelines**

We require that all reporters:

* Make every effort to avoid privacy violations, degradation of user experience,
disruption to production systems, and destruction of data during security testing.

* Use the identified communication channels to report vulnerability information to us.

* Keep information about any vulnerabilities you’ve discovered confidential between yourself and
dYdX until we’ve had 30 days to resolve the issue.

If you follow these guidelines when reporting an issue to us, we commit to:

* Not pursue or support any legal action related to your findings.

* Work with you to understand and resolve the issue quickly
(including an initial confirmation of your report within 72 hours of submission).

* Grant a monetary reward based on the [OWASP risk assessment methodology](https://medium.com/dydxderivatives/announcing-bug-bounties-for-the-dydx-margin-trading-protocol-d0c817d1cda4).


# File: v4-documentation/old-docs/slate-docs/source/includes/_websocket-v3.md

# V3 Websocket API

dYdX offers a WebSocket API for streaming v3 updates.

You can connect to the v3 WebSockets at:

* **Production**: `wss://api.dydx.exchange/v3/ws`
* **Staging (Goerli)**: `wss://api.stage.dydx.exchange/v3/ws`

The server will send pings every 30s and expects a pong within 10s. The server does not expect pings, but will respond with a pong if sent one.

## Accounts channel

This channel provides realtime information about orders, fills, funding updates and positions for a user. To subscribe, you will need to
be authenticated.

To subscribe:

| field         | type   | description                                      |
|---------------|--------|--------------------------------------------------|
| type          | string | Set to <code>subscribe</code>                    |
| channel       | string | Set to <code>v3_accounts</code>                  |
| accountNumber | string | The account number to subscribe to               |
| apiKey        | string | The apiKey for the user                          |
| signature     | string | validation signature. See below                  |
| timestamp     | string | timestamp used for the signature                 |
| passphrase    | string | The <code>passphrase</code> field of the API key |

**Authentication**

The authentication in the accounts channel is identical to [private endpoint authentication](#authentication) with one key difference. The `requestPath` is `/ws/accounts`.

### Initial Response:

The initial response will contain the information about the account, open positions, recent transfers, and open orders, i.e. everything from GET `/v3/accounts/:id`, GET `/v3/transfers`, GET `/v3/funding` and GET `/v3/orders` (with `accountId` in the header).

Note that the `freeCollateral` and `equity` (also called `total account value`) for an account are only sent in the initial response. To track these over time, refer to [this section](#margin).

> Example initial response

```json
{
  "type": "subscribed",
  "channel": "v3_accounts",
  "connection_id": "e2a6c717-6f77-4c1c-ac22-72ce2b7ed77d",
  "id": "e33a8007-57ca-52ab-887d-d162d1666f3b",
  "message_id": 1,
  "contents": {
    "orders": [
      {
        "id": "797fc129eeb7c54163f3947f1f250594",
        "clientId": "2",
        "market": "BTC-USD",
        "accountId": "e33a8007-57ca-52ab-887d-d162d1666f3b",
        "side": "BUY",
        "size": "112",
        "remainingSize": "0",
        "price": "34",
        "limitFee": "0.0005",
        "type": "LIMIT",
        "status": "OPEN",
        "signature": "0x456...",
        "timeInForce": "FOK",
        "postOnly": "false",
        "expiresAt": "2021-09-22T20:22:26.399Z",
        "createdAt": "2020-09-22T20:22:26.399Z"
      }
    ],
    "account": {
      "id": "e33a8007-57ca-52ab-887d-d162d1666f3b",
      "positionId": "9356",
      "userId": "fe71e7df-c633-4ba1-870e-61f36580cfc5",
      "accountNumber": "0",
      "starkKey": "041c2ae647ee91807eed6471488983ab4addc2a602d4ceeb04dfda470e33f148",
      "quoteBalance": "300",
      "pendingDeposits": "0",
      "pendingWithdrawals": "0",
      "lastTransactionId": "14",
      "equity": "1879.090000",
      "freeCollateral": "1879.090000",
      "createdAt": "2021-04-09T21:08:34.984Z",
      "openPositions": {
        "LINK-USD": {
          "id": "677dad3b-d848-5e7c-84bf-18760f3414f6",
          "accountId": "e33a8007-57ca-52ab-887d-d162d1666f3b",
          "market": "LINK-USD",
          "side": "LONG",
          "status": "OPEN",
          "size": "200",
          "maxSize": "300",
          "entryPrice": "36",
          "exitPrice": "38",
          "realizedPnl": "50",
          "createdAt": "2020-09-22T20:25:26.399Z",
          "openTransactionId": "2",
          "lastTransactionId": "14",
          "sumOpen": "300",
          "sumClose": "100"
        }
      }
    }
  },
  "transfers": [
    {
      "id": "8d303634-da14-56bb-99f5-122e34b1ce34",
      "type": "FAST_WITHDRAWAL",
      "debitAsset": "USDC",
      "creditAsset": "USDC",
      "debitAmount": "500",
      "creditAmount": "500",
      "transactionHash": "0xb86e98d05098de6249d7c10616ffefa0b001976238083dc34a8e747fd7960029",
      "status": "CONFIRMED",
      "createdAt": "2021-02-05T00:37:43.009Z",
      "confirmedAt": null,
      "clientId": "9407156494718159",
      "fromAddress": "0x3ebe6781be6d436cb7999cfce8b52e40819721cb",
      "toAddress": "0x14c2a496e5b7a52d54748cba0bd9f4b24ed27fdd"
    }
  ],
  "fundingPayments": [],
}
```

### Channel Data

Subsequent responses will contain any updates to open orders, or changes to account balance, or the open positions, or transfers, in a single message.

> A fill occurs, and a position is closed, and the account balance modified

```json
{
  "type": "channel_data",
  "channel": "v3_accounts",
  "connection_id": "e2a6c717-6f77-4c1c-ac22-72ce2b7ed77d",
  "id": "e33a8007-57ca-52ab-887d-d162d1666f3b",
  "message_id": 2,
  "contents": {
    "fills": [{
        "id": "677dad3b-d848-5e7c-84bf-18760f3414f6",
        "accountId": "e33a8007-57ca-52ab-887d-d162d1666f3b",
        "side": "BUY",
        "liquidity": "TAKER",
        "market": "LINK-USD",
        "orderId": "797fc129eeb7c54163f3947f1f250594",
        "size": "112",
        "price": "35",
        "fee": "10",
        "transactionId": "1",
        "orderClientId": "31391968951033844",
        "createdAt": "2020-09-22T20:25:26.399Z",
    }],
    "orders": [{
      "id": "797fc129eeb7c54163f3947f1f250594",
      "clientId": "2",
      "market": "BTC-USD",
      "accountId": "e33a8007-57ca-52ab-887d-d162d1666f3b",
      "side": "BUY",
      "size": "112",
      "remainingSize": "0",
      "price": "34",
      "limitFee": "0.0005",
      "type": "LIMIT",
      "status": "ENTIRELY_FILLED",
      "signature": "0x456...",
      "timeInForce": "FOK",
      "postOnly": "false",
      "expiresAt": "2021-09-22T20:22:26.399Z",
      "createdAt": "2020-09-22T20:22:26.399Z"
    }],
    "positions": [{
      "id": "677dad3b-d848-5e7c-84bf-18760f3414f6",
      "accountId": "e33a8007-57ca-52ab-887d-d162d1666f3b",
      "market": "LINK-USD",
      "side": "LONG",
      "status": "CLOSED",
      "size": "200",
      "maxSize": "300",
      "entryPrice": "36",
      "exitPrice": "38",
      "realizedPnl": "50",
      "createdAt": "2020-09-22T20:25:26.399Z",
      "openTransactionId": "2",
      "closeTransactionId": "23",
      "lastTransactionId": "23",
      "closedAt": "2020-14-22T20:25:26.399Z",
      "sumOpen": "300",
      "sumClose": "100"
    }],
    "accounts": [{
      "id": "e33a8007-57ca-52ab-887d-d162d1666f3b",
      "positionId": "b2759094-12af-4b59-8071-661e99148a14",
      "userId": "fe71e7df-c633-4ba1-870e-61f36580cfc5",
      "accountNumber": "0",
      "starkKey": "0x456...",
      "quoteBalance": "700",
      "pendingDeposits": "400",
      "pendingWithdrawals": "0",
      "lastTransactionId": "14"
    }]
  }
}
```

> a deposit occurs

```json
{
  "type": "channel_data",
  "channel": "v3_accounts",
  "connection_id": "e2a6c717-6f77-4c1c-ac22-72ce2b7ed77d",
  "id": "e33a8007-57ca-52ab-887d-d162d1666f3b",
  "message_id": 2,
  "contents": {
    "fills": [],
    "orders": [],
    "positions": [],
    "accounts": [{
      "id": "e33a8007-57ca-52ab-887d-d162d1666f3b",
      "positionId": "b2759094-12af-4b59-8071-661e99148a14",
      "userId": "fe71e7df-c633-4ba1-870e-61f36580cfc5",
      "accountNumber": "0",
      "starkKey": "0x456...",
      "quoteBalance": "7000",
      "pendingDeposits": "200",
      "pendingWithdrawals": "0",
      "lastTransactionId": "14"
    }],
    "transfers": [{
      "id" : "35bb84a8-d8b5-5f8e-a49e-8ad979fb7567",
      "accountId" : "e33a8007-57ca-52ab-887d-d162d1666f3b",
      "type" : "DEPOSIT",
      "debitAsset" : "USDC",
      "creditAsset" : "USDC",
      "debitAmount" : "10000",
      "creditAmount" : "10000",
      "transactionHash" : "0xec2bd16e73e4bb54c1ee25415233ded15f6e8c4edb8480ce9774a28c7846d4f0",
      "status" : "PENDING",
      "clientId" : "18",
      "updatedAt" : "2021-01-17 22:24:54.661+00",
      "createdAt" :  "2021-01-17 22:24:54.560426+00",
    }]
  }
}
```

## Orderbook

To subscribe:

| field                     | type    | description                                                                     |
|---------------------------|---------|---------------------------------------------------------------------------------|
| type                      | string  | Set to <code>subscribe</code>                                                   |
| channel                   | string  | Set to <code>v3_orderbook</code>                                                |
| id                        | string  | The market to subscribe to e.g. BTC-USD, LINK-USD                               |
| includeOffsets (optional) | boolean | If specified, this will return an initial response with per-price level offsets |

### Initial Response:

The initial response will contain the state of the orderbook and will be the same structure as GET `/v3/orderbook/:market`. If <code>includeOffsets</code> is sent and set to true in the subscription message, there will be an offset included for each price level. (See the example included)

| field    | description                                      |
|----------|--------------------------------------------------|
| type     | will be <code>subscribed</code>                  |
| channel  | the channel name, i.e. <code>v3_orderbook</code> |
| id       | the market subscribed to e.g. BTC-USD            |
| contents | the message contents                             |

The contents is structured as:

| field  | type               | description                                                             |
|--------|--------------------|-------------------------------------------------------------------------|
| offset | string             | A number used for ordering. See <code>offset</code> below.              |
| bids   | array<PublicOrder> | See <code>PublicOrder</code> below. Sorted by price in descending order |
| asks   | array<PublicOrder> | See <code>PublicOrder</code> below. Sorted by price in ascending order  |

PublicOrder:

| field  | type   | description                                                                       |
|--------|--------|-----------------------------------------------------------------------------------|
| price  | string | human readable price of the order (in quote / base currency)                      |
| size   | string | human readable size of the order (in base currency)                               |
| offset | string | (if <code>includeOffsets</code> is set to true) the offset for the specific price |


Offset:

The price updates are not guaranteed to be sent in order. So it is possible to receive an older price update later. For this reason, the offset is included in the message, to help order. The offset increases monotonically, and increasing values of offsets indicate more recent values.

<aside>
To keep a valid orderbook, you should store the offset for each price level independently. A given price level should be updated if and only if an update for the price level is received with a higher offset than what you have stored.

To get a per-price level offset in the initial response, you can set <code>includeOffsets</code> to true when subscribing.
</aside>

Example messages:


> Example initial response:

```json
{
  "type": "subscribed",
  "connection_id": "87b25218-0170-4111-bfbf-d9f0a506fcab",
  "message_id": 1,
  "channel": "v3_orderbook",
  "id": "ETH-USD",
  "contents": {
    "bids": [
      {
        "price": "1779",
        "size": "11.24"
      },
      {
        "price": "1778.5",
        "size": "18"
      }
    ],
    "asks": [
      {
        "price": "1782.8",
        "size": "10"
      },
      {
        "price": "1784",
        "size": "2.81"
      }
    ]
  }
}
```

> Example initial response if <code>includeOffsets</code> is set to true:

Request:

```json
{
  "type": "subscribe",
  "channel": "v3_orderbook",
  "id": "ETH-USD",
  "includeOffsets": "true"
}
```

Response:

```json
{
  "type": "subscribed",
  "connection_id": "14f7c481-1e1f-4f5c-8c5c-7b114209d8ce",
  "message_id": 1,
  "channel": "v3_orderbook",
  "id": "ETH-USD",
  "contents": {
    "bids": [
      {
        "price": "1778.8",
        "offset": "36850163",
        "size": "11"
      },
      {
        "price": "1776.7",
        "offset": "36849225",
        "size": "5.9"
      }
    ],
    "asks": [
      {
        "price": "1783",
        "offset": "36848764",
        "size": "13"
      },
      {
        "price": "1784",
        "offset": "36848433",
        "size": "4.3"
      }
    ]
  }
}
```

### Channel Data

Subsequent responses will contain the new order sizes for any price levels that have changed since the previous update:

e.g:

> Subsequent messages

```json
{
  "type": "channel_data",
  "id": "BTC-USD",
  "connection_id": "e2a6c717-6f77-4c1c-ac22-72ce2b7ed77d",
  "channel": "v3_orderbook",
  "message_id": 2,
  "contents": {
    "offset": "178",
    "bids": [["102", "12"]],
    "asks": [["104", "0" ]]
  }
}
```

E.g: if some orders at "102" price, get filled, then the update would be ["102", "12"], where "12" is the new size.
If there are no more asks at "104", then the ask update would be ["104", "0"].

## Trades

To subscribe:

| field   | type   | description                                       |
|---------|--------|---------------------------------------------------|
| type    | string | Set to <code>subscribe</code>                     |
| channel | string | Set to <code>v3_trades</code>                     |
| id      | string | The market to subscribe to e.g. BTC-USD, LINK-USD |

### Initial Response:

The initial response will contain the historical trades and will be the same structure as GET `/v3/trades/:market`.

| field    | description                                   |
|----------|-----------------------------------------------|
| type     | will be <code>subscribed</code>               |
| channel  | the channel name, i.e. <code>v3_trades</code> |
| id       | the market subscribed to e.g. BTC-USD         |
| contents | the message contents                          |

The contents is structured as:

| field  | type               | description                         |
|--------|--------------------|-------------------------------------|
| trades | array<PublicTrade> | See <code>PublicTrade</code> below. |

PublicTrade:

| field       | type                  | description                                                        |
|-------------|-----------------------|--------------------------------------------------------------------|
| side        | string                | <code>BUY</code> or <code>SELL</code>                              |
| size        | string                | size of the trade                                                  |
| price       | string                | price of the trade                                                 |
| createdAt   | ISO time of the trade | time of the trade                                                  |
| liquidation | boolean               | <code>true</code> if the trade was the result of a liquidation, <code>false</code> otherwise |

Example messages:

> Example initial response:

```json
{
  "type": "subscribed",
  "id": "BTC-USD",
  "connection_id": "e2a6c717-6f77-4c1c-ac22-72ce2b7ed77d",
  "channel": "v3_trades",
  "message_id": 1,
  "contents": {
    "trades": [
      {
        "side": "BUY",
        "size": "100",
        "price": "4000",
        "createdAt": "2020-10-29T00:26:30.759Z"
      },
      {
        "side": "BUY",
        "size": "100",
        "price": "4000",
        "createdAt": "2020-11-02T19:45:42.886Z"
      },
      {
        "side": "BUY",
        "size": "100",
        "price": "4000",
        "createdAt": "2020-10-29T00:26:57.382Z"
      }
    ]
  }
}
```

### Channel Data

Subsequent responses will contain the recently created trades. e.g:

> Subsequent responses

```json
{
  "type": "channel_data",
  "id": "BTC-USD",
  "connection_id": "e2a6c717-6f77-4c1c-ac22-72ce2b7ed77d",
  "channel": "v3_trades",
  "message_id": 2,
  "contents": {
    "trades": [
      {
        "side": "BUY",
        "size": "100",
        "price": "4000",
        "createdAt": "2020-11-29T00:26:30.759Z"
      },
      {
        "side": "SELL",
        "size": "100",
        "price": "4000",
        "createdAt": "2020-11-29T14:00:03.382Z"
      }
    ]
  }
}
```

## Markets

To subscribe:

| field   | type   | description                    |
|---------|--------|--------------------------------|
| type    | string | Set to <code>subscribe</code>  |
| channel | string | Set to <code>v3_markets</code> |

### Initial Response:

Same as [GET /v3/markets](#get-markets)

### Channel Data

Subsequent responses will contain an update for one or more markets. Updates will be sent any time a field(s) changes on a market(s). Updates will only contain the field(s) that have changed:

> Subsequent responses

```json
{
  "type": "channel_data",
  "connection_id": "e2a6c717-6f77-4c1c-ac22-72ce2b7ed77d",
  "channel": "v3_markets",
  "message_id": 2,
  "contents": {
    "ETH-USD": {
        "oraclePrice": "100.23"
    },
    "BTC-USD": {
        "indexPrice": "100.23",
        "priceChange24H": "0.12",
        "initialMarginFraction": "1.23"
    }
  }
}
```


# File: v4-documentation/old-docs/pages/api_integration-constants.md

# Constants

| Name                        | Value  | Description                                                                                                                                                                                                                   |
| --------------------------- | ------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `sdk.DefaultPowerReduction` | `1e18` | The staking power is equal the number of staked-token coins divided by this number (to prevent overflow). This number typically denotes how many of the staked-token denom are considered to be equal to one canonical token. |

# Module Accounts

In Cosmos-SDK, a module account is an account with address generated by hashing a string. The module account has no known private key and is therefore only controlled by the state-machine and governance. Here we list the module account addresses (assuming the default HRP of `dydx`) and the hashed string that results in the address.

| Module           | Name                | Address                                       | String                     |
| ---------------- | ------------------- | --------------------------------------------- | -------------------------- |
| `x/auth`         | Fee Collector       | `dydx17xpfvakm2amg962yls6f84z3kell8c5leqdyt2` | `"fee_collector"`          |
| `x/bridge`       | Bridge Module       | `dydx1zlefkpe3g0vvm9a4h0jf9000lmqutlh9jwjnsv` | `"bridge"`                 |
| `x/distribution` | Distribution Module | `dydx1jv65s3grqf6v6jl3dp4t6c9t9rk99cd8wx2cfg` | `"distribution"`           |
| `x/staking`      | Bonded Pool         | `dydx1fl48vsnmsdzcv85q5d2q4z5ajdha8yu3uz8teq` | `"bonded_tokens_pool"`     |
| `x/staking`      | Not-Bonded Pool     | `dydx1tygms3xhhs3yv487phx3dw4a95jn7t7lgzm605` | `"not_bonded_tokens_pool"` |
| `x/gov`          | Gov Module          | `dydx10d07y265gmmuvt4z0w9aw880jnsr700jnmapky` | `"gov"`                    |
| `x/ibc`          | IBC Module          | `dydx1yl6hdjhmkf37639730gffanpzndzdpmh8xcdh5` | `"transfer"`               |
| `x/subaccounts`  | Subaccounts Module  | `dydx1v88c3xv9xyv3eetdx0tvcmq7ung3dywp5upwc6` | `"subaccounts"`            |
| `x/clob`         | Insurance Fund      | `dydx1c7ptc87hkd54e3r7zjy92q29xkq7t79w64slrq` | `"insurance_fund"`         |
| `x/rewards`      | Rewards Treasury    | `dydx16wrau2x4tsg033xfrrdpae6kxfn9kyuerr5jjp` | `"rewards_treasury"`       |
| `x/rewards`      | Rewards Vester      | `dydx1ltyc6y4skclzafvpznpt2qjwmfwgsndp458rmp` | `"rewards_vester"`         |
| `x/vault`        | Megavault           | `dydx18tkxrnrkqc2t0lr3zxr5g6a4hdvqksylxqje4r` | `"megavault"`              |
| `x/vest`         | Community Treasury  | `dydx15ztc7xy42tn2ukkc0qjthkucw9ac63pgp70urn` | `"community_treasury"`     |
| `x/vest`         | Community Vester    | `dydx1wxje320an3karyc6mjw4zghs300dmrjkwn7xtk` | `"community_vester"`       |


# File: v4-documentation/old-docs/pages/api_integration-full-node-streaming.md

# Full Node gRPC Streaming

Last updated for: `v7.0.2`

Enable full node streaming to expose a stream of orderbook updates (L3), fills, taker orders, and subaccount updates, allowing clients to maintain a full view of the orderbook and various exchange activities. Note that the orderbook state can vary slightly between nodes due to dYdX's offchain orderbook design.


## Enabling Streaming
Full node streaming supports two streaming protocols. Information can be streamed via [gRPC](https://grpc.io/), a streaming RPC protocol developed by Google and used in CosmosSDK, or Websockets. Use the following flags to configure full node streaming features:

| CLI Flag | Type | Default | Short Explanation |
| -------- | ----- | ------- | -------- |
| grpc-streaming-enabled | bool | false | Toggle on to enable grpc-based full node streaming. |
| grpc-streaming-flush-interval-ms | int | 50 | Buffer flush interval for batch emission of protocol-side updates. |
| grpc-streaming-max-batch-size | int | 2000 | Maximum protocol-side update buffer before dropping all streaming connections. |
| grpc-streaming-max-channel-buffer-size | int | 2000 | Maximum channel size before dropping slow or erroring grpc connections. Decreasing this will more aggressively drop slow client connections. |
| websocket-streaming-enabled | bool | false | Toggle on to enable websocket-based streaming. Must be used in conjunction with `grpc-streaming-enabled`. |
| websocket-streaming-port | int | 9092 | Port number to expose for websocket streaming. |
| fns-snapshot-interval | int | 0 | If set to a nonzero number, snapshots will be sent out at this block interval. Used for debugging purposes. |


**Disclaimer:** We recommend you use this exclusively with your own node, as supporting multiple public gRPC streams with unknown client subscriptions may result in degraded performance.

## Connecting to the Stream

After setting up a full node with gRPC streaming enabled, you can connect to the stream using any gRPC client.
To follow along with [Google's documentation on gRPC streaming clients](https://grpc.io/docs/languages/go/basics/#client):

1. Clone the [github.com/dydxprotocol/v4-chain](https://github.com/dydxprotocol/v4-chain) repository at the same version as your full node.
2. Generate the protos: `make proto-gen && make proto-export-deps`.
3. The generated protos are now in the `.proto-export-deps` directory.
4. Use the protobuf compiler (protoc) to [generate stubs](https://protobuf.dev/getting-started/) in any supported language.
5. Follow [Google's documentation](https://grpc.io/docs/languages/go/basics/#client) to write a client that can read from the stream.
6. Connect to the stream defined in the `dydxprotocol.clob.Query` service ([StreamOrderbookUpdates](https://github.com/dydxprotocol/v4-chain/blob/4199c3e7b00ded24774d49ce8adcbaaa8325ddc1/proto/dydxprotocol/clob/query.proto#L63-L67)).

For Python, the corresponding code is already generated in [the v4-proto PyPi package](https://pypi.org/project/v4-proto/).

To connect via websocket, connect to the specified websocket server port at endpoint `/ws`. Default port number is `9092`, but it can be configured via cli flag. There are two query parameters. `clobPairIds` is a list of clob pair ids to subscribe to, and `subaccountIds` are a list of subaccount ids to subscribe to.

## Maintaining Orderbook and Subaccount State 

### Overview

1. Connect to the stream and subscribe to updates for a series of clob pair ids, each of which corresponds to a tradeable instrument, and subaccount ids, each of which corresponds to a subaccount.
2. Discard order messages until you receive a `StreamOrderbookUpdate` with `snapshot` set to `true`. This message contains the full orderbook state for each clob pair.
3. Similarly, discard subaccount messages until you receive a `StreamSubaccountUpdate` with `snapshot` set to `true`. This message contains the full subaccount state for each subscribed subaccount.
4. When you see an `OrderPlaceV1` message, insert the order into the book at the end of the queue on its price level. Track the order's initial quantums (quantity) and total filled quantums.
5. When you see an `OrderUpdateV1` message, update the order's total filled quantums.
6. When you see a `ClobMatch` (trade) message, update the total filled quantums for each maker order filled using the `fill_amounts` field. 
	- Note that, similar to `OrderUpdateV1`, the `fill_amounts` field represents the order's total filled quantity up to this point. This is not the amount filled in this specific match, but rather the cumulative amount filled across all matches for this order. 
    - The order's quantity remaining is always its initial quantity minus its total filled quantity.
    - Note that both `OrderUpdateV1` and `ClobMatch` messages must be processed to maintain the correct book state. See [OrderUpdateV1](#orderupdatev1) for details.
7. When you see an `OrderRemoveV1` message, remove the order from the book.
8. When you see a `StreamSubaccountUpdate` message with `snapshot` set to `false`, incrementally update the subaccount's balances and positions.
8. When you see a `StreamTakerOrder` message, state does not need to be updated. Taker orders are purely informational and are emitted whenever a taker order enters the matching loop, regardless of success or failure.

Note:
- The order subticks (price) and quantums (quantity) fields are encoded as integers and 
  require [translation to human-readable values](https://github.com/dydxprotocol/grpc-stream-client/blob/d8cbbc3c6aeb454078c72204491727b243c26e19/src/market_info.py#L1).
- Each node's view of the book is subjective, because order messages arrive at different nodes in different orders. When a block is proposed, nodes "sync" subsets of their book states to cohere with the trades seen by the block proposer.
- Only `ClobMatch` messages with `execModeFinalize` are trades confirmed by consensus.
	- Use all `ClobMatch` messages to update the orderbook state. The node's book state is optimistic, and reverts if fills are not confirmed, in which case a series of `OrderRemoveV1`, `OrderPlaceV1` and `OrderUpdateV1` messages are sent to represent the modifications to the full node's book state.
    - Treat only `ClobMatch` messages with `execModeFinalize` as confirmed trades.
    - See [Reference Material](#reference-material) for more information.


### Request / Response

To subscribe to the stream, the client can send a 'StreamOrderbookUpdatesRequest' specifying the clob pair ids and subaccount ids to subscribe to.

<details>

<summary>Protobuf Structs</summary>

```protobuf
// StreamOrderbookUpdatesRequest is a request message for the
// StreamOrderbookUpdates method.
message StreamOrderbookUpdatesRequest {
  // Clob pair ids to stream orderbook updates for.
  repeated uint32 clob_pair_id = 1;

  // Subaccount ids to stream subaccount updates for.
  repeated dydxprotocol.subaccounts.SubaccountId subaccount_ids = 2;
}
```
</details>
&nbsp;

Response will contain a `oneof` field that contains either:
- `StreamOrderbookUpdate`
	- Contains one or more `OffChainUpdateV1` orderbook updates (Add/Remove/Update)
	- boolean field indicating if the updates are coming from a snapshot or not.
- `StreamOrderbookFill`
	- Contains a singular `ClobMatch` object describing a fill (order or liquidation).
		- Represents one taker order matched with 1 or more maker orders.
		- Matched quantums are provided for each pair in the match.
	- `orders` field contains full order information at time of matching. Contains all maker and taker orders involved in the `ClobMatch` object.
		- Prices within a Match are matched at the maker order price.
	- `fill_amounts` contains the absolute, total filled quantums of each order as stored in state.
		- fill_amounts should be zipped together with the `orders` field. Both arrays should have the same length.
- `StreamTakerOrder`
  - Contains a oneof `TakerOrder` field which represents the order that entered the matching loop.
    - Could be a regular order or a Liquidation Order.
  - Contains a `StreamTakerOrderStatus` field which represents the status of a taker order after it has finished the matching loop.
    - `OrderStatus` is a uint32 describing the result of the taker order matching. Only value `0` indicates success. Possible values found [here](https://github.com/dydxprotocol/v4-chain/blob/main/protocol/x/clob/types/orderbook.go#L118-L152).
      - @jonfung to update to static link
    - `RemainingQuantums` represents the remaining amount of non-matched quantums for the taker order.
    - `OptimisticallyFilledQuantums` represents the number of quantums filled *during this matching loop*. It does not include quantums filled before this matching loop, if the order was a replacement order and was previously filled.
- `StreamSubaccountUpdate`
  - Contains a singular `SubaccountId` object to identify the subaccount.
  - multiple `SubaccountPerpetualPosition`s to represent the perpetual positions of the subaccount.
    - each `SubaccountPerpetualPosition` contains a perpetual id and the size of the position in base quantums.
  - multiple `SubaccountAssetPosition`s to represent the asset positions of the subaccount. (i.e, usdc collateral positions)
    - each `SubaccountAssetPosition` contains an asset id and the size of the position in base quantums.

as well as `block_height` and `exec_mode` (see [Exec Modes Reference](#exec-mode-reference)). 

<details>

<summary>Protobuf Structs</summary>

```protobuf
// StreamOrderbookUpdatesResponse is a response message for the
// StreamOrderbookUpdates method.
message StreamOrderbookUpdatesResponse {
  // Batch of updates for the clob pair.
  repeated StreamUpdate updates = 1 [ (gogoproto.nullable) = false ];
}

// StreamUpdate is an update that will be pushed through the
// gRPC stream.
message StreamUpdate {
  // Contains one of an StreamOrderbookUpdate,
  // StreamOrderbookFill, StreamTakerOrderStatus, StreamSubaccountUpdate.
  oneof update_message {
    StreamOrderbookUpdate orderbook_update = 1;
    StreamOrderbookFill order_fill = 2;
    StreamTakerOrder taker_order = 3;
    dydxprotocol.subaccounts.StreamSubaccountUpdate subaccount_update = 4;
  }

  // Block height of the update.
  uint32 block_height = 5;

  // Exec mode of the update.
  uint32 exec_mode = 6;
}

// StreamOrderbookUpdate provides information on an orderbook update. Used in
// the full node gRPC stream.
message StreamOrderbookUpdate {
  // Orderbook updates for the clob pair. Can contain order place, removals,
  // or updates.
  repeated dydxprotocol.indexer.off_chain_updates.OffChainUpdateV1 updates = 1
      [ (gogoproto.nullable) = false ];

  // Snapshot indicates if the response is from a snapshot of the orderbook.
  // This is true for the initial response and false for all subsequent updates.
  // Note that if the snapshot is true, then all previous entries should be
  // discarded and the orderbook should be resynced.
  bool snapshot = 2;
}

// StreamOrderbookFill provides information on an orderbook fill. Used in
// the full node gRPC stream.
message StreamOrderbookFill {
  // Clob match. Provides information on which orders were matched
  // and the type of order.
  ClobMatch clob_match = 1;

  // All orders involved in the specified clob match. Used to look up
  // price of a match through a given maker order id.
  repeated Order orders = 2 [ (gogoproto.nullable) = false ];

  // Resulting fill amounts for each order in the orders array.
  repeated uint64 fill_amounts = 3 [ (gogoproto.nullable) = false ];
}

// StreamTakerOrder provides information on a taker order that was attempted
// to be matched on the orderbook.
// It is intended to be used only in full node streaming.
message StreamTakerOrder {
  // The taker order that was matched on the orderbook. Can be a
  // regular order or a liquidation order.
  oneof taker_order {
    Order order = 1;
    StreamLiquidationOrder liquidation_order = 2;
  }

  // Information on the taker order after it is matched on the book,
  // either successfully or unsuccessfully.
  StreamTakerOrderStatus taker_order_status = 3;
}

// StreamTakerOrderStatus is a representation of a taker order
// after it is attempted to be matched on the orderbook.
// It is intended to be used only in full node streaming.
message StreamTakerOrderStatus {
  // The state of the taker order after attempting to match it against the
  // orderbook. Possible enum values can be found here:
  // https://github.com/dydxprotocol/v4-chain/blob/main/protocol/x/clob/types/orderbook.go#L105
  uint32 order_status = 1;

  // The amount of remaining (non-matched) base quantums of this taker order.
  uint64 remaining_quantums = 2;

  // The amount of base quantums that were *optimistically* filled for this
  // taker order when the order is matched against the orderbook. Note that if
  // any quantums of this order were optimistically filled or filled in state
  // before this invocation of the matching loop, this value will not include
  // them.
  uint64 optimistically_filled_quantums = 3;
}

// StreamSubaccountUpdate provides information on a subaccount update. Used in
// the full node GRPC stream.
message StreamSubaccountUpdate {
  SubaccountId subaccount_id = 1;
  // updated_perpetual_positions will each be for unique perpetuals.
  repeated SubaccountPerpetualPosition updated_perpetual_positions = 2;
  // updated_asset_positions will each be for unique assets.
  repeated SubaccountAssetPosition updated_asset_positions = 3;
  // Snapshot indicates if the response is from a snapshot of the subaccount.
  // All updates should be ignored until snapshot is received.
  // If the snapshot is true, then all previous entries should be
  // discarded and the subaccount should be resynced.
  // For a snapshot subaccount update, the `updated_perpetual_positions` and
  // `updated_asset_positions` fields will contain the full state of the
  // subaccount.
  bool snapshot = 4;
}

// SubaccountPerpetualPosition provides information on a subaccount's updated
// perpetual positions.
message SubaccountPerpetualPosition {
  // The `Id` of the `Perpetual`.
  uint32 perpetual_id = 1;
  // The size of the position in base quantums. Negative means short.
  int64 quantums = 2;
}

// SubaccountAssetPosition provides information on a subaccount's updated asset
// positions.
message SubaccountAssetPosition {
  // The `Id` of the `Asset`.
  uint32 asset_id = 1;
  // The absolute size of the position in base quantums.
  uint64 quantums = 2;
}
```
</details>


After subscribing to the orderbook updates, use the orderbook in the snapshot as the starting orderbook.
Similarly, use the subaccount state in the snapshot as the starting subaccount state.

### OrderPlaceV1
When `OrderPlaceV1` is received,  add the corresponding order to the end of the price level.
- This message is only used to modify the orderbook data structure (Bids, Asks).
- This message is sent out whenever an order is added to the in-memory orderbook.
- This may occur in various places such as when an order is initially placed, or when an order is replayed during the ProcessCheckState step.
- An `OrderPlaceV1` message is always be followed by an `OrderUpdateV1` message, which sets the intial fill amount (typically zero).

<details>

<summary>Code Snippet</summary>

```go
func (l *LocalOrderbook) AddOrder(order v1types.IndexerOrder) {
	l.Lock()
	defer l.Unlock()

	if _, ok := l.OrderIdToOrder[order.OrderId]; ok {
		l.Logger.Error("order already exists in orderbook")
	}

	subticks := order.GetSubticks()
	if order.Side == v1types.IndexerOrder_SIDE_BUY {
		if _, ok := l.Bids[subticks]; !ok {
			l.Bids[subticks] = make([]v1types.IndexerOrder, 0)
		}
		l.Bids[subticks] = append(l.Bids[subticks], order)
	} else {
		if _, ok := l.Asks[subticks]; !ok {
			l.Asks[subticks] = make([]v1types.IndexerOrder, 0)
		}
		l.Asks[subticks] = append(l.Asks[subticks], order)
	}

	l.OrderIdToOrder[order.OrderId] = order
	l.OrderRemainingAmount[order.OrderId] = 0
}
```
</details>

### OrderUpdateV1
When `OrderUpdateV1` is received, update the order's fill amount to the amount specified.
- This message is only used to update fill amounts. It carries information about an order's updated fill amount.
- This message is emitted when an order's fill amount changes due to something other than a `ClobMatch`.
    - This includes when deliverState is reset to the checkState from last block, or when branched state is written to and then discarded if there was a matching error.
    - For example, this could happen if the full node sees the order filled, and then the next block committed by consensus does not contain the expected fill, so the order’s quantity remaining resets to its state from the previous block.
- An update message will always accompany an order placement message.
- It's possible for an update message to be sent before a placement message. You can safely ignore update messages with order ids not in the orderbook.
- **Note that you must handle both `OrderUpdateV1` and `ClobMatch` messages to maintain the correct book state**.

<details>

<summary>Code Snippet</summary>

```go
func (l *LocalOrderbook) SetOrderFillAmount(
	orderId *v1types.IndexerOrderId,
	fillAmount uint64,
) {
	l.Lock()
	defer l.Unlock()

	if fillAmount == 0 {
		delete(l.FillAmounts, *orderId)
	} else {
		l.FillAmounts[*orderId] = fillAmount
	}
}
```
</details>


### OrderRemoveV1
When `OrderRemoveV1` is received, remove the order from the orderbook.
- This message is only used to modify the orderbook data structure (Bids, Asks).
- This message is emitted when an order is removed from the in-memory orderbook.
- Note that this does not mean the fills are removed from state yet.
	- When fills are removed from state, a separate Update message will be sent with 0 quantum.

<details>

<summary>Code Snippet</summary>

```go
func (l *LocalOrderbook) RemoveOrder(orderId v1types.IndexerOrderId) {
	l.Lock()
	defer l.Unlock()

	if _, ok := l.OrderIdToOrder[orderId]; !ok {
		l.Logger.Error("order not found in orderbook")
	}

	order := l.OrderIdToOrder[orderId]
	subticks := order.GetSubticks()

	if order.Side == v1types.IndexerOrder_SIDE_BUY {
		for i, o := range l.Bids[subticks] {
			if o.OrderId == order.OrderId {
				l.Bids[subticks] = append(
					l.Bids[subticks][:i],
					l.Bids[subticks][i+1:]...,
				)
				break
			}
		}
		if len(l.Bids[subticks]) == 0 {
			delete(l.Bids, subticks)
		}
	} else {
		for i, o := range l.Asks[subticks] {
			if o.OrderId == order.OrderId {
				l.Asks[subticks] = append(
					l.Asks[subticks][:i],
					l.Asks[subticks][i+1:]...,
				)
				break
			}
		}
		if len(l.Asks[subticks]) == 0 {
			delete(l.Asks, subticks)
		}
	}
	delete(l.OrderIdToOrder, orderId)
}
```

</details>

### StreamOrderbookFill/ClobMatch
This message is only used to update fill amounts, it does not add or remove orders from the book but can change the quantity remaining for open orders.

The `ClobMatch` data structure contains either a `MatchOrders` or a `MatchPerpetualLiquidation` object. Match Deleveraging events are not emitted. Within each Match object, a `MakerFill` array contains the various maker orders that matched with the singular taker order and the amount of quantums matched.

Note that all matches occur at the maker order price. The `orders` field in the `StreamOrderbookFill` object allow for price lookups based on order id. It contains all the maker order ids, and in the case of non-liquidation orders, it has the taker order.

Mapping each order in `orders` to the corresponding value in the `fill_amounts` field provides the absolute filled amount of quantums that each order is filled to after the ClobMatch was processed. 


<details>

<summary>Code Snippet</summary>

```go
// fillAmountMap is a map of order ids to fill amounts.
// The SetOrderFillAmount code can be found in `the `OrderUpdateV1` section.
func (c *GrpcClient) ProcessMatchOrders(
	matchOrders *clobtypes.MatchOrders,
	orderMap map[clobtypes.OrderId]clobtypes.Order,
	fillAmountMap map[clobtypes.OrderId]uint64,
) {
	takerOrderId := matchOrders.TakerOrderId
	clobPairId := takerOrderId.GetClobPairId()
	localOrderbook := c.Orderbook[clobPairId]

	indexerTakerOrder := v1.OrderIdToIndexerOrderId(takerOrderId)
	localOrderbook.SetOrderFillAmount(&indexerTakerOrder, fillAmountMap[takerOrderId])

	for _, fill := range matchOrders.Fills {
		makerOrder := orderMap[fill.MakerOrderId]
		indexerMakerOrder := v1.OrderIdToIndexerOrderId(makerOrder.OrderId)
		localOrderbook.SetOrderFillAmount(&indexerMakerOrder, fillAmountMap[makerOrder.OrderId])
	}
}

func (c *GrpcClient) ProcessMatchPerpetualLiquidation(
	perpLiquidation *clobtypes.MatchPerpetualLiquidation,
	orderMap map[clobtypes.OrderId]clobtypes.Order,
	fillAmountMap map[clobtypes.OrderId]uint64,
) {
	localOrderbook := c.Orderbook[perpLiquidation.ClobPairId]
	for _, fill := range perpLiquidation.GetFills() {
		makerOrder := orderMap[fill.MakerOrderId]
		indexerMakerOrderId := v1.OrderIdToIndexerOrderId(makerOrder.OrderId)
		localOrderbook.SetOrderFillAmount(&indexerMakerOrderId, fillAmountMap[makerOrder.OrderId])
	}
}
```

</details>

### StreamSubaccountUpdate
This message is used to update subaccount balances and positions.

The initial message for a subaccount will have `snapshot` set to `true`. This message contains the full state of the subaccount. All updates should be ignored until the snapshot is received. Subsequent updates will contain updates to the positions and balances of the subaccount. They should be merged in with the existing state of the subaccount.

Apart from the initial snapshot, this mesage will only be sent out for subaccount updates that are in consensus.

<details>

<summary>Code Snippet</summary>

```go
type SubaccountId struct {
    Owner  string
    Number int
}

type SubaccountPerpetualPosition struct {
    PerpetualId int
    Quantums    int
}

type SubaccountAssetPosition struct {
    AssetId  int
    Quantums int
}

type SubaccountState struct {
    SubaccountId       SubaccountId
    PerpetualPositions map[int]SubaccountPerpetualPosition
    AssetPositions     map[int]SubaccountAssetPosition
}

func (c *GrpcClient) ProcessSubaccountUpdate(
    subaccountUpdate *satypes.StreamSubaccountUpdate,
    subaccountMap map[satypes.SubaccountId]SubaccountState,
) {
    // Extract the subaccount ID from the update
    subaccountId := *subaccountUpdate.SubaccountId

    // Check if this is a snapshot
    if subaccountUpdate.Snapshot {
        // Replace the entire subaccount state with the snapshot data
        subaccountState := SubaccountState{
            SubaccountId:       subaccountId,
            PerpetualPositions: make(map[int]SubaccountPerpetualPosition),
            AssetPositions:     make(map[int]SubaccountAssetPosition),
        }

        // Populate perpetual positions from snapshot
        for _, perpPositionUpdate := range subaccountUpdate.UpdatedPerpetualPositions {
            subaccountState.PerpetualPositions[perpPositionUpdate.PerpetualId] = *perpPositionUpdate
        }

        // Populate asset positions from snapshot
        for _, assetPositionUpdate := range subaccountUpdate.UpdatedAssetPositions {
            subaccountState.AssetPositions[assetPositionUpdate.AssetId] = *assetPositionUpdate
        }

        // Update the map with the new snapshot state
        subaccountMap[subaccountId] = subaccountState
    } else {
        // If not a snapshot, retrieve or initialize the current subaccount state
        subaccountState, exists := subaccountMap[subaccountId]
        if !exists {
            subaccountState = SubaccountState{
                SubaccountId:       subaccountId,
                PerpetualPositions: make(map[int]SubaccountPerpetualPosition),
                AssetPositions:     make(map[int]SubaccountAssetPosition),
            }
        }

        // Update perpetual positions
        for _, perpPositionUpdate := range subaccountUpdate.UpdatedPerpetualPositions {
            if perpPositionUpdate.Quantums != 0 {
                subaccountState.PerpetualPositions[perpPositionUpdate.PerpetualId] = *perpPositionUpdate
            } else {
                // Delete the entry if the position size is zero
                delete(subaccountState.PerpetualPositions, perpPositionUpdate.PerpetualId)
            }
        }

        // Update asset positions
        for _, assetPositionUpdate := range subaccountUpdate.UpdatedAssetPositions {
            if assetPositionUpdate.Quantums != 0 {
                subaccountState.AssetPositions[assetPositionUpdate.AssetId] = *assetPositionUpdate
            } else {
                // Delete the entry if the asset quantity is zero
                delete(subaccountState.AssetPositions, assetPositionUpdate.AssetId)
            }
        }

        // Update the map with the modified state
        subaccountMap[subaccountId] = subaccountState
    }
}
```

</details>

### StreamTakerOrder

This message is purely an informational message used to indicate whenever a taker order is matched against the orderbook. No internal state in clients need to be updated.

Information provided in the struct:
- One of (taker order, liquidation order) entering matching loop
- Status of order after matching. If order failed to match, status code provides the reason for failure (i.e post only order crosses book)
- Remaining non-matched quantums for the taker order
- Quantity of optimistically matched quantums during this matching order loop.

Note that by protocol design, all `StreamTakerOrderStatus` emissions will be optimistic from CheckTx state. This is due to the fact that each node maintains it's own orderbook, thus all matching operations when a taker order enters the matching loop will be optimistic. If confirmed fill amounts in consensus are desired, `StreamOrderbookFill` objects will be emitted during DeliverTx for proposed blocks.

<details>

<summary>Code Snippet</summary>

```go
type StreamTakerOrderStatus struct {
	OrderStatus uint32
	RemainingQuantums uint64
	OptimisticallyFilledQuantums uint64
}

func (c *GrpcClient) ProcessStreamTakerOrder(
    streamTakerOrder *satypes.StreamTakerOrder,
) {
	takerOrder := streamTakerOrder.GetOrder()
	takerOrderLiquidation := streamTakerOrder.GetLiquidationOrder()
	takerOrderStatus := streamTakerOrder.GetTakerOrderStatus()
	if takerOrderStatus.OrderStatus == 0 || takerOrderStatus.OrderStatus == 0 {
		if takerOrder != nil {
			// Process success of regular taker order
		}
		if takerOrderLiquidation != nil {
			// Process success of liquidation taker order
		}
	}
}
```

</details>

## Reference Material

### Optimistic Orderbook Execution

By protocol design, each validator has their own version of the orderbook and optimistically processes orderbook matches. As a result, you may see interleaved sequences of order removals, placements, and state fill amount updates when optimistically processed orderbook matches are removed and later replayed on the local orderbook.

![full node streaming diagram](../artifacts/full_node_streaming_diagram.jpg)

Note that DeliverTx maps to exec mode `execModeFinalize`.

### Staged DeliverTx Validation

In DeliverTx, all of the updates emitted are finalized and in consensus. A batch of updates will be sent out in the same `StreamOrderbookUpdatesResponse` object. In consensus, fills and subaccount updates will be emitted.

### Finalized Subaccount Updates

Only finalized subaccount updates are sent. Snapshots are sent during PrepareCheckState, so the execMode will be set to `102` for subaccount snapshots. Finalized incremental subaccount updates are sent with execMode `7`.

### Exec Mode Reference
<details>

<summary>Exec Modes</summary>

```go
	execModeCheck               = 0 // Check a transaction
	execModeReCheck             = 1 // Recheck a (pending) transaction after a commit
	execModeSimulate            = 2 // Simulate a transaction
	execModePrepareProposal     = 3 // Prepare a block proposal
	execModeProcessProposal     = 4 // Process a block proposal
	execModeVoteExtension       = 5 // Extend or verify a pre-commit vote
	execModeVerifyVoteExtension = 6 // Verify a vote extension
	execModeFinalize            = 7 // Finalize a block proposal
	ExecModeBeginBlock          = 100
	ExecModeEndBlock            = 101
	ExecModePrepareCheckState   = 102
```
</details>
<br>

### Taker Order Status Reference

Values are defined in code [here](https://github.com/dydxprotocol/v4-chain/blob/main/protocol/x/clob/types/orderbook.go#L118-L152).
  - @jonfung to update to static link

| Value    | Status | Description |
| -------- | ------ | ------- |
| 0  |  Success  | Order was successfully matched and/or added to the orderbook.|
| 1  |  Undercollateralized  | Order failed collateralization checks when matching or placed on orderbook. Order was cancelled. |
| 2  |  InternalError  | Order caused internal error and was cancelled. |
| 3  |  ImmediateOrCancelWouldRestOnBook  | Order is an IOC order that would have been placed on the orderbook. Order was cancelled. |
| 4  |  ReduceOnlyResized  | Order was resized since it would have changed the user's position size. |
| 5  |  LiquidationRequiresDeleveraging  | Not enough liquidity to liquidate the subaccount profitably on the orderbook. Order was not fully matched because insurance fund did not have enough funds to cover losses from performing liquidation. Subaccount requires deleveraging. |
| 6  |  LiquidationExceededSubaccountMaxNotionalLiquidated  | Liquidation order could not be matched because it exceeds the max notional liquidated in this block. |
| 7  |  LiquidationExceededSubaccountMaxInsuranceLost  | Liquidation order could not be matched because it exceeds the max funds lost for hte insurance fund in this block. |
| 8  |  ViolatesIsolatedSubaccountConstraints  | Matching this order would lead to the subaccount violating isolated perpetual constraints. Order was cancelled. |
| 9  |  PostOnlyWouldCrossMakerOrder  | Matching this order would lead to the post only taker order crossing the orderbook. Order wasa cancelled. |

<br>

### Example Scenario

- Trader places a bid at price 100 for size 1
  - OrderPlace, price = 100, size = 1
  - OrderUpdate, total filled amount = 0
- Trader replaces that original bid to be price 99 at size 2
  - OrderRemove
  - OrderPlace, price = 99, size = 2
  - OrderUpdate, total filled amount = 0
- Another trader submits an IOC ask at price 100 for size 1.
  - Full node doesn't see this matching anything so no updates.
- Block is confirmed that there was a fill for the trader's original order at price 100 for size 1 (block proposer didn't see the order replacement)
  - OrderUpdate, set total fill amount to be 0 (no-op) from checkState -> deliverState reset
  - MatchOrder emitted for block proposer's original order match, total filled amount = 1

### Metrics and Logs

| Metric | Type | Explanation |
| -------- | ----- | ------- |
| grpc_send_orderbook_updates_latency.quantile | histogram | Latency for each orderbook cache buffer enqueue |
| grpc_send_orderbook_updates_latency.count | count | number orderbook updates enqueued in cache buffer |
| grpc_send_orderbook_snapshot_latency.quantile | histogram | Latency for each snapshot orderbook emission |
| grpc_send_orderbook_snapshot_latency.count | count | number of order book snapshots emitted |
| grpc_send_subaccount_update_count | count | Number of subaccount updates emitted |
| grpc_send_orderbook_fills_latency.quantile | histogram | Latency for each orderbook fill cache buffer enqueue |
| grpc_send_orderbook_fills_latency.count | count | number orderbook snapshots enqueued in cache buffer |
| grpc_add_update_to_buffer_count | count | Number of total update objects added to the cache buffer |
| grpc_add_to_subscription_channel_count | count | Number of updates added to each per-subscription channel buffer. Tagged by `subscription_id`. |
| grpc_send_response_to_subscriber_count | count | Number of updates sent from each per-subscription channel buffer to the client. Tagged by `subscription_id`. |
| grpc_stream_subscriber_count | count | number of streaming connections currently connected to the full node |
| grpc_stream_num_updates_buffered | histogram | number of updates in the full node's buffer cache of updates. Once this hits `grpc-streaming-max-batch-size`, all subscriptions will be dropped. Use with `quantile:0.99` in order to observe maximum amount of updates. |
| grpc_flush_updates_latency.count | count | number of times the buffer cache is flushed. |
| grpc_flush_updates_latency.quantile | histogram | Latency of each buffer cache flush call into subscription channel. |
| grpc_subscription_channel_length.quantile | histogram | Length of each subscription's channel buffer. Tagged by `subscription_id`. Use with `quantile:0.99` in order to observe subscription channel length for subscription ids. Once this hits `grpc-streaming-max-channel-buffer-size`, the offending subscription will be dropped. |

All logs from grpc streaming are tagged with `module: full-node-streaming`.

### Protocol-side buffering and Slow gRPC Client Connections

The full node maintains a length-configurable buffer cache of streaming updates to ensure bursts of protocol updates do not induce full node lag. If the buffer reaches maximum capacity, all connections and updates are dropped, and subscribers will have to re-subscribe. The buffer is periodically flushed into each per-subscription golang channel at a configurable set interval of time, defaulting to 50ms.

To ensure slow client connections do not induce full node lag, each client subscription has a unique goroutine and golang channel that pushes updates through the grpc stream. If the channel buffer grows beyond the configurable `grpc-streaming-max-channel-buffer-size` parameter, the goroutine will be stopped. With the poller gone, the channel buffer will eventually grow and hit the max buffer size, at which the lagging subscription is pruned.

Metrics and logs are emitted to help tune both of these parameters.

### FAQs

Q: Suppose the full node saw the cancellation of order X at t0 before the placement of the order X at t1. What would the updates be like?
- **A: No updates because the order was never added to the book**

Q: A few questions because it often results in crossed books:
In which cases shall we not expect to see OrderRemove message?
- Post only reject? → **PO reject won’t have a removal since they were never added to the book**
- IOC/FOK auto cancel? → **IOC/FOK also won’t have a removal message for similar reason**
- Order expired outside of block window? → **expired orders will generate a removal message**
- Passive limit order was fully filled → **fully filled maker will generate a removal message**
- Aggressive limit order was fully filled? → **fully filled taker won’t have a removal**

Q: Why does `StreamOrderbookUpdate` use IndexerOrderId and `StreamOrderbookFill` use dydxprotocol.OrderId?
- A: gRPC streaming exposes inner structs of the matching engine and our updates are processed differently from fills. The two data structures have equivalent fields, and a lightweight translation layer to go from Indexer OrderId to Protocol OrderId can be written.

Q: I only want to listen to confirmed updates. I do not want to process optimistic fills.
- A: You will want to only process messages from DeliverTx stage (`execModeFinalize`). This step is when we save proposed matches from the block proposer into state. These updates will have exec mode execModeFinalize.

Q: Why do I see an Order Update message for a new OrderId before an Order Place message?
- A: During DeliverTx, the first step we do is to reset fill amounts (via OrderUpdate messages) for all orders involved in the proposed and local operations queue due to the deliver state being reset to the check state from last block. We "reset" fill order amounts to 0 for orders that the block proposer has seen but has not gossiped to our full node yet. In the future, we may reduce the number of messages that are sent, but for now we are optimizing for orderbook correctness.

Q: How do I print the gRPC stream at the command line?
- A: Use the [grpcurl](https://github.com/fullstorydev/grpcurl) tool. Connect to a full node stream with:
	```
	grpcurl -plaintext -d '{"clobPairId":[0,1], "subaccountIds": [{"owner": "dydx1nzuttarf5k2j0nug5yzhr6p74t9avehn9hlh8m", "number": 0}]}' 127.0.0.1:9090 dydxprotocol.clob.Query/StreamOrderbookUpdates
	```

Q: Is there a sample client?
- A: Example client which subscribes to the stream and maintains a local orderbook: [dydxprotocol/grpc-stream-client](https://github.com/dydxprotocol/grpc-stream-client/)

## Changelog

### v7.0.2
- perp position to signed int for tracking long/short positions

### v6.0.8
- added taker order message to stream
- added subaccount update message to stream
- Finalized DeliverTx updates are all batched together in a single message
- Metrics modifications
- Websocket support

### v5.0.5
- added update batching and per-channel channel/goroutines to not block full node on laggy subscriptions
- Protobuf breaking change: Shifted block height and exec mode from `StreamOrderbookUpdatesResponse` to `StreamUpdate`
- Metrics


# File: v4-documentation/old-docs/pages/api_integration-repositories.md

# Open Source Repositories

Please find the open source repositories on our [GitHub](https://github.com/dydxprotocol)

* [Monorepo](https://github.com/dydxprotocol/v4-chain)
    * [Protocol](https://github.com/dydxprotocol/v4-chain/tree/main/protocol)
    * [Indexer](https://github.com/dydxprotocol/v4-chain/tree/main/indexer)
* [Clients](https://github.com/dydxprotocol/v4-clients)
* [Frontend](https://github.com/dydxprotocol/v4-web)
* [iOS](https://github.com/dydxprotocol/v4-native-ios)
* [Android](https://github.com/dydxprotocol/v4-native-android)
* [Terraform](https://github.com/dydxprotocol/v4-infrastructure)

When contributing, please ensure your commits are verified. You can follow these steps to do so:
* [Generate a new signing key](https://docs.github.com/en/authentication/managing-commit-signature-verification/generating-a-new-gpg-key) for work use and [turn on Vigilant Mode](https://docs.github.com/en/authentication/managing-commit-signature-verification/displaying-verification-statuses-for-all-of-your-commits)
* [Tell Git about your GPG key](https://docs.github.com/en/authentication/managing-commit-signature-verification/telling-git-about-your-signing-key) and install `pinentry` if necessary


# File: v4-documentation/old-docs/pages/concepts-limit-order-book-and-matching.md

# Limit Order Book and Matching

This document outlines the key differences between centralized exchanges and dYdX Chain, focusing on the decentralized limit order book and matching engine.


## Blockchain Overview
<!-- TODO: Move this to a general explainer section and link to it -->

dYdX Chain is a p2p blockchain network using [CosmosSDK](https://github.com/cosmos/cosmos-sdk) and [CometBFT](https://github.com/cometbft/cometbft) (formerly Tendermint).

Anyone can run a full node using the open-source software. Full nodes with sufficient delegated governance tokens participate in block building as validators.

The software repository is: https://github.com/dydxprotocol/v4-chain/

## Limit Order Book
Each full node in the network maintains an in-memory order book, which undergoes state changes in real time as traders submit order instructions.

Block proposers use trades from their local order book to build blocks, with matches generated by price-time priority. Since message arrival order varies between nodes, the order book may differ across the network at any given point in time. To address this, upon seeing a new consensus-commited block, nodes sync their local books with the block contents.

Clients can subscribe to a node's book state using the [Full Node Streaming API](./api_integration-full-node-streaming.md).

## Matching and Block Processing

The order matching logic is broadly similar to centralized exchanges, with some key differences:

1. On receiving a cancel instruction:
    - The node cancels the order unless it's already matched locally.
    - The cancel instruction is stored until it expires (based on the [GTB field](https://github.com/dydxprotocol/v4-chain/blob/4780b4cba2cab75e0af5675c3e87e551162ecf33/proto/dydxprotocol/clob/tx.proto#L90)).

2. On receiving an order:
    - The order fails to place if it has already been cancelled.
    - Otherwise, it is matched and/or placed on the order book, with optimistic matches stored locally.

3. Validator nodes propose blocks that include all their local matches.

4. When processing a new block:
    - The node starts from the state of the prior block (local state used to propose is temporarily disregarded).
    - The block’s changes are applied.
    - The node replays its local state on top of the new state, during which:
        - Cancels are preserved.
        - Orders matched in the prior local state are re-placed.
        - Orders may match differently, fail to place due to cancellation, or not match at all in the new state.

#### Source Code References
For further details on how the protocol handles these actions, refer to the following source code references:

- See [here](https://github.com/dydxprotocol/v4-chain/blob/dc6e0a004fd81e3139a24f88b10605ab5ce16cfd/protocol/x/clob/ante/clob.go#L90) and [here](https://github.com/dydxprotocol/v4-chain/blob/2d5dfa55357abd5ead46f8baa03ed76d420849cc/protocol/x/clob/memclob/memclob.go#L103) for how the protocol reacts when (1) a cancel is seen.

- When (2) [an order is placed](https://github.com/dydxprotocol/v4-chain/blob/dc6e0a004fd81e3139a24f88b10605ab5ce16cfd/protocol/x/clob/ante/clob.go#L132) and [checked to not be already cancelled](https://github.com/dydxprotocol/v4-chain/blob/749dff9cbca56eb2a6ab3a19feeb338de8db80e6/protocol/x/clob/keeper/orders.go#L780).

- When (3) [proposing a block](https://github.com/dydxprotocol/v4-chain/blob/189b11217490aa5a87a4108dde0f679b0190511b/protocol/app/prepare/prepare_proposal.go#L157).

- And (4) when [nodes process blocks committed by consensus](https://github.com/dydxprotocol/v4-chain/blob/4780b4cba2cab75e0af5675c3e87e551162ecf33/protocol/x/clob/abci.go#L152).

## Order Messages

Order instructions are limit order placements, replacements, and cancellations.

> Note: This section covers short-term orders which live off-chain, in node memory, until matched.
> 
> Stateful orders (on-chain, consensus-speed placement) exist for longer-lived limit orders but aren't recommended for API traders.
> More info: [Short-term vs Stateful Orders](./api_integration-trading/short_term_vs_stateful.mdx)


### Finality and GTB
Each limit order placement or cancellation [includes a GTB (good-til-block) field](https://github.com/dydxprotocol/v4-chain/blob/dc6e0a004fd81e3139a24f88b10605ab5ce16cfd/proto/dydxprotocol/clob/order.proto#L114-L146), which specifies the block height after which the instruction expires.

While rare, it is possible for a cancel instruction to be seen by the current block proposer but not by one or more subsequent proposers (if the instruction isn't gossiped to them in time through the p2p network). In such cases, the order could still match after the sender expects it to have been cancelled.

Therefore, we recommend that API traders consider setting tight GTB values on order placements (e.g. the current chain height + 3) because expiry due to GTB is the only guaranteed way for an order to become unfillable. Consensus does not permit any order to fill at a height greater than its GTB.

### Replacements

We recommend using replacement instructions over cancelling and placing new orders.

Replacing prevents accidental double-fills that can occur with a ‘place order A, cancel order A, place order B’ approach, where both A and B might fill simultaneously unless the chain height has already passed A’s GTB.

For example, after the following messages are sent:
1. Place A: Sell 1 @ $100, client id = 123
2. Cancel A
3. Place B: Sell 1 @ $101, client id = 456

If a proposer sees messages 1 and 3, but not 2, it sees both orders A and B as open. If it also sees marketable bids for qty >= 2, both could fill simultaneously.

#### Replacement Instruction Fields

To replace an order, send a placement with the same order ID **and a larger GTB value**.

Orders have the same ID if these client-specified fields match ([OrderId proto definition](https://github.com/dydxprotocol/v4-chain/blob/dcd2d9c2f6170bd19218d92cf6f2f88216b2ffe1/proto/dydxprotocol/clob/order.proto#L9-L41)):
- [Subaccount ID](https://github.com/dydxprotocol/v4-chain/blob/dcd2d9c2f6170bd19218d92cf6f2f88216b2ffe1/proto/dydxprotocol/subaccounts/subaccount.proto#L10-L17) (owner: signing address, number: 0 unless different subaccount)
- Client ID
- Order flags (0 for short-term orders)
- CLOB pair ID


# File: v4-documentation/old-docs/pages/index.md

# dYdX Chain Documentation

Welcome to the dYdX Chain documentation! This is the source of truth for information about dYdX Chain.

> The terms "dYdX Chain" and "dYdX v4 software" are synonymous. They both refer to the same product, called dYdX Chain in this documentation.

## About dYdX

dYdX Chain is an open-source application specific blockchain software that can power a decentralized perpetuals exchange. This standalone blockchain software is open-sourced by dYdX Trading Inc. (“dYdX”) and is based on the Cosmos SDK and CometBFT proof-of-stake consensus protocol. dYdX Chain is fully decentralized end-to-end, including its consensus mechanism, order-book, matching engine and front end.

dYdX does not control any aspects of any public deployments of dYdX Chain. Any use of dYdX Chain is subject to the [v4 Terms of Use](https://dydx.exchange/v4-terms). You can read more about v4 software in our blog post [here](https://dydx.exchange/blog/dydx-chain).

## A Note on Network Examples
Parameters included in code examples throughout this documentation are for the dYdX Chain Testnet. These parameters need to be updated to access any specific deployment of dYdX Chain. In each relevant code snippet, please see the comments to pull the relevant parameters to access an applicable mainnet deployment of dYdX Chain, such as the following deployment:

| Name of Provider               | URL | Status Page     |
| ------------------------ | -------- | --------- |
| dYdX Operations Services Ltd.             | [dydx.trade](https://dydx.trade)       | https://status.dydx.trade |


_**Terms and Conditions:** All of the above third parties are independent from and unaffiliated with dYdX Trading Inc. (”dYdX”), and dYdX is not responsible for any action taken by such third parties, including content set forth on any third-party websites, such as any links to such content on this page. dYdX services and products are not available to persons or entities who reside in, are located in, are incorporated in, or have registered offices in the U.S. or Canada, or Restricted Persons (as defined in the dYdX [Terms of Use](https://dydx.exchange/terms)). The content provided herein does not constitute, and should not be considered, or relied upon as, financial advice, legal advice, tax advice, investment advice or advice of any other nature, and you agree that you are responsible to conduct independent research, perform due diligence and engage a professional advisor prior to taking any financial, tax, legal or investment action related to the foregoing content. The information contained herein, and any use of v4 software, are subject to the [v4 Terms of Use](https://dydx.exchange/v4-terms)._


# File: v4-documentation/old-docs/pages/introduction-getting_started.md

## Depositing

**Depositing on dYdX Chain**

1. Connect your preferred wallet to the dYdX Chain deployment of your choice (e.g. the dYdX Operations Services Ltd. deployment [dydx.trade](https://dydx.trade)).
2. Deposit USDC to your dYdX Chain address. The default onboarding path uses Circle's Cross Chain Transfer Protocol (CCTP) on Noble Chain. You can deposit USDC from many origination chains. Read more [here](https://dydx.exchange/blog/cctp).

## User Journeys

**Trading via API**

Currently, dYdX natively hosts a TypeScript client. 3rd parties were also commissioned to build working Python and C++ clients. All clients are hosted in the [dydxprotocol/v4-clients](https://github.com/dydxprotocol/v4-clients) repo.

| Client Type                                                                     | Quickstart Guide                                                                                              | Built By          |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ----------------- |
| [TypeScript](https://github.com/dydxprotocol/v4-clients/tree/main/v4-client-js) | [Getting Started with the TS Client](./api_integration-guides/Getting_started_with_the_typescript_client.mdx) | dYdX Trading Inc. |
| [Python](https://github.com/dydxprotocol/v4-clients/tree/main/v4-client-py-v2)  |                                                                                                               | Nethermind        |
| [C++](https://github.com/dydxprotocol/v4-clients/tree/main/v4-client-cpp)       |                                                                                                               | FastForward       |

**Trading via Web**

| Deployment | Web App Site                                                  | Deployed By                   |
| ---------- | ------------------------------------------------------------- | ----------------------------- |
| Mainnet    | [dydx.trade](https://dydx.trade)                              | dYdX Operations Services Ltd. |
| Testnet    | [v4.testnet.dydx.exchange](https://v4.testnet.dydx.exchange/) | dYdX Trading Inc.             |

**Trading via Mobile**

| Platform       | Link                                                                 | Deployed By                   |
| -------------- | -------------------------------------------------------------------- | ----------------------------- |
| iOS            | https://apps.apple.com/bg/app/dydx/id6475599596                      | dYdX Operations Services Ltd. |
| Android (Beta) | https://play.google.com/store/apps/details?id=trade.opsdao.dydxchain | dYdX Operations Services Ltd. |

_dYdX Trading Inc. ("dYdX") does not control or operate any public deployments of dYdX Chain. Any use of the dYdX Chain documentation hub and dYdX Chain software is subject to dYdX's [Terms and Policies](./other-terms_of_use_and_privacy_policy.md#native-token-denom)._


# File: v4-documentation/old-docs/pages/introduction-trading_fees.md

# Trading Fees

The dYdX Chain uses a tiered fee structure based on 30-day trailing trading volume.

| Tier | 30d Trailing Volume                   | Taker (bps) | Maker (bps) |
| ---- | ------------------------------------- | ----------- | ----------- |
| 1    | < $1M                                 | 5.0         | 1.0         |
| 2    | ≥ $1M                                 | 4.5         | 1.0         |
| 3    | ≥ $5M                                 | 4.0         | 0.5         |
| 4    | ≥ $25M                                | 3.5         | —           |
| 5    | ≥ $125M                               | 3.0         | —           |
| 6    | ≥ $125M and ≥0.5% exchange mkt. share | 2.5         | -0.5        |
| 7    | ≥ $125M and ≥1% maker mkt. share      | 2.5         | -0.7        |
| 8    | ≥ $125M and ≥2% maker mkt. share      | 2.5         | -0.9        |
| 9    | ≥ $125M and ≥4% maker mkt. share      | 2.5         | -1.1        |

> Negative maker fees represent rebates where traders earn a percentage of the notional value when providing liquidity as makers.

- **Taker Fees**: Applied when you remove liquidity from the order book (market orders, limit orders that cross the spread)
- **Maker Fees/Rebates**: Applied when you add liquidity to the order book (limit orders that don't cross the spread)
- **Volume Calculation**: Includes trading activity across all your subaccounts and markets

## Onchain Parameters

Fee tiers are set by governance and can be queried from a full node with the `/dydxprotocol/v4/feetiers/perpetual_fee_params` RPC endpoint.

For example:

https://dydx-ops-rest.kingnodes.com/dydxprotocol/v4/feetiers/perpetual_fee_params

## More Info

For more detailed information about trading rewards, fee structures, and parameters, please see the [Rewards, Fees and Parameters](./concepts-trading/rewards_fees_and_parameters.md) section.


# File: v4-documentation/old-docs/pages/other-security.md

# Security

## Independent Audits

The protocol has been audited by the [Informal Systems](https://informal.systems/) team. Additional audits are planned as more protocol code is developed.

You can find all finalized audit reports in the [v4_chain audits folder](https://github.com/dydxprotocol/v4-chain/tree/main/audits).

## Bug Bounty

With all core dYdX Chain (v4) software GitHub repos now made public, we are inviting the community to help us identify any vulnerabilities to improve the security of dYdX Chain.

To find more details, please see our blog post [here](https://dydx.exchange/blog/dydx-bug-bounty-program)!


# File: v4-documentation/old-docs/pages/other-terms_of_use_and_privacy_policy.md

# Terms-of-Use & Privacy Policy

By using, recording, referencing, or downloading (i.e., any “action”) any information contained on this page or in any dYdX Trading Inc. ("dYdX") database or documentation, you hereby and thereby agree to the [v4 Terms of Use](https://dydx.exchange/v4-terms) and [Privacy Policy](https://dydx.exchange/privacy) governing such information, and you agree that such action establishes a binding agreement between you and dYdX.

This documentation provides information on how to use dYdX v4 software (”dYdX Chain”). dYdX does not deploy or run v4 software for public use, or operate or control any dYdX Chain infrastructure. dYdX is not responsible for any actions taken by other third parties who use v4 software. dYdX services and products are not available to persons or entities who reside in, are located in, are incorporated in, or have registered offices in the United States or Canada, or Restricted Persons (as defined in the dYdX [Terms of Use](https://dydx.exchange/terms)). The content provided herein does not constitute, and should not be construed, or relied upon as, financial advice, legal advice, tax advice, investment advice or advice of any other nature, and you agree that you are responsible to conduct independent research, perform due diligence and engage a professional advisor prior to taking any financial, tax, legal or investment action related to the foregoing content. The information contained herein, and any use of v4 software, are subject to the [v4 Terms of Use](https://dydx.exchange/v4-terms).


# File: v4-documentation/old-docs/pages/users-faqs.md

# User Submitted Questions and Answers

Since the inception of dYdX Chain, we have been compiling a list of questions and answers from users related to technical support. We turned this list into a live _v4 Telegram Questions_ document, which should be able to answer many of your more nuanced questions.

It's a large document, so we recommend CTRL+F to find key words. 

You can anonymously access the live document with [this link](https://docs.google.com/document/d/1QZE5aemQ1lzBN_2RA8-tTVk5JVQ_fNNB4VeSEWKWl8w/edit?usp=sharing).


# File: v4-documentation/old-docs/pages/api_integration-trading/isolated_markets.md

# Isolated Markets

In v5.0.0 the Isolated Markets feature was added to the V4 chain software. The below is an overview of how trading will work on Isolated Markets on the V4 chain software.

>Note: This document covers how the feature works from the protocol point of view and not the front end or the indexer. For more details on what isolated markets are see the [blog post](https://dydx.exchange/blog/introducing-isolated-markets-and-isolated-margin).

# Trading Isolated Markets

Positions in isolated markets can only be opened on a subaccount with no open perpetual positions or a subaccount with an existing perpetual position in the same isolated market. Once a perpetual position for an isolated market is opened on a subaccount, no positions in any other markets can be opened until the perpetual position is closed.

The above restriction only applies to positions, orders can still be placed for different markets on a subaccount while it holds an open position for an isolated market. The orders will fail and be canceled when they match if the subaccount still holds an open position for a different isolated market. A new [error code](https://github.com/dydxprotocol/v4-chain/blob/protocol/v5.0.0/protocol/x/clob/types/errors.go#L364-L368) `2005` has been added to indicate such a failure.

Other than the above caveat, isolated markets can be traded in the same way as before v5.0.0. 

>Note: The maximum number of subaccounts per address was increased from 127 to 128000 in v5.0.0 to address the need for a separate subaccount per isolated market.


# Querying for Isolated Markets

There is a new `market_type` parameter in the `PerpetualParams` proto struct that indicates the type of market. 

There are 2 possible values for this parameter:

- `PERPETUAL_MARKET_TYPE_CROSS` - markets where subaccounts can have positions cross-margined with other `PERPETUAL_MARKET_TYPE_CROSS` markets, all markets created before the v5.0.0 upgrade are `PERPETUAL_MARKET_TYPE_CROSS` markets
- `PERPETUAL_MARKET_TYPE_ISOLATED` - markets that can only be margined in isolated, no cross-margining with other markets is possible

An example of how each type of market looks when queried using the `/dydxprotocol/perpetuals/perpetual/:id` REST endpoint.

- `PERPETUAL_MARKET_TYPE_CROSS`

```json
{
  "perpetual": {
    "params": {
      "id": 1,
      "ticker": "ETH-USD",
      "market_id": 1,
      "atomic_resolution": -9,
      "default_funding_ppm": 0,
      "liquidity_tier": 0,
      "market_type": "PERPETUAL_MARKET_TYPE_CROSS"
    },
    "funding_index": "0",
    "open_interest": "0"
  }
}
```

- `PERPETUAL_MARKET_TYPE_ISOLATED`

```json
{
  "perpetual": {
    "params": {
      "id": 1,
      "ticker": "FLOKI-USD",
      "market_id": 37,
      "atomic_resolution": -13,
      "default_funding_ppm": 0,
      "liquidity_tier": 2,
      "market_type": "PERPETUAL_MARKET_TYPE_ISOLATED"
    },
    "funding_index": "0",
    "open_interest": "0"
  }
}
```


# File: v4-documentation/old-docs/pages/api_integration-trading/order_types.md

# Order Execution Options

## [Time In Force](https://github.com/dydxprotocol/v4-chain/blob/aefa183b759efe62a53c0fbbb23d97d8095868e9/proto/dydxprotocol/clob/order.proto#L159)
Execution options can be specified using the `TimeInForce` field for order placements.

### Unspecified/Empty
Leaving order execution as unspecified/empty represents the default behavior where an order will first match with existing orders on the book, and any remaining size will be added to the book as a maker order.

### Immediate or Cancel Order (IOC)
IOC enforces that an order only be matched with maker orders on the book. If the order has remaining size after matching with existing orders on the book, the remaining size is not placed on the book.

### Post Only
Post only enforces that an order only be placed on the book as a maker order. Note this means that validators will cancel any newly-placed post only orders that would cross with other maker orders.

## [Reduce Only Order (RO)](https://github.com/dydxprotocol/v4-chain/blob/aefa183b759efe62a53c0fbbb23d97d8095868e9/proto/dydxprotocol/clob/order.proto#L189)

*Reduce only orders are currently only enabled on FOK/IOC orders as of right now.*

Reduce Only orders are a type of order that can only reduce your position size. For example, a 1.25 BTC Sell Reduce Only order on a 1 BTC long can only decrease your position size by 1. The remaining .25 BTC sell will not fill and be cancelled. Reduce Only orders are used to close out your positions.

## [Condition Types](https://github.com/dydxprotocol/v4-chain/blob/aefa183b759efe62a53c0fbbb23d97d8095868e9/proto/dydxprotocol/clob/order.proto#L195)

### Unspecified
Unspecified represents the default behavior where an order will be placed immediately on the orderbook.

### Stop Loss
Stop loss represents a stop order. A stop order will trigger when the oracle price moves at or above the trigger price for buys, and at or below the trigger price for sells.

### Take Profit
Take profit represents a take profit order. A take profit order will trigger when the oracle price moves at or below the trigger price for buys and at or above the trigger price for sells.


# File: v4-documentation/old-docs/pages/api_integration-trading/other_limits.md

## Other Limits

Subaccounts have a limited number of stateful open orders at any one time determined by the net collateral of the subaccount.

These limits are subject to governance. The latest limits can be queried via the `https://<REST_NODE_ENDPOINT>/dydxprotocol/clob/equity_tier` endpoint.

Here is an example response:

```
{
  "equity_tier_limit_config": {
    "stateful_order_equity_tiers": [
      {
        "usd_tnc_required": "0",
        "limit": 0
      },
      {
        "usd_tnc_required": "20000000",
        "limit": 4
      },
      {
        "usd_tnc_required": "100000000",
        "limit": 8
      },
      {
        "usd_tnc_required": "1000000000",
        "limit": 10
      },
      {
        "usd_tnc_required": "10000000000",
        "limit": 100
      },
      {
        "usd_tnc_required": "100000000000",
        "limit": 200
      }
    ]
  }
}
```

Read as:

| Net Collateral | Long-term or Conditional orders |
| -------------- |  ------------------------------- |
| < $20          |  0                               |
| >= $20 and < $100         |  4                               |
| >= $100 and < $1,000       |  8                               |
| >= $1,000 and < $10,000      |  10                              |
| >= $10,000 and < $100,000     |  100                             |
| >= $100,000      |  200                             |

For example up to 10 open bids across all markets for a subaccount with a net collateral of $2,000.

Note:
- Short term orders, including limit `Immediate-or-Cancel`, `Fill-or-Kill`, and market orders on the frontend do not have this limitation.
- Only the `stateful_order_equity_tiers` field is in effect -- short term order equity limits under the `short_term_order_equity_tiers` key are no longer in effect.


# File: v4-documentation/old-docs/pages/api_integration-trading/rate_limits.md

## Rate Limits

All rate limits are subject to change. The latest limits can be queried via the `https://<REST_NODE_ENDPOINT>/dydxprotocol/clob/block_rate` endpoint.

Note that rate limits are applied per account. That is, subaccounts under the same account share the same rate limit.

Here is an example response:

```
{
    "block_rate_limit_config": {
        "max_short_term_orders_per_n_blocks": [],
        "max_stateful_orders_per_n_blocks": [
            {
                "num_blocks": 1,
                "limit": 2
            },
            {
                "num_blocks": 100,
                "limit": 20
            }
        ],
        "max_short_term_order_cancellations_per_n_blocks": [],
        "max_short_term_orders_and_cancels_per_n_blocks": [
            {
                "num_blocks": 5,
                "limit": 2000
            }
        ]
    }
}
```

### Active Fields

`max_stateful_orders_per_n_blocks`: How many stateful order **place** attempts (successful and failed) are allowed for an account per N blocks. Note that the rate limits are applied in an AND fashion such that an order placement must pass all rate limit configurations.

`max_short_term_orders_and_cancels_per_n_blocks`: How many short term order **place and cancel** attempts (successful and failed) are allowed for an account per N blocks. Note that the rate limits are applied in an AND fashion such that an order placement must pass all rate limit configurations.

### Deprecated Fields

These fields are not used at this time.

`max_short_term_order_cancellations_per_n_blocks`
`max_short_term_orders_per_n_blocks`

### Examples

Examples assume the values in the provided example response.

- 2 long-term orders can be placed for each of the first 10 blocks and then a new long-term order would be rate limited on the 11th block since the limit of 20 long-term orders over the past 100 blocks would apply.


# File: v4-documentation/old-docs/pages/api_integration-indexer/indexer_websocket.md

# Indexer Websocket Documentation

dYdX offers a WebSocket API for streaming v4 updates.

* For **the deployment by DYDX token holders**, use `wss://indexer.dydx.trade/v4/ws`
* For **Testnet**, use `wss://indexer.v4testnet.dydx.exchange/v4/ws`

Note: Messages on Indexer WebSocket feeds are typically more recent than data fetched via Indexer's REST API, because the latter is backed by read replicas of the databases that feed the former. Ordinarily this difference is minimal (less than a second), but it might become prolonged under load. Please see [Indexer Architecture](https://dydx.exchange/blog/v4-deep-dive-indexer) for more information.

## Overall

### Connect

Upon connecting to v4 Websockets you will receive an initial connection message with the following format:

```tsx
{
  "type": "connected",
  "connection_id": "004a1efa-21bb-4b19-a2e9-a8ffadd6dc53",
  "message_id": 0
}
```

### Maintaining a Connection

Every 30 seconds, the websocket API will send a [heartbeat ping control frame](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API/Writing_WebSocket_servers#pings_and_pongs_the_heartbeat_of_websockets) to the connected client. If a pong event is not received within 10 seconds back, the websocket API will disconnect.

### Subscribe

You may subscribe to any channel following the subscribe instructions above. Subscribing to a channel has the following fields:

- `type` - Should always be specified to `subscribe`
- `channel` - Specifies the channel you are subscribing to. The specific string is specified in each channel’s documentation
- `id` - required for all channels other than market. Specifies the market or subaccount you are subscribing to.

### Rate Limiting

The default rate limiting config for websockets is:
- 2 subscriptions per (connection + channel + channel id) per second.
- 2 invalid messages per connection per second.

### Unsubscribe

Utilize the same message to subscribe but replace the type with `unsubscribe`. For example:
`{ "type": "unsubscribe", "channel": "v4_trades", "id": "BTC-USD" }`

### Example

Use a command-line websocket client such as [interactive-websocket-cli](https://www.npmjs.com/package/interactive-websocket-cli) to connect and subscribe to channels.

Example (with `interactive-websocket-cli`)

```tsx
# For the deployment by DYDX token holders, use
# wscli connect wss://indexer.dydx.trade/v4/ws
wscli connect wss://indexer.v4testnet.dydx.exchange/v4/ws
<output from ws-cli>
<type 's' to send> { "type": "subscribe", "channel": "v4_trades", "id": "BTC-USD" }
```

## Subaccounts

This channel provides realtime information about orders, fills, transfers, perpetual positions, and perpetual assets for a subaccount.

### Subscribe

| Field | Type | Description |
| --- | --- | --- |
| type | string | Set to subscribe |
| channel | string | Set to v4_subaccounts |
| id | string | Set to the address and subaccount number in the format {address}/{subaccount_number} |

### Initial Response

Returns everything from the `/v4/addresses/:address/subaccountNumber/:subaccountNumber`, and `/v4/orders?addresses=${address}&subaccountNumber=${subaccountNumber}&status=OPEN`.

### Example
```tsx
{
  "type": "subscribed",
  "connection_id": "c5a28fa5-c257-4fb5-b68e-fe084c2768e5",
  "message_id": 1,
  "channel": "v4_subaccounts",
  "id": "dydx199tqg4wdlnu4qjlxchpd7seg454937hjrknju4/0",
  "contents": {
    "subaccount": {
      "address": "dydx199tqg4wdlnu4qjlxchpd7seg454937hjrknju4",
      "subaccountNumber": 0,
      "equity": "100000000000.000000",
      "freeCollateral": "100000000000.000000",
      "openPerpetualPositions": {},
      "assetPositions": {
        "USDC": {
          "symbol": "USDC",
          "side": "LONG",
          "size": "100000000000",
          "assetId": "0"
        }
      },
      "marginEnabled": true
    },
    "orders": []
  }
}
```


### Channel Data

Subsequent responses will contain any update to open orders, changes in account, changes in open positions, and/or transfers in a single message.

```tsx
export interface SubaccountsChannelData {
	channel: 'v4_trades',
	id: string,
	contents: SubaccountMessageContents,
	blockHeight: string,
	transactionIndex: number,
	eventIndex: number,
	clobPairId: string,
	version: string,
}

export interface SubaccountMessageContents {
	// Perpetual position updates on the subaccount
  perpetualPositions?: PerpetualPositionSubaccountMessageContents[],
	// Asset position updates on the subaccount
  assetPositions?: AssetPositionSubaccountMessageContents[],
	// Order updates on the subaccount
  orders?: OrderSubaccountMessageContents[],
	// Fills that occur on the subaccount
  fills?: FillSubaccountMessageContents[],
	// Transfers that occur on the subaccount
  transfers?: TransferSubaccountMessageContents,
}

export interface PerpetualPositionSubaccountMessageContents {
  address: string,
  subaccountNumber: number,
  positionId: string,
  market: string,
  side: PositionSide,
  status: PerpetualPositionStatus,
  size: string,
  maxSize: string,
  netFunding: string,
  entryPrice: string,
  exitPrice?: string,
  sumOpen: string,
  sumClose: string,
  realizedPnl?: string,
  unrealizedPnl?: string,
}

export enum PositionSide {
  LONG = 'LONG',
  SHORT = 'SHORT',
}

export enum PerpetualPositionStatus {
  OPEN = 'OPEN',
  CLOSED = 'CLOSED',
  LIQUIDATED = 'LIQUIDATED',
}

export interface AssetPositionSubaccountMessageContents {
  address: string,
  subaccountNumber: number,
  positionId: string,
  assetId: string,
  symbol: string,
  side: PositionSide,
  size: string,
}

export interface OrderSubaccountMessageContents {
  id: string;
  subaccountId: string;
  clientId: string;
  clobPairId: string;
  side: OrderSide;
  size: string;
  ticker: string,
  price: string;
  type: OrderType;
  timeInForce: APITimeInForce;
  postOnly: boolean;
  reduceOnly: boolean;
  status: APIOrderStatus;
  orderFlags: string;
  totalFilled?: string;
  totalOptimisticFilled?: string;
  goodTilBlock?: string;
  goodTilBlockTime?: string;
  removalReason?: string;
  createdAtHeight?: string;
  clientMetadata: string;
  triggerPrice?: string;
  updatedAt?: IsoString;
  updatedAtHeight?: string;
}

export enum OrderSide {
  BUY = 'BUY',
  SELL = 'SELL',
}

export enum OrderType {
  LIMIT = 'LIMIT',
  MARKET = 'MARKET',
  STOP_LIMIT = 'STOP_LIMIT',
  STOP_MARKET = 'STOP_MARKET',
  TRAILING_STOP = 'TRAILING_STOP',
  TAKE_PROFIT = 'TAKE_PROFIT',
  TAKE_PROFIT_MARKET = 'TAKE_PROFIT_MARKET',
}

export enum APITimeInForce {
  // GTT represents Good-Til-Time, where an order will first match with existing orders on the book
  // and any remaining size will be added to the book as a maker order, which will expire at a
  // given expiry time.
  GTT = 'GTT',
  // FOK represents Fill-Or-KILl where it's enforced that an order will either be filled
  // completely and immediately by maker orders on the book or canceled if the entire amount can't
  // be filled.
  FOK = 'FOK',
  // IOC represents Immediate-Or-Cancel, where it's enforced that an order only be matched with
  // maker orders on the book. If the order has remaining size after matching with existing orders
  // on the book, the remaining size is not placed on the book.
  IOC = 'IOC',
}

export enum APIOrderStatus {
  OPEN = 'OPEN',
  FILLED = 'FILLED',
  CANCELED = 'CANCELED',
  BEST_EFFORT_CANCELED = 'BEST_EFFORT_CANCELED',
  BEST_EFFORT_OPENED = 'BEST_EFFORT_OPENED',
  UNTRIGGERED = "UNTRIGGERED"
}

export interface FillSubaccountMessageContents {
  id: string;
  subaccountId: string;
  side: OrderSide;
  liquidity: Liquidity;
  type: FillType;
  clobPairId: string;
  size: string;
  price: string;
  quoteAmount: string;
  eventId: string,
  transactionHash: string;
  createdAt: IsoString;
  createdAtHeight: string;
  orderId?: string;
  ticker: string;
}

export enum Liquidity {
  TAKER = 'TAKER',
  MAKER = 'MAKER',
}

export enum FillType {
  // LIMIT is the fill type for a fill with a limit taker order.
  LIMIT = 'LIMIT',
  // LIQUIDATED is for the taker side of the fill where the subaccount was liquidated.
  // The subaccountId associated with this fill is the liquidated subaccount.
  LIQUIDATED = 'LIQUIDATED',
  // LIQUIDATION is for the maker side of the fill, never used for orders
  LIQUIDATION = 'LIQUIDATION',
  // DELEVERAGED is for the subaccount that was deleveraged in a deleveraging event.
  // The fill type will be set to taker.
  DELEVERAGED = 'DELEVERAGED',
  // OFFSETTING is for the offsetting subaccount in a deleveraging event.
  // The fill type will be set to maker.
  OFFSETTING = 'OFFSETTING',
}

export enum TradeType {
  // LIMIT is the trade type for a fill with a limit taker order.
  LIMIT = 'LIMIT',
  // LIQUIDATED is the trade type for a fill with a liquidated taker order.
  LIQUIDATED = 'LIQUIDATED',
  // DELEVERAGED is the trade type for a fill with a deleveraged taker order.
  DELEVERAGED = 'DELEVERAGED',
}

export interface TransferSubaccountMessageContents {
  sender: {
    address: string,
    subaccountNumber?: number,
  },
  recipient: {
    address: string,
    subaccountNumber?: number,
  },
  symbol: string,
  size: string,
  type: TransferType,
  createdAt: IsoString,
  createdAtHeight: string,
  transactionHash: string,
}

export enum TransferType {
  TRANSFER_IN = 'TRANSFER_IN',
  TRANSFER_OUT = 'TRANSFER_OUT',
  DEPOSIT = 'DEPOSIT',
  WITHDRAWAL = 'WITHDRAWAL',
}

```

### Example

```tsx
{
  "type": "channel_data",
  "connection_id": "a00edbe8-095a-4da1-8a9d-ff1f91467258",
  "message_id": 4,
  "id": "dydx1zsw8fczav25uvc8rg3zcv6zy9j7yhnktpq374m/0",
  "channel": "v4_subaccounts",
  "version": "2.1.0",
  "contents": {
    "orders": [
      {
        "id": "64fe30a2-006d-5108-a156-cb0c8443546c",
        "side": "BUY",
        "size": "1",
        "totalFilled": "1",
        "price": "1948.65",
        "type": "LIMIT",
        "status": "FILLED",
        "timeInForce": "IOC",
        "reduceOnly": false,
        "orderFlags": "0",
        "goodTilBlock": "61186",
        "goodTilBlockTime": null,
        "postOnly": false,
        "ticker": "ETH-USD"
      }
    ],
    "fills": [
      {
        "id": "c5030bd3-cd85-5046-8f2a-518bbba6ec45",
        "subaccountId": "db535c19-b298-5ee8-bb59-e96c659a8bd4",
        "side": "BUY",
        "liquidity": "TAKER",
        "type": "LIMIT",
        "clobPairId": "1",
        "orderId": "64fe30a2-006d-5108-a156-cb0c8443546c",
        "size": "1",
        "price": "1854.25",
        "quoteAmount": "1854.25",
        "eventId": {
          "type": "Buffer",
          "data": [
            0,
            0,
            238,
            241,
            0,
            0,
            0,
            2,
            0,
            0,
            0,
            77
          ]
        },
        "transactionHash": "C84B0BBCA8E713A2D46EFBA07F2D0A32C1F6E2440794A366B888503935E0EF40",
        "createdAt": "2023-04-04T19:09:24.869Z",
        "createdAtHeight": "61169",
        "ticker": "ETH-USD"
      }
    ]
  }
}
```


## Orderbooks

### Subscribe

| Field | Type | Description |
| --- | --- | --- |
| type | string | Set to subscribe |
| channel | string | Set to v4_orderbook |
| id | string | Set to the ticker of the market you would like to subscribe to. For example, BTC-USD |

### Initial Response

Returns everything from `v4/orderbooks/perpetualMarkets/${id}` endpoint.

- Example

    ```tsx
    {
      "type": "subscribed",
      "connection_id": "ee5a4696-dce8-44ef-8d68-f0e0d0b06160",
      "message_id": 2,
      "channel": "v4_orderbook",
      "id": "BTC-USD",
      "contents": {
        "bids": [
          {
            "price": "28194",
            "size": "4.764826096"
          },
          {
            "price": "28193",
            "size": "3.115323739"
          },
          {
            "price": "28192",
            "size": "3.400340775"
          },
          {
            "price": "28191",
            "size": "3.177700682"
          },
          {
            "price": "28190",
            "size": "3.055502176"
          },
          {
            "price": "28189",
            "size": "3.672892171"
          },
          {
            "price": "28188",
            "size": "3.597672948"
          },
          {
            "price": "28187",
            "size": "2.561597964"
          },
          {
            "price": "28186",
            "size": "3.070490554"
          },
          {
            "price": "28185",
            "size": "3.550128411"
          },
          {
            "price": "28184",
            "size": "4.213369101"
          },
          {
            "price": "28183",
            "size": "3.608880877"
          },
    		],
    		"asks": [
          {
            "price": "28195",
            "size": "3.219612343"
          },
          {
            "price": "28196",
            "size": "2.387087565"
          },
          {
            "price": "28197",
            "size": "2.698530469"
          },
          {
            "price": "28198",
            "size": "2.590884421"
          },
          {
            "price": "28199",
            "size": "3.192796678"
          },
    		],
    	},
    }
    ```


### Channel Data

```tsx
interface OrderbookChannelData {
	channel: 'v4_orderbook',
	id: string,
	contents: OrderbookMessageContents,
	clobPairId: string,
	version: string,
}

interface OrderbookMessageContents {
  bids?: PriceLevel[],
  asks?: PriceLevel[],
}

// The first string indicates the price, the second string indicates the size
type PriceLevel = [string, string];
```

- Example

    ```tsx
    {
      "type": "channel_data",
      "connection_id": "ee5a4696-dce8-44ef-8d68-f0e0d0b06160",
      "message_id": 484,
      "id": "BTC-USD",
      "channel": "v4_orderbook",
      "version": "0.0.1",
      "contents": {
        "bids": [
          [
            "27773",
            "1.986168516"
          ]
        ]
      }
    }
    ```


## Trades

### Subscribe

| Field | Type | Description |
| --- | --- | --- |
| type | string | Set to subscribe |
| channel | string | Set to v4_trades |
| id | string | Set to the ticker of the market you would like to subscribe to. For example, BTC-USD |

### Initial Response

Returns everything from `v4/trades/perpetualMarkets/${id}` endpoint.

- Example

    ```tsx
    {
      "type": "subscribed",
      "connection_id": "57844645-0b1d-4c3f-ad71-1c6154154a13",
      "message_id": 1,
      "channel": "v4_trades",
      "id": "BTC-USD",
      "contents": {
        "trades": [
          {
            "side": "BUY",
            "size": "0.00396135",
            "price": "27848",
            "createdAt": "2023-04-04T00:28:56.226Z",
            "createdAtHeight": "49592"
          },
          {
            "side": "SELL",
            "size": "0.000019216",
            "price": "27841",
            "createdAt": "2023-04-04T00:28:56.226Z",
            "createdAtHeight": "49592"
          },
          {
            "side": "SELL",
            "size": "0.001682908",
            "price": "27840",
            "createdAt": "2023-04-04T00:28:56.226Z",
            "createdAtHeight": "49592"
          },
          {
            "side": "SELL",
            "size": "0.000311013",
            "price": "27840",
            "createdAt": "2023-04-04T00:28:56.226Z",
            "createdAtHeight": "49592"
          },
          {
            "side": "SELL",
            "size": "0.000000011",
            "price": "27842",
            "createdAt": "2023-04-04T00:28:56.226Z",
            "createdAtHeight": "49592"
          },
          {
            "side": "SELL",
            "size": "0.000000017",
            "price": "27842",
            "createdAt": "2023-04-04T00:28:56.226Z",
            "createdAtHeight": "49592"
          },
          {
            "side": "SELL",
            "size": "0.000226026",
            "price": "27842",
            "createdAt": "2023-04-04T00:28:56.226Z",
            "createdAtHeight": "49592"
          },
          {
            "side": "SELL",
            "size": "0.000000004",
            "price": "27842",
            "createdAt": "2023-04-04T00:28:56.226Z",
            "createdAtHeight": "49592"
          },
          {
            "side": "SELL",
            "size": "0.000000006",
            "price": "27842",
            "createdAt": "2023-04-04T00:28:56.226Z",
            "createdAtHeight": "49592"
          },
          {
            "side": "SELL",
            "size": "0.000226015",
            "price": "27842",
            "createdAt": "2023-04-04T00:28:56.226Z",
            "createdAtHeight": "49592"
          },
          {
            "side": "SELL",
            "size": "0.000003739",
            "price": "27842",
            "createdAt": "2023-04-04T00:28:56.226Z",
            "createdAtHeight": "49592"
          },
          {
            "side": "SELL",
            "size": "0.000164144",
            "price": "27842",
            "createdAt": "2023-04-04T00:28:56.226Z",
            "createdAtHeight": "49592"
          },
          {
            "side": "BUY",
            "size": "0.037703477",
            "price": "27848",
            "createdAt": "2023-04-04T00:28:50.516Z",
            "createdAtHeight": "49591"
          },
          {
            "side": "SELL",
            "size": "0.000000321",
            "price": "27842",
            "createdAt": "2023-04-04T00:28:50.516Z",
            "createdAtHeight": "49591"
          },
          {
            "side": "SELL",
            "size": "0.06706869",
            "price": "27842",
            "createdAt": "2023-04-04T00:28:50.516Z",
            "createdAtHeight": "49591"
          },
          {
            "side": "SELL",
            "size": "0.002573305",
            "price": "27842",
            "createdAt": "2023-04-04T00:28:50.516Z",
            "createdAtHeight": "49591"
          },
          {
            "side": "SELL",
            "size": "0.001525924",
            "price": "27842",
            "createdAt": "2023-04-04T00:28:50.516Z",
            "createdAtHeight": "49591"
          },
          {
            "side": "SELL",
            "size": "0.00387205",
            "price": "27842",
            "createdAt": "2023-04-04T00:28:50.516Z",
            "createdAtHeight": "49591"
          },
          {
            "side": "SELL",
            "size": "0.000094697",
            "price": "27845",
            "createdAt": "2023-04-04T00:28:50.516Z",
            "createdAtHeight": "49591"
          },
          {
            "side": "SELL",
            "size": "0.002828331",
            "price": "27842",
            "createdAt": "2023-04-04T00:28:50.516Z",
            "createdAtHeight": "49591"
          },
          {
            "side": "SELL",
            "size": "0.000100428",
            "price": "27845",
            "createdAt": "2023-04-04T00:28:50.516Z",
            "createdAtHeight": "49591"
          },
          {
            "side": "BUY",
            "size": "0.000098184",
            "price": "27848",
            "createdAt": "2023-04-04T00:28:50.516Z",
            "createdAtHeight": "49591"
          },
        ],
    	},
    }
    ```


### Channel Data

```tsx
interface TradeChannelData {
	channel: 'v4_trades',
	id: string,
	contents: TradeMessageContents,
	blockHeight: string,
	clobPairId: string,
	version: string,
}

interface TradeMessageContents {
  trades: TradeContent[],
}

interface TradeContent {
	// Unique id of the trade, which is the taker fill id.
  id: string,
  size: string,
  price: string,
  side: string,
  createdAt: IsoString,
  type: TradeType,
}
```

### Example

```tsx
{
  "type": "channel_data",
  "connection_id": "57844645-0b1d-4c3f-ad71-1c6154154a13",
  "message_id": 4,
  "id": "BTC-USD",
  "channel": "v4_trades",
  "version": "1.1.0",
  "contents": {
    "trades": [
      {
        "id": "8ee6d90d-272d-5edd-bf0f-2e4d6ae3d3b7",
        "size": "0.000100431",
        "price": "27839",
        "side": "BUY",
        "createdAt": "2023-04-04T00:29:19.353Z",
        "type": "LIQUIDATED"
      },
      {
        "id": "38e64479-af09-5417-a795-195f83879156",
        "size": "0.000000004",
        "price": "27839",
        "side": "BUY",
        "createdAt": "2023-04-04T00:29:19.353Z",
        "type": "LIQUIDATED"
      },
      {
        "id": "d310c32c-f066-5ba8-a97d-10a29d9a6c84",
        "size": "0.000000005",
        "price": "27837",
        "side": "SELL",
        "createdAt": "2023-04-04T00:29:19.353Z",
        "type": "LIMIT"
      },
      {
        "id": "dd1088b5-5cab-518f-a59c-4d5f735ab861",
        "size": "0.000118502",
        "price": "27837",
        "side": "SELL",
        "createdAt": "2023-04-04T00:29:19.353Z",
        "type": "LIMIT"
      },
    ],
  },
}
```


## Markets

### Subscribe

| Field | Type | Description |
| --- | --- | --- |
| type | string | Set to subscribe |
| channel | string | Set to v4_markets |

### Initial Response

Returns everything from `v4/perpetualMarkets` endpoint.

### Example

```tsx
{
  "type": "subscribed",
  "connection_id": "6e0af39b-5937-459a-b7ac-cc8abe1049db",
  "message_id": 1,
  "channel": "v4_markets",
  "contents": {
    "markets": {
      "BTC-USD": {
        "clobPairId": "0",
        "ticker": "BTC-USD",
        "status": "ACTIVE",
        "baseAsset": "",
        "quoteAsset": "",
        "oraclePrice": "27752.92",
        "priceChange24H": "0",
        "volume24H": "63894023.044245577",
        "trades24H": 143820,
        "nextFundingRate": "0",
        "initialMarginFraction": "0.050000",
        "maintenanceMarginFraction": "0.030000",
        "basePositionSize": "0",
        "incrementalPositionSize": "0",
        "maxPositionSize": "0",
        "openInterest": "1891.473716288",
        "atomicResolution": -10,
        "quantumConversionExponent": -8,
        "tickSize": "1",
        "stepSize": "0.000000001",
        "stepBaseQuantums": 10,
        "subticksPerTick": 10000
      },
      "ETH-USD": {
        "clobPairId": "1",
        "ticker": "ETH-USD",
        "status": "ACTIVE",
        "baseAsset": "",
        "quoteAsset": "",
        "oraclePrice": "1808.2",
        "priceChange24H": "0",
        "volume24H": "67487133.70842158",
        "trades24H": 137552,
        "nextFundingRate": "0",
        "initialMarginFraction": "0.050000",
        "maintenanceMarginFraction": "0.030000",
        "basePositionSize": "0",
        "incrementalPositionSize": "0",
        "maxPositionSize": "0",
        "openInterest": "44027.853711",
        "atomicResolution": -9,
        "quantumConversionExponent": -9,
        "tickSize": "0.01",
        "stepSize": "0.000001",
        "stepBaseQuantums": 1000,
        "subticksPerTick": 10000
      }
    }
  }
}
```


### Channel Data

```tsx
interface MarketChannelData {
	channel: 'v4_markets',
	id: 'v4_markets',
	contents: MarketMessageContents,
	version: string,
}

interface MarketMessageContents {
  trading?: TradingMarketMessageContents,
  oraclePrices?: OraclePriceMarketMessageContentsMapping,
}

type TradingMarketMessageContents = {
  [ticker: string]: TradingPerpetualMarketMessage
};

interface TradingPerpetualMarketMessage {
  id?: string;
  clobPairId?: string;
  ticker?: string;
  marketId?: number;
  status?: PerpetualMarketStatus; // 'ACTIVE', 'PAUSED', 'CANCEL_ONLY', 'POST_ONLY', or 'INITIALIZING'
  baseAsset?: string;
  quoteAsset?: string;
  initialMarginFraction?: string;
  maintenanceMarginFraction?: string;
  basePositionSize?: string;
  incrementalPositionSize?: string;
  maxPositionSize?: string;
  openInterest?: string;
  quantumConversionExponent?: number;
  atomicResolution?: number;
  subticksPerTick?: number;
  stepBaseQuantums?: number;
  priceChange24H?: string;
  volume24H?: string;
  trades24H?: number;
  nextFundingRate?: string;
}

type OraclePriceMarketMessageContentsMapping = {
  [ticker: string]: OraclePriceMarket,
};

interface OraclePriceMarket {
  oraclePrice: string,
  effectiveAt: IsoString,
  effectiveAtHeight: string,
  marketId: number,
}
```

### Example

```tsx
{
  "type": "channel_data",
  "connection_id": "1f4ec0e3-ff95-48cc-94f1-7118a19412ff",
  "message_id": 2,
  "channel": "v4_markets",
  "version": "0.0.1",
  "contents": {
    "trading": {
      "BTC-USD": {
        "nextFundingRate": "0.00006821875"
      },
      "ETH-USD": {
        "volume24H": "1462890959.6541",
        "nextFundingRate": "0.00007478125"
      }
    }
  }
}
```


# File: v4-documentation/old-docs/pages/infrastructure_providers-operators/indexer_usage_estimates.md

# Technical estimates

## AWS services

AWS service estimates:

- ECS - Fargate

  | Service Name | Instances | CPU | Memory |
  | ------------ | --------- | --- | ------ |
  | Comlink      | 20        |  2  | 4gb    |
  | Ender        | 1         |  4  | 8gb    |
  | Roundtable   | 5         |  2  | 4gb    |
  | Socks        | 20        |  4  | 16gb   |
  | Vulcan       | 8         |  4  | 8gb    |
- RDS - Postgres Database
  - Primary - db.m6g.16xlarge
  - Replica - 1 db.m6g.16xlarge
- EC2
  - Devboxes - t2.medium (1 instance per engineer)
- ElastiCache Redis
  - 1 primary and 1 replica with cache.r6g.large
- EC2 ELB - Loadbalancer
  - 250,000 LCU-Hrs/mo
- Cloudwatch - Logs
  - ~20,000 GB of logs ingested/mo
  - ~100,000,000 Metrics requested using GetMetricData API/mo
- Secret Manager
  - ~100 secrets
  - ~250,000 API requests

## Other services

- Terraform Cloud — deploying to cloud
  - ~4 engineers
- Bugsnag — bug awareness
  - Standard plan
- Datadog — metrics and monitoring
  - ~6000 custom metrics / hour
- PagerDuty — alerting
  - ~4 engineers
- v4 open source software is subject to [terms and conditions](https://dydx.exchange/v4-terms). dYdX will not operate or control any protocol that runs the software. The software licensing requires that users of the software comply with all applicable laws and regulations.


# File: v4-documentation/old-docs/pages/infrastructure_providers-operators/software_checklist.md

# v4 Software – Checklist

The following checklist provides suggestions for any third party interested in running v4 software.

| Checklist Item                                                       | Notes                                             |
| -------------------------------------------------------------------- | ------------------------------------------------- |
| Prepare pregenesis.json                                              |                                                   |
| Finalize validators and coordinate launch                            |                                                   |
| Distribute software and collect Gentx                                |                                                   |
| Distribute final protocol binary + final ‘genesis.json’              |                                                   |
| Compile list of full nodes for front end                             |                                                   |
| Integrate with data analytics vendors                                | Such as Amplitude or other similar providers      |
| Set up data alert vendor(s)                                          | Such as Datadog or other similar providers        |
| Set up cloud services provider                                       | Such as Cloudflare or other similar providers     |
| Set up error monitoring and reporting software                       | Such as BugSnag or other similar providers        |
| Network “launch”: start the network (including protocol and indexer) |                                                   |
| Deploy seed nodes                                                    |                                                   |
| Create IBC connection with Noble                                     |                                                   |
| Deploy front end web app and iOS app                                 |                                                   |
| Create onboarding routes                                             | Such as 0xSquid or CCTP via Noble or other routes |


# File: v4-documentation/old-docs/pages/infrastructure_providers-validators/full_node_streaming.md

# Full Node gRPC Streaming

This page has moved to [API Integration > Full Node Streaming API](../api_integration-full-node-streaming.md).


# File: v4-documentation/old-docs/pages/infrastructure_providers-validators/hardware_requirements.md

# Hardware Requirements

## Minimum Specs

The minimum recommended specs for running a node is the following:

- 16-core, x86_64 architecture processor
- 64 GiB RAM
- 500 GiB of locally attached SSD storage

For example, an AWS instance like the `r6id.4xlarge`, or equivalent.


# File: v4-documentation/old-docs/pages/infrastructure_providers-validators/optimize_full_node.md

# Optimize Your Full Node
Optimizing your full node helps keep it online, up to date, and operating quickly. Faster nodes have an advantage over slower nodes because they tend to receive new data first and they minimize the time between placing and resolving orders. Optimize your full node by connecting to trusted nodes, taking precautions against falling out of sync with the network, and configuring storage settings.

> Code snippets on this page use example values. Replace them with your own. See the [Network Configuration](../infrastructure_providers-network/network_constants.mdx) section of the documentation for network constants and other resources you need to configure a full node.

## Prerequisites
You need a running, non-validating full node that is connected to a network. 

- If you created a system service for your node by following the instructions on the previous page, [Set Up a Full Node](../infrastructure_providers-validators/set_up_full_node.md), start your node with the following command:
  ```bash
  stystemctl start dydxprotocold
  ```

- To start your node with Cosmovisor or with the `dydxprotocold` binary, you must include the flag `--non-validating-full-node=true`. The flag disables the functionality intended for validator nodes and enables additional logic for reading data. Your CLI may prompt you to configure additional variables in your environment or include them in your command.
  
  To start your node with Cosmovisor, run the following command:
  ```bash
  cosmovisor run start --non-validating-full-node=true
  ```

  To start your node with `dydxprotocold`, run the following command:
  ```bash
  dydxprotocold run start --non-validating-full-node=true 
  ```

## Save a List of Trusted Nodes
Specify a list of healthy, stable nodes that you trust. Your node prioritizes connecting to those nodes, speeding up the process of connecting or re-connecting to the network. Connecting directly with a peer node is faster than connecting to a seed node and then finding new peers.

### Save a List of Persistent Peers
You can save a list of healthy, stable nodes in the `persistent_peers` field of your `config.toml` file.

Request a list of healthy peers for your deployment from a [Live Peer Node](../infrastructure_providers-network/resources.mdx#live-peer-node-providers) provider.

From the list of healthy peers that you retrieve from peer node provider, choose any 5 for your node to query for the latest state. Add a comma-separated list of those peer addresses to the `persistent_peers` field in your `config.toml`, like in the following example:

```yaml
# config.toml
# Example values from Polkachu for dydx-mainnet-1
persistent_peers=83c299de2052db247f08422b6592e1383dd7a104@136.243.36.60:23856,1c64b35055d34ff3dd199bb4a5a3ae46b9c10c89@3.114.126.71:26656,3651c82a89f8f4d6fc30fb27b91159f0de092031@202.8.9.134:26656,580ec248de1f41d4e50abe132b7838348db55b80@176.9.144.40:23856,febe75fb6e70a60ce6344b82ff14903bcb53a209@38.122.229.90:26656
```

### Replace Your Address Book File
As an alternative to persistent peers, you can replace your node's local address book with the latest address book from a trusted provider. The address book file contains the latest connection information for peers from that provider.

Download an up-to-date `addrbook.json` file for your deployment from an [Address Book](../infrastructure_providers-network/resources.mdx#address-book-providers) provider. 

Save it in your `/.dydxprotocol/config` directory, replacing the existing `addrbook.json` file.

## Prepare to Restore Your Node
To minimize downtime in case your node falls out of sync, make preparations to restore your node quickly.

Your full node can fall out of sync with the rest of the network for a variety of reasons, including a bad software upgrade, unexpected node crashes, or human operational error. To re-sync with the network, your full node needs to replay the history of the network, which can take a long time.

You can speed up the re-syncing process significantly by providing your node with a snapshot. A snapshot contains a compressed copy of the application state at the time the snapshot was taken. If your node falls out of sync, a snapshot allows it to recover to that saved state before replaying the rest of the history of the network, saving you time.

### Configure Your Node's State Sync Setting
You can use state sync, a configuration setting that allows your node to retrieve a snapshot from the network, to ensure that your node can be restored quickly if it falls out of sync.

To use state sync for quick recovery in case your node falls out of sync, follow the instructions for your deployment from a [State Sync](../infrastructure_providers-network/resources.mdx#state-sync-service) service.

<!-- 
Cosmos SDK 0.40 release will include automatic support for state sync, and developers only need to enable it in their applications to make use of it. Replace above with a procedure.
-->

### Save a Snapshot on Your System
As an alternative to state sync, you can use a snapshot that you have saved on your node's system to restore your node if it falls out of sync.

To save a snapshot on your system for quick recovery in case your node falls out of sync, install a snapshot for your deployment from a [Snapshot Service](../infrastructure_providers-network/resources.mdx#snapshot-service).

## Configure a Pruning Strategy
To reduce the amount of storage your node requires, dYdX recommends the following pruning setting, configured in your `app.toml` file:

```bash
# app.toml
pruning = "everything" # 2 latest states will be kept; pruning at 10 block intervals
```

However, if you want to use your node to query historical data, configure a custom pruning strategy to retain more states. Retaining more states increases storage requirements.

# File: v4-documentation/old-docs/pages/infrastructure_providers-validators/peering_with_gateway.md

# Peering Directly with Order Gateway

For improved order latency of the network, the community might spin up an order gateway node to directly peer with. A chain coordination party may share this in the form of `$gateway_node_id@$gateway_ip_address:$port`.

There are 2 options to peer directly with the gateway node:

## Option A: Gateway -> Validator

- Share the full peering info of your validator node (`node_id@ip_address:port`) with the coordination party, which can be added as a `persistent_peer` to the gateway node. It's important that raw IP address (as opposed to a loadbalancer URL) of the validator node (as opposed to a sentry node) is shared. This ensures that the a direction connection can be maintained across node restarts.
  - If your IP or node ID changes due to node migration, please inform the coordination party.  
- Add the gateway `node_id` as a private and unconditional peer. This ensure that the gateway node is not subject to regualr peer # limits, and is not broadcasted to the rest of the network.

```bash
--p2p.private_peer_ids="$gateway_node_id,..."
--p2p.unconditional_peer_ids="$gateway_node_id,..."
```

## Option B: Validator -> Gateway

- Share the `node_id` (IP not required) of your validator node with the coordination party. It's important to share the `node_id` of the validator node, as opposed to a sentry node. This can be added to the gateway node as `unconditional_peer`.
- Add the gateway node as a persistent and private peer to the validator node:

```bash
--p2p.private_peer_ids="$gateway_node_id,..."
--p2p.persistent_peers="$gateway_node_id@$gateway_ip_address:$port,..."
```

# Addendum

CometBFT [documentation](https://docs.cometbft.com/v0.38/spec/p2p/legacy-docs/config) on P2P configs

# File: v4-documentation/old-docs/pages/infrastructure_providers-validators/required_node_configs.md

# Required Node Configs

These configurations must be applied for both full nodes and validators.

💡Note: failure to set up below configurations on a validator node may compromise chain functionality.

## Node Configs

The dYdX Chain has important node configurations required for normal chain operation. This includes:
- The `config.toml` file read by CometBFT
  - ([Full documentation](https://docs.cometbft.com/v0.38/core/configuration))
- The `app.toml` file read by CosmosSDK
  - ([Full documentation](https://docs.cosmos.network/main/learn/advanced/config))

### `config.toml`

#### Consensus Configs

```
[consensus]
timeout_commit = "500ms"
```

### `app.toml`

#### Base Configuration

Replace `$NATIVE_TOKEN_DENOM` at the end of the field with the correct value from [Network Constants](../infrastructure_providers-network/network_constants.mdx#native-token-denom)

```
### Gas Prices ###
minimum-gas-prices = "0.025ibc/8E27BA2D5493AF5636760E354E46004562C46AB7EC0CC4C1CA14E9E20E2545B5,12500000000$NATIVE_TOKEN_DENOM"
```

```
### Pruning ###
pruning = "custom"

# Small numbers >= "2" for validator nodes.
# Larger numbers could be used for full-nodes if they are used for historical queries.
pruning-keep-recent = "7"

# Any prime number between "13" and "97", inclusive.
pruning-interval = "17"
```

#### gRPC Configs

```
[grpc]
# Enable grpc. The Cosmos gRPC service is used by various daemon processes,
# and must be enabled in order for the protocol to operate:
enable = true

# Non-standard gRPC ports are not supported at this time. Please run on port 9090, which is the default
# port specified in the config file.
# Note: grpc can be also be configured via start flags. Be careful not to change the default settings
# with either of the following flags: `--grpc.enable`, `--grpc.address`.
address = "0.0.0.0:9090"
```


# File: v4-documentation/old-docs/pages/infrastructure_providers-validators/running_a_validator.md

# Running a Validator

💡Note: failure to set up below configurations on a validator node may compromise chain functionality.

## Ethereum RPC Endpoint

For the chain to process bridge transactions from Ethereum, Ethereum testnet, or other chain that supports the `eth_getLogs` RPC method, the bridge daemon queries an RPC endpoint for logs emitted by the bridge contract. By default, a node will use a public testnet endpoint that may have rate-limiting, low reliability, or other restricted functionality.

As a validator run the flags `--bridge-daemon-enabled=false` in the command you run when starting the node, since the bridge has been disabled

## Connect Sidecar

Starting in `v5.0.0`, running a validating full node requires a Skip Protocol's Connect Sidecar to be run in order to fetch Oracle prices. The sidecar should be started before upgrading from `v4` to `v5`. Instructions to start Connect Sidecar can be found [here](https://docs.skip.build/connect/validators/quickstart).

Support issues with Skip's Sidecar should be directed [here](https://discord.gg/7hxEThEaRQ).

You can find the required version of the Connect sidecar listed in the `dYdX Blockchain` section [here](https://docs.skip.build/connect/validators/quickstart#run-connect-sidecar).

Instructions on upgrading sidecar can be found [here](./upgrades/upgrading_sidecar.md).


# File: v4-documentation/old-docs/pages/infrastructure_providers-validators/set_up_full_node.md

# Set Up a Full Node
Installing and running a full node allows you to read orderbook and onchain data from a network, as well as place, confirm and cancel orders directly on that network.

> Code snippets on this page use example values. Replace them with your own. See the [Network Configuration](../infrastructure_providers-network/network_constants.mdx) section of the documentation for network constants and other resources you need to configure a full node.

## Prerequisites

The minimum recommended specs for running a node is the following:

- 16-core, x86_64 architecture processor
- 64 GiB RAM
- 500 GiB of locally attached SSD storage

For example, an AWS instance like the `r6id.4xlarge`, or equivalent.

## Choose a Method
To set up a full node, you can either:

1. Use [this script](https://github.com/dydxprotocol/v4-chain/blob/main/protocol/scripts/create_full_node.sh), provided by dYdX, to automate setup.

Save the script with an `.sh` extension in your `$HOME` directory. Edit the script, replacing default values in fields such `VERSION` and `CHAIN-ID` with your own. Run the script with the following commands:

> To find the current version of the [dYdX foundation](https://www.dydx.foundation/) mainnet, see the recommended protocol version on [mintscan.io](https://www.mintscan.io/dydx/parameters). To find network constants such as chain IDs, see the [Network Configuration](../infrastructure_providers-network/network_constants.mdx) section of the documentation.

```bash
cd $HOME
bash create_full_node.sh
```

2. Or, follow the steps on this page to manually set up a full node.

## Manual Installation Steps
The following steps will guide you through manually setting up a full node.

Run the commands in this procedure from your home directory unless otherwise specified. To change directories to your home folder, run the following command:
```bash
cd $HOME
```

### Step 1: Update your system and prepare to install dependencies
To download system updates and install [curl](https://curl.se/),[jq](https://jqlang.github.io/jq/), and [lz4](https://lz4.org/), run the following commands:
```bash
sudo apt-get -y update
sudo apt-get install -y curl jq lz4
```

### Step 2: Install Go
To install [Go](https://go.dev/), run the following commands using the latest version of Go:

```bash
# Example for AMD64 architecture and Go version 1.22.2
wget https://golang.org/dl/go1.22.2.linux-amd64.tar.gz # Download the compressed file
sudo tar -C /usr/local -xzf go1.22.2.linux-amd64.tar.gz # Extract the file to /usr/local
rm go1.22.2.linux-amd64.tar.gz # Delete the installer package
```

Add the Go directory to your system `$PATH`:
```bash
echo 'export PATH=$PATH:/usr/local/go/bin:$HOME/go/bin' >> $HOME/.bashrc # Write to your .bashrc profile
```

### Step 3: Install Cosmovisor and create data directories
[Cosmovisor](https://docs.cosmos.network/main/build/tooling/cosmovisor) is a process manager for Cosmos SDK-based blockchains that enables automatic binary updates without downtime. To install the latest version of Cosmovisor, run the following command:
```bash
go install cosmossdk.io/tools/cosmovisor/cmd/cosmovisor@latest
```

To create data directories for Cosmovisor, run the following commands:
```bash
mkdir -p $HOME/.dydxprotocol/cosmovisor/genesis/bin
mkdir -p $HOME/.dydxprotocol/cosmovisor/upgrades
```

### Step 4: Download the `dydxprotocold` binary
The `dydxprotocold` binary contains the software you need to operate a full node. **You must use the same version of the software as the network to which you want to connect.** To find the current version of the [dYdX foundation](https://www.dydx.foundation/) mainnet, see the recommended protocol version on [mintscan.io](https://www.mintscan.io/dydx/parameters).

**Option 1**: Find and download that protocol binary from the [v4 Chain Releases](https://github.com/dydxprotocol/v4-chain/releases/) page.
> For example, for protocol version 5.0.5 on an AMD system, download `dydxprotocold-v5.0.5-linux-amd64.tar.gz`.

**Option 2**: Download the binary with `curl`, replacing the version numbers and architecture of the package as needed:
```bash
# curl example for protocol version 5.0.5 on AMD64 architecture
curl -L -O https://github.com/dydxprotocol/v4-chain/releases/download/protocol/v5.0.5/dydxprotocold-v5.0.5-linux-amd64.tar.gz
```

### Step 5: Move `dydxprotocold` to your Cosmovisor `/genesis` directory
After you download the binary, moving `dydxprotocold` into your Cosmovisor data directory allows you to use Cosmovisor for no-downtime binary upgrades. To extract, rename, and move the file to your Cosmovisor data directory, run the following commands:

```bash
# Example for AMD64 architecture
sudo tar -xzvf dydxprotocold-v5.0.5-linux-amd64.tar.gz # Extract the file
sudo mv ./build/dydxprotocold-v5.0.5-linux-amd64 ./.dydxprotocol/cosmovisor/genesis/bin/dydxprotocold # Move the file to /.dydxprotocol and rename it
rm dydxprotocold-v5.0.5-linux-amd64.tar.gz # Delete the installer package
rm -rf build # Delete the now-empty /build directory
```

Add the `dydxprotocold` directory to your system `$PATH`:
```bash
echo 'export PATH=$PATH:$HOME/.dydxprotocol/cosmovisor/genesis/bin' >> $HOME/.bashrc # Write to your .bashrc profile
```

### Step 6: Initialize your node
To initialize your node, provide the ID of the chain to which you want to connect and create a name for your node. The dYdX home directory is created in `$HOME/.dydxprotocol` by default. Replace the example values `dydx-mainnet-1` and `my-node` with your own and run the following command:
```bash
# Example for DYDX token holders on mainnet
dydxprotocold init --chain-id=dydx-mainnet-1 my-node
```

> See the [Network Configuration](../infrastructure_providers-network/network_constants.mdx) section of the documentation for chain IDs and other network constants.

When you initialize your node, `dydxprotocold` returns your default node configuration in JSON.

### Step 7: Update your node configuration with a list of seed nodes
A seed node acts as an address book and helps your node join the network. To update `config.toml` with a list of seed nodes, run the following command:

> Check the [Resources](https://docs.dydx.exchange/network/resources#seed-nodes) page for an up-to-date list of seed nodes for the network to which you want to connect.

```bash
# Example for DYDX token holders on mainnet
SEED_NODES=("ade4d8bc8cbe014af6ebdf3cb7b1e9ad36f412c0@seeds.polkachu.com:23856",
"65b740ee326c9260c30af1f044e9cda63c73f7c1@seeds.kingnodes.net:23856",
"d8e106274b24ec64ce724a611def6a3637226745@dydx-mainnet-seed.bwarelabs.com:36656",
"20e1000e88125698264454a884812746c2eb4807@seeds.lavenderfive.com:23856",
"c2c2fcb5e6e4755e06b83b499aff93e97282f8e8@tenderseed.ccvalidators.com:26401",
"a9cae4047d5c34772442322b10ef5600d8e54900@dydx-mainnet-seednode.allthatnode.com:26656",
"802607c6db8148b0c68c8a9ec1a86fd3ba606af6@64.227.38.88:26656",
"ebc272824924ea1a27ea3183dd0b9ba713494f83@dydx-mainnet-seed.autostake.com:27366"
)

sed -i 's/seeds = ""/seeds = "'"${SEED_NODES[*]}"'"/' $HOME/.dydxprotocol/config/config.toml
```

The preceding command updates the `seeds` variable of `config.toml` with the list you provide.

### Step 8: Use a snapshot as your node's initial state
Using snapshots to restore or sync your full node's state saves time and effort. Using a snapshot avoids replaying all the blocks from genesis and does not require multiple binary versions for network upgrades. Instead, your node uses the snapshot as its initial state.

#### Clear your data directory
If you already have a data directory at `$HOME/.dydxprotocol/data`, you must clear it before installing a snapshot, which comes with its own data directory. To clear your data directory while retaining files you need, follow these steps:

First, make a backup copy of `priv_validator_state.json` in your `.dydxprotocol` directory by running the following command:
```bash
# Make a copy of priv_validator_state.json and append .backup
cp $HOME/.dydxprotocol/data/priv_validator_state.json $HOME/.dydxprotocol/priv_validator_state.json.backup
```

Next, confirm the following:
- A backup file, `priv_validator_state.json.backup`, exists in your current directory.
- The original `priv_validator_state.json` exists in the `/data` directory to be deleted.
- No other files exist in the `/data` directory to be deleted.

```bash
ls $HOME/.dydxprotocol # Confirm that the backup exists in /.dydxprotocol
ls $HOME/.dydxprotocol/data # Confirm that only priv_validator_state.json exists in /data
```

Finally, to clear the data directory, removing it and all files inside, run the following command:
```bash
# WARNING: This command recursively deletes files and directories in the dydxprotocol /data directory. Make sure you know what you are deleting before running the command.
rm -rf $HOME/.dydxprotocol/data
```

Installing a snapshot will create a new `/data` directory.

#### Install the Snapshot
To download and extract the snapshot contents to the default dydxprotocol home directory, first **change directories into /.dydxprotocol**. To change directories, run the following command:

```bash
cd $HOME/.dydxprotocol
```

Next, find a provider for your use case on the [Snapshot Service](https://docs.dydx.exchange/network/resources#snapshot-service) page. Use the provider's instructions to download the snapshot into your `$HOME/.dydxprotocol` directory.

> For example, if you are connecting to `dydx-mainnet-1`, you may use the provider [Polkachu](https://polkachu.com/tendermint_snapshots/dydx). In most cases, you can run `wget <snapshot-web-address>`.

Next, run the following command in your `$/HOME/.dydxprotocol` directory, replacing the example value `your-snapshot-filename`:

```bash
lz4 -dc < your-snapshot-filename.tar.lz4 | tar xf -
```
Extracting the snapshot creates a new `/data` folder in your current directory, `.dydxprotocol`.

Next, use the backup file `priv_validator_state.json.backup` you created to reinstate `/data/priv_validator_state.json` with the following command:

```bash
mv $HOME/.dydxprotocol/priv_validator_state.json.backup $HOME/.dydxprotocol/data/priv_validator_state.json
```

Finally, **change directories back to your $HOME directory for the rest of the procedure**. Run the following command:
```bash
cd $HOME
```

When you start your full node, it will automatically use the snapshot in your data directory to begin syncing your full node's state with the network.

### Step 9: Create a system service to start your full node automatically
To create a `systemd` service that starts your full node automatically, run the following commands:

```bash
sudo tee /etc/systemd/system/dydxprotocold.service > /dev/null << EOF
[Unit]
Description=dydxprotocol node service
After=network-online.target

[Service]
User=$USER
ExecStart=/$HOME/go/bin/cosmovisor run start --non-validating-full-node=true
WorkingDirectory=$HOME/.dydxprotocol
Restart=always
RestartSec=5
LimitNOFILE=4096
Environment="DAEMON_HOME=$HOME/.dydxprotocol"
Environment="DAEMON_NAME=dydxprotocold"
Environment="DAEMON_ALLOW_DOWNLOAD_BINARIES=false"
Environment="DAEMON_RESTART_AFTER_UPGRADE=true"
Environment="UNSAFE_SKIP_BACKUP=true"

[Install]
WantedBy=multi-user.target
EOF

sudo systemctl daemon-reload
sudo systemctl enable dydxprotocold
```

The system service definition above holds environment variables. When you start it, the service will run the command `/$HOME/go/bin/cosmovisor run start --non-validating-full-node=true`.

> The flag `--non-validating-full-node` is required. It disables the functionality intended for validator nodes and enables additional logic for reading data.

### Step 10: Start the service
To start your node using the `systemd` service that you created, run the following command:
```bash
sudo systemctl start dydxprotocold
```

When you want to stop the service, run the following command:
```bash
sudo systemctl stop dydxprotocold
```

When you start your full node it must sync with the history of the network. If you initialized your full node using a snapshot, your node must update its state only with blocks created after the snapshot was taken. If your node's state is empty, it must sync with the entire history of the network.

### Check your service logs to confirm that your node is running
```bash
sudo journalctl -u dydxprotocold -f
```
If your system service `dydxprotocold` is running, the preceding command streams updates from your node to your command line. Press `Ctrl + C` to stop viewing updates.

Finally, confirm that your full node is properly synchronized by comparing its current block to the dYdX Chain:
- To find the network's current block, see the **Block Height** of your network with a block explorer, such as [mintscan.io](https://www.mintscan.io/dydx).
- To find your full node's height, query your node with the following command:
```bash
curl localhost:26657/status
```

When your full node's latest block is the same as the network's latest block, your full node is ready to participate in the network.

## Next Steps
When your full node is up to date with the network, you can use it to read live data and configure additional settings. Learn more on the [Running a Full Node](../infrastructure_providers-validators/optimize_full_node.md) page.

# File: v4-documentation/old-docs/pages/infrastructure_providers-validators/snapshots.md

# Snapshots

Services that provide snapshots for the network can be found [here](../infrastructure_providers-network/resources.mdx#snapshot-service) .
These snapshots will be used as a backup point in case an upgrade fails or a new node wants to start up and does not want to start from block 1 to catchup.


# File: v4-documentation/old-docs/pages/infrastructure_providers-validators/upgrades/cosmovisor.md

# Cosmovisor

`cosmovisor` is a small process manager for Cosmos SDK application binaries that monitors the governance module for incoming chain upgrade proposals. If it sees a proposal that gets approved, `cosmovisor` can automatically download the new binary, stop the current binary, switch from the old binary to the new one, and finally restart the node with the new binary.

We recommend validators to use `cosmovisor` to run their nodes. This will make low-downtime upgrades smoother, as validators don’t have to manually upgrade binaries during the upgrade. Instead, they can pre-install new binaries, and `cosmovisor` will automatically update them based on the onchain software upgrade proposals.

## Configuration

When Cosmovisor activates an upgrade, it does a backup of the entire data directory by default. This backup can take a very long time to process unless the user does aggressive historical-state-pruning using the `pruning` [configuration on the node](../required_node_configs.md).

As long as you have access to a previous state [snapshot](../snapshots.md), we recommend setting the environment variable `UNSAFE_SKIP_BACKUP` to `true` which skips the data backup and allows a much faster upgrade. If your node is configured to only keep a small amount of historical state, then you may be able to get away with running the backup quickly.

More information about Cosmovisor settings can be found in the [Cosmovisor documentation](https://docs.cosmos.network/main/build/tooling/cosmovisor).

## Installation

### Using go install

To install the latest version of `cosmovisor`, run the following command:

```bash
go install cosmossdk.io/tools/cosmovisor/cmd/cosmovisor@latest
```

### Manual Build

You can also install from source by pulling the cosmos-sdk repository and switching to the correct version and building as follows:

```bash
git clone https://github.com/cosmos/cosmos-sdk.git
cd cosmos-sdk
git checkout cosmovisor/vx.x.x
make cosmovisor
```

This will build Cosmovisor in `/cosmovisor`
 directory. Afterwards you may want to put it into your machine's PATH like as follows:

```bash
cp cosmovisor/cosmovisor ~/go/bin/cosmovisor
```

To check your Cosmovisor version, run

```bash
cosmovisor version
```

## Directory structure

```
.
├── current -> genesis or upgrades/<name>
├── genesis
│   └── bin
│       └── $DAEMON_NAME
└── upgrades
    └── <name>
        ├── bin
        │   └── $DAEMON_NAME
        └── upgrade-info.json
```

## Initializing Cosmovisor

1. Rename binary to `dydxprotocold`

```bash
mv dydxprotocold.<version>-<platform> dydxprotocold
```

2. Set the environment variables

```bash
export DAEMON_NAME=dydxprotocold
export DAEMON_HOME=<your directory>
```

3. The directory structure can be initialized with

```bash
cosmovisor init <path to executable>
```

- `DAEMON_HOME` should be set to the **validator’s home directory** since Cosmovisor polls `/data/` for upgrade info.
- `DAEMON_NAME` should be set to `dydxprotocold`

## How to run

`cosmovisor` is simply a thin wrapper around Cosmos applications. Use the following command to start a testnet validator using `cosmovisor` .

```bash
cosmovisor run arg1 arg2 arg3 ...
```

All arguments passed to `cosmovisor run` will be passed to the application binary (as a subprocess). `cosmovisor` will return `/dev/stdout` and  `/dev/stderr` of the subprocess as its own.

Example:

```bash
cosmovisor run start —log-level info —home /dydxprotocol/chain/.alice
```

runs

```bash
dydxprotocold start —log-level info —home /dydxprotocol/chain/.alice
```

as its subprocess.


# File: v4-documentation/old-docs/pages/infrastructure_providers-validators/upgrades/performing_upgrades.md

# Performing Upgrades

## Managing Upgrades

Validators can choose how to run a validator and manage software upgrades according to their preferred option:

1. Using [Cosmovisor](./cosmovisor.md)
2. Manual

## Voting for Upgrade Proposals

See [Governance -> Voting](../../users-governance/voting.md)

## Upgrades

Releases for the dYdX Chain will use [semantic versioning](https://semver.org/). See [here](./types_of_upgrades.md) for details.

### ⚒️ Cosmovisor Users

#### Upgrading to a new Major/Minor Version (e.g. v0.1.0)

1. Download the [binary](https://github.com/dydxprotocol/v4-chain) for the new release, rename the binary to `dydxprotocold`.

```bash
mv dydxprotocold.<version>-<platform> dydxprotocold
```

2. Make sure that the new binary is executable.

```bash
chmod 755 dydxprotocold
```

3. Create a new directory `$DAEMON_HOME/cosmovisor/upgrades/<name>/bin` where `<name>` is the URI-encoded name of the upgrade as specified in the Software Upgrade Plan.

```bash
mkdir -p $DAEMON_HOME/cosmovisor/upgrades/<name>/bin
```

4. Place the new binary under `$DAEMON_HOME/cosmovisor/upgrades/<name>/bin` before the upgrade height.


```bash
mv <path_to_major_version> $DAEMON_HOME/cosmovisor/upgrades/<name>/bin
```

💡 **IMPORTANT**: Do this before the upgrade height, so that `cosmovisor` can make the switch.

That’s it! The old binary will stop itself at the upgrade height, and `cosmovisor` will switch to the new binary automatically. For a `Plan` with name `v0.1.0`, your `cosmovisor/` directory should look like this:

```
cosmovisor/
├── current/   # either genesis or upgrades/<name>
├── genesis
│   └── bin
│       └── dydxprotocold
└── upgrades
    └── v0.1.0
        ├── bin
           └── dydxprotocold
```

#### Upgrading to a Patch Version (e.g. v0.0.2)

1. Download the [binary](https://github.com/dydxprotocol/v4-chain/releases) for the new patch release, rename the binary to `dydxprotocold`.

```bash
mv dydxprotocold.<version>-<platform> dydxprotocold
```

2. Make sure that the new binary is executable.

```bash
chmod 755 dydxprotocold
```

3. Replace the binary under `$DAEMON_HOME/cosmovisor/current/bin` with the new binary.

```bash
mv <path_to_patch_version> $DAEMON_HOME/cosmovisor/current/bin
```

4. Stop the current binary (e.g. Ctrl+C)
5. Restart `cosmovisor`

```bash
cosmovisor run start --p2p.seeds="[seed_node_id]@[seed_node_ip_addr]:26656" --bridge-daemon-eth-rpc-endpoint="<eth rpc endpoint>"
```

### 🦾 Manual Users

#### Upgrading to a Major/Minor Version (e.g. v0.1.0)

1. Download the [binary](https://github.com/dydxprotocol/v4-chain/releases) for the new release.
    1. Ideally also before the upgrade height to minimize downtime
2. Make sure that the new binary is executable.

```bash
chmod 755 dydxprotocold
```

3. Wait for the old binary to stop at the upgrade height (this should happen automatically).
4. Restart the application using the **new binary from step 1**.

```bash
./dydxprotocold start --p2p.seeds="[seed_node_id]@[seed_node_ip_addr]:26656" --bridge-daemon-eth-rpc-endpoint="<eth rpc endpoint>"
```

#### Upgrading to a Patch Version (e.g. v0.0.2)

1. Download the [binary](https://github.com/dydxprotocol/v4-chain/releases) for the new release.
2. Make sure that the new binary is executable.

```bash
chmod 755 dydxprotocold
```

3. Stop the current binary (e.g. Ctrl+C)
4. Restart the application using the new binary from step 1.

```bash
./dydxprotocold start --p2p.seeds="[seed_node_id]@[seed_node_ip_addr]:26656" --bridge-daemon-eth-rpc-endpoint="<eth rpc endpoint>"
```

---

## Rollback


In the case of an unsuccessful chain upgrade, an incorrect `AppHash` might get persisted by Tendermint. To move forward, validators will need to rollback to the previous state so that upon restart, Tendermint can replay the last block to get the correct `AppHash`. **Please note:** validators should never rollback further than the last invalid block. In extreme edge cases, transactions could be reverted / re-applied for the last black and cause issues.


### ⚒️ Cosmovisor Users

Cosmovisor backs up the `data` directory before attempting an upgrade. To restore to a previous version:

1. Stop the node (e.g. Ctrl+C)
2. Then, copy the contents of your backup data directory back to `~/.dydxprotocol`

```bash
rm -rf ~/.dydxprotocol/data
mv ~/.dydxprotocol/data-backup-YYYY-MM-DD ~/.dydxprotocol/data
```

3. Restart your node.

```bash
cosmovisor run start --p2p.seeds="[seed_node_id]@[seed_node_ip_addr]:26656" --bridge-daemon-eth-rpc-endpoint="<eth rpc endpoint>"
```

### 🦾 Manual Users

If you don’t have a data backup:

1. Stop the node (e.g. Ctrl+C)
2. Rollback the application and Tendermint state by one block height.

```bash
./dydxprotocold rollback
```

3. Restart your node.

```bash
./dydxprotocold start --p2p.seeds="[seed_node_id]@[seed_node_ip_addr]:26656" --bridge-daemon-eth-rpc-endpoint="<eth rpc endpoint>"
```


# File: v4-documentation/old-docs/pages/infrastructure_providers-validators/upgrades/types_of_upgrades.md

# Types of upgrades

## Major and minor versions

Major and minor changes can be consensus breaking. These upgrades usually go through a governance proposal and happen at specific heights.

## Patch versions

Patch versions are backwards compatible changes. These typically can be applied in a rolling fashion and don’t need to go through a governance proposal.

## Hard-forks

One of the limitations of the normal upgrade procedure via governance is that it requires waiting for the entire voting period, which makes them unsuitable for emergency situations. For such cases, hard forks are usually required.

The high-level strategy for coordinating an upgrade is as follows:

1. The vulnerability is fixed on a private branch that contains breaking changes.
2. A new patch release (e.g. `v8.0.0` -> `v8.0.1`) needs to be created that contains a hard fork logic and performs an upgrade to the next breaking version (e.g. `v9.0.0`) at a predefined block height.
3. Validators upgrade their nodes to the patch release (e.g. `v8.0.1`). In order to perform the hard fork successfully, it’s important that enough validators upgrade to the patch release so that they make up at least 2/3 of the total validator voting power.
4. Before the upgrade time (corresponding to the upgrade block height), the new major release (e.g. `v9.0.0`) including the vulnerability fix is published.
5. Upgrades happen in a similar fashion as `MsgSoftwareUpgrade`.

From a node operator’s perspective, hard forks are essentially a combination of a patch version (`v8.0.1`) followed by a major version (`v9.0.0`). Please use the instructions from [Performing Upgrades](./performing_upgrades.md) to perform the corresponding upgrades.


# File: v4-documentation/old-docs/pages/infrastructure_providers-validators/upgrades/upgrading_sidecar.md

Starting in `v5.0.0`, all validating full nodes should be running the [Sidecar](../optimize_full_node.md#slinky-sidecar). Non validating full nodes do not need to run the sidecar.

Follow instructions [here](https://docs.skip.build/connect/validators/faq#how-do-i-upgrade-the-connect-binary) to upgrade the sidecar.


# File: v4-documentation/old-docs/pages/infrastructure_providers-validators/upgrades/using_cosmovisor_to_stage_dYdX_Chain_binary_upgrade.md

# Using Cosmovisor to stage dYdX Chain binary upgrade 

## Prerequisite

1. Linux (Ubuntu Server 22.04.3 recommended)
2. 8-cpu (ARM or x86_64), 64 GB RAM, 500 GB SSD NVME Storage
3. Already installed dYdXChain full node

## Preparation

1. Install Go from https://go.dev/doc/install (Version tested is 1.22.1)
2. Install Cosmovisor, with the following command:
- `go install cosmossdk.io/tools/cosmovisor/cmd/cosmovisor@latest`
3. Copy cosmovisor from $HOME/go/bin/ to a directory in your $PATH
4. Add two environment variables to $HOME/.profile.  The data directory is typically $HOME/.dydx-mainnet-1
- `export DAEMON_NAME=dydxprotocold`
- `export DAEMON_HOME=<your data directory>`
5. Log out and log back in.
6. Initialize Cosmovisor with the following command.  The <path to executable> is the the full path to dydxprotocold
- `cosmovisor init <path to executable>`
7. Cosmovisor is now ready for use.

## Running dydxprotocold under Cosmovisor

You have to change the way you currently run dydxprotocold to run under Cosmovisor.  This is done simply by specifying “cosmovisor run” in place of the “dydxprotocold” command you used previously.  Therefore, if you previously used “dydxprotocold start --p2p.seeds="ade4d8…”, you would change that to “cosmovisor run start --p2p.seeds="ade4d8…”

## Staging upgrade

1. The Cosmovisor directory structure looks like this:

![Upgrade1](../../../artifacts/Staging_1.png)

2. To stage an upgrade, you would create a <name> directory inside the upgrades/ directory.  For example, as of 4/1/2024, the current version is v3.0.0 and the next upgrade version is v4.0.0.  Therefore you would create a directory called “v4.0.0” and then a bin directory inside it.

![Upgrade2](../../../artifacts/Staging_2.png)

3. Now, download the upgraded binary and put it inside the bin directory created previously.  It must be named dydxprotocold

4. Restart dydxprotocold with Cosmovisor.  Now, Cosmovisor will automatically halt the current binary at the block activation height and start the upgrade binary.


# File: v4-documentation/old-docs/pages/concepts-architecture/architectural_overview.md

# Intro to dYdX Chain Architecture

### System Architecture

dYdX Chain (sometimes referred to as "v4") has been designed to be completely decentralized end-to-end. The main components broadly include the protocol, the Indexer, and the front end. Each of these components are available as open source software. None of the components are run by dYdX Trading Inc.

![image](https://github.com/dydxprotocol/v4-documentation/assets/130097657/e9a54253-e7fa-44ab-97c5-ae1ce7cae320)

### Protocol (or “Application”)

The open-source protocol is an L1 blockchain built on top of [CometBFT](https://dydx.exchange/blog/v4-technical-architecture-overview#:~:text=on%20top%20of-,CometBFT,-and%20using%20CosmosSDK) and using [CosmosSDK](https://docs.cosmos.network/). The node software is written in Go, and compiles to a single binary. Like all CosmosSDK blockchains, dYdX Chain uses a proof-of-stake consensus mechanism.

The protocol is supported by a network of nodes. There are two types of nodes:

- **Validators**: Validators are responsible for storing orders in an in-memory orderbook (i.e. off chain and not committed to consensus), gossipping transactions to other validators, and producing new blocks for dYdX Chain through the consensus process. The consensus process will have validators take turns as the proposer of new blocks in a weighted-round-robin fashion (weighted by the number of tokens staked to their node). The proposer is responsible for proposing the contents of the next block. When an order gets matched, the proposer adds it to their proposed block and initiates a consensus round. If ⅔ or more of the validators (by stake weight) approve of a block, then the block is considered committed and added to the blockchain. Users will submit transactions directly to validators.

- **Full Nodes**: A Full Node represents a process running the dYdX Chain open-source application that does not participate in consensus. It is a node with 0 stake weight and it does not submit proposals or vote on them. However, full nodes are connected to the network of validators, participate in the gossiping of transactions, and also process each new committed block. Full nodes have a complete view of a dYdX Chain and its history, and are intended to support the Indexer. Some parties may decide (either for performance or cost reasons) to run their own full node and/or Indexer.

### Indexer

The Indexer is a read-only collection of services whose purpose is to index and serve blockchain data to end users in a more efficient and web2-friendly way. This is done by consuming real time data from a dYdX Chain full node, storing it in a database, and serving that data through a websocket and REST requests to end-users.

While the dYdX Chain open-source protocol itself is capable of exposing endpoints to service queries about some basic onchain data, those queries tend to be slow as validators and full nodes are not optimized to efficiently handle them. Additionally, an excess of queries to a validator can impair its ability to participate in consensus. For this reason, many Cosmos validators tend to disable these APIs in production. This is why it is important to build and maintain Indexer and full-node software separate from validator software.

Indexers use Postgres databases to store onchain data, Redis for offchain data, and Kafka for consuming and streaming on/offchain data to the various Indexer services.

### Front-ends

In service of building an end-to-end decentralized experience, dYdX has built three open-source front ends: a web app, an iOS app, and an Android app.

- **Web application**: The website was built using Javascript and React. The website interacts with the Indexer through an API to get offchain orderbook information and will send trades directly to the chain. dYdX has open sourced the front-end codebase and associated deployment scripts. This allows anyone to easily deploy and access the dYdX front end to/from their own domain/hosting solution via IPFS/Cloudflare gateway.

- **Mobile**: The iOS and Android apps are built in native Swift and Kotlin, respectively. The mobile apps interact with the Indexer in the same way the web application does, and will send trades directly to the chain. The mobile apps have been open sourced as well, allowing anyone to deploy the mobile app to the App Store or Play store. Specifically for the App store, the deployer needs to have a developer account as well as a Bitrise account to go through the app submission process.

### Lifecycle of an Order

Now that we have a better understanding of each of the components of dYdX Chain, let’s take a look at how it all comes together when placing an order. When an order is placed on dYdX Chain, it follows the flow below:

1. User places a trade on a decentralized front end (e.g., website) or via API
2. The order is routed to a validator. That validator gossips that transaction to other validators and full nodes to update their orderbooks with the new order.
3. The consensus process picks one validator to be the proposer. The selected validator matches the order and adds it to its next proposed block.
4. The proposed block continues through the consensus process.
   1. If ⅔ of validator nodes vote to confirm the block, then the block is committed and saved to the onchain databases of all validators and full nodes.
   2. If the proposed block does not successfully hit the ⅔ threshold, then the block is rejected.
5. After the block is committed, the updated onchain (and offchain) data is streamed from full nodes to Indexers. The Indexer then makes this data available via API and Websockets back to the front end and/or any other outside services querying for this data.


# File: v4-documentation/old-docs/pages/concepts-architecture/indexer.md

# Indexer Deep Dive

A good way to think about the indexer is as similar to Infura or Alchemy’s role in the Ethereum ecosystem. However, unlike Infura/Alchemy, and like everything else in dYdX Chain, the Indexer is completely open source and can be run by anyone!

### What is the Indexer?

As part of tooling for the dYdX ecosystem, we want to ensure that clients have access to performant data queries when using exchanges running on dYdX Chain software. Cosmos SDK Full Nodes offer a number of APIs that can be used to request onchain data. However, these Full Nodes are optimized for committing and executing blocks, not for serving high frequency, low-latency requests from web/mobile clients.

This is why we wrote software for an indexing service. The Indexer is a read-only service that serves off chain data to clients over REST APIs and Websockets. Its purpose is to store and serve data that exists on dYdX Chain in an easier to use way. In other words, the purpose of an indexer is to index and serve data to clients in a more performant, efficient and web2-friendly way. For example the indexer will serve websockets that provide updates on the state of the orderbook and fills. These clients will include front-end applications (mobile and web), market makers, institutions, and any other parties looking to query dYdX Chain data via a traditional web2 API.

### Onchain vs. Offchain data

The Indexer will run two separate ingestion/storage processes with data from a v4 Full Node: one for onchain data and one for offchain data. Currently, throughput of onchain data state changes is expected to be from 10-50 events/second. On the other hand, the expected throughput of offchain data state changes is between 500-1,000 events/second. This represents a 10-100x difference in throughput requirements. By handling these data types separately, v4 is built to allow for different services to better scale according to throughput requirements.

### Onchain Data

Onchain data is all data that can be reproduced by reading committed transactions on a dYdX Chain deployment. All onchain data has been validated through consensus. This data includes:

1. Account balances (USDC)
2. Account positions (open interest)
3. Order Fills 
    1. Trades 
    2. Liquidations
    3. Deleveraging
    4. Partially and completely filled orders
4. Funding rate payments
5. Trade fees
6. Historical oracle prices (spot prices used to compute funding and process liquidations)
7. Long-term order placement and cancellation
8. Conditional order placement and cancellation

### Offchain Data

Offchain data is data that is kept in-memory on each v4 node. It is not written to the blockchain or stored in the application state. This data cannot be queried via the gRPC API on v4 nodes, nor can it be derived from data stored in blocks. It is effectively ephemeral data on the v4 node that gets lost on restarts/purging of data from in-memory data stores. This includes:

1. Short-term order placement and cancellations
2. Order book of each perpetual exchange pair
3. Indexed order updates before they hit the chain

## Indexer Architecture

![image](https://github.com/dydxprotocol/v4-documentation/assets/130097657/8fc9842f-49e7-430f-a1f0-969c72489b28)

The Indexer is made up of a series of services that ingest information from v4 Full Nodes and serve that information to various clients. Kafka topics are used to pass events/data around to the services within the Indexer. The key services that make up Indexer are outlined below.

### Ender (Onchain ingestion)

Ender is the Indexer’s onchain data ingestion service. It consumes data from the “to-ender” Kafka topic (which queues all onchain events by block) and each payload will include all event data for an entire block. Ender takes all state changes from that block and applies them to a Postgres database for the Indexer storing all onchain data. Ender will also create and send websocket events via a “to-websocket-?” Kafka topic for any websocket events that need to be emitted.

### Vulcan (Offchain ingestion)

Vulcan is the Indexer’s offchain data ingestion service. It will consume data from the “to-vulcan” Kafka topic (queues all offchain events), which will carry payloads that include active order book updates, place order updates, cancel order updates, and optimistic fills. This data will be stored in a Redis cache. Vulcan will update Redis with any new open orders, set the status of canceled orders to cancel pending, and update orderbooks based on the payload received. Vulcan will also update Postgres whenever a partially filled order is canceled to update the state of the order in Postgres. Vulcan will also create and send websocket events via a “to-websocket-?” Kafka topic for any websocket events that need to be emitted.

### Comlink (API Server)

Comlink is an API server that will expose REST API endpoints to read both onchain and offchain data. For example, a user could request their USDC balance or the size of a particular position through Comlink, and would receive a formatted JSON response.

As an explicit goal set out by the dYdX team, we’re designing v4 APIs to closely match the [v3 APIs](https://dydx.exchange/blog/v4-deep-dive-indexer#:~:text=closely%20match%20the-,v3%20exchange%20APIs,-.%20We%20have%20had). We have had time to gather feedback and iterate on these APIs over time with v3, and have confidence that they are reasonable at the product-level.

### Roundtable

Roundtable is a periodic job service that provides required exchange aggregation computations. Examples of these computations include: 24h volume per market, open interest, PnL by account, candles, etc. 

### Socks (Websocket service)

Socks is the Indexer’s websockets service that allows for real-time communication between clients and the Indexer. It will consume data from ender, vulcan, and roundtable, and send websocket messages to connected clients.

## Hosting & Deploying the Indexer

In service of creating an end-to-end decentralized product, the Indexer will be open source.  This will include comprehensive documentation about all services and systems, as well as infrastructure-as-code for running the Indexer on popular cloud providers. 

The specific responsibilities of a third party operator looking to host the Indexer generally include initial deployment and ongoing maintenance. 

Initial deployment will involve: 

- Setting up AWS infrastructure to utilize the open-source repo.
- Deploying Indexer code to ingest data from a full-node and expost that information through APIs and websockets
- Datadog (provides useful metrics and monitoring for Indexer services), and Bugsnag (real-time alerting on bugs or issues requiring human intervention).

Maintenance of the Indexer will involve:

- Migrating and/or upgrading the Indexer for new open-source releases
- Monitoring Bugsnag and Datadog for any issues and alerting internal team to address
- Debugging and fixing any issues with a run book provided by dYdX

dYdX believes that, at minimum, a DevOps engineer will be required to perform the necessary duties for deployment and maintenance of the Indexer. An operator will need to utilize the services below: 

- AWS
    - ECS - Fargate
    - RDS - Postgres Database
    - EC2
    - Lambda
    - ElastiCache Redis
    - EC2 ELB - Loadbalancer
    - Cloudwatch - Logs
    - Secret Manager
- Terraform Cloud - for deploying to the cloud
- Bugsnag - bug awareness
- Datadog - metrics and monitoring
- Pagerduty - alerting

Operators should be able to host the open-sourced Indexer for public access in a highly available (i.e., high uptime) manner. Requirements include owning accounts to the services above and hiring the appropriate personnel to perform deployment and maintenance responsibilities. 


# File: v4-documentation/old-docs/pages/api_integration-deposits_and_withdrawals/cli_commands.md

## CLI commands

Note: Native token denoms for transfer amounts and fees can be found [here](../infrastructure_providers-network/network_constants.mdx#native-token-denom)

### Deposit to Subaccount

The below cmd allows depositing funds into a subaccount (`x/subaccounts`) from a sender's `x/bank` account. 
Typically, this cmd is used to self deposit, which can be done by setting the sender and recipient address to be the same address, as in the provided example.
```bash
dydxprotocold tx sending deposit-to-subaccount <sender_key_or_address> <recipient_address> <recipient_subaccount_number> <quantums> [flags]
```

Example:
```bash
dydxprotocold tx sending deposit-to-subaccount dydx1g2ygh8ufgwwpg5clp2qh3tmcmlewuyt2z6px8k dydx1g2ygh8ufgwwpg5clp2qh3tmcmlewuyt2z6px8k 0 <usdc_quantum_uint64> --keyring-backend test --fees 5000000000000000<native_token_denom>
```


### Withdraw from Subaccount

The below cmd allows withdrawing funds from a subaccount (`x/subaccounts`) to a sender's `x/bank` account.
Typically, this cmd is used to self withdraw, which can be done by setting the sender and recipient address to be the same address, as in the provided example.
```bash
dydxprotocold tx sending withdraw-from-subaccount <sender_key_or_address> <sender_subaccount_number> <recipient_address> <quantums> [flags]
```

Example:
```bash
dydxprotocold tx sending withdraw-from-subaccount dydx1g2ygh8ufgwwpg5clp2qh3tmcmlewuyt2z6px8k 0 dydx1g2ygh8ufgwwpg5clp2qh3tmcmlewuyt2z6px8k <usdc_quantum_uint64> --keyring-backend test --fees 5000000000000000<native_token_denom>
```

# File: v4-documentation/old-docs/pages/api_integration-deposits_and_withdrawals/how_to_send_usdc_from_ethereum_to_dydx.md

# How to send USDC from Ethereum to dYdX

## Deployments
| Deployment         | Chain ID       | USDC Native Chain | USDC_ERC20_ADDRESS                                                                                                            | TOKEN_MESSENGER_CONTRACT_ADDRESS                                                                                              |
| ------------------ | -------------- | ----------------- | ----------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| DYDX token holders | dydx-mainnet-1 | Ethereum          | [0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48](https://etherscan.io/address/0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48)         | [0xBd3fa81B58Ba92a82136038B25aDec7066af3155](https://etherscan.io/address/0xbd3fa81b58ba92a82136038b25adec7066af3155)         |
| Testnet            | dydx-testnet-4 | Sepolia Testnet   | [0x1c7D4B196Cb0C7B01d743Fbc6116a902379C7238](https://sepolia.etherscan.io/address/0x1c7D4B196Cb0C7B01d743Fbc6116a902379C7238) | [0x9f3B8679c73C2Fef8b59B4f3444d4e156fb70AA5](https://sepolia.etherscan.io/address/0x9f3B8679c73C2Fef8b59B4f3444d4e156fb70AA5) |

> **Note:** the example values in the steps below align with the **deployment by DYDX token holders**.

## Requirements
1. Your wallet is on the Ethereum network.
2. You have sufficient ETH for gas and USDC.

## Prerequisite USDC Approval
1. First, go to `USDC_ERC20_ADDRESS`'s `writeProxyContract` tab [https://etherscan.io/token/0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48#writeProxyContract](https://etherscan.io/token/0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48#writeProxyContract)
2. Click the “Connect to Web3” button
![Connect to Web3](../../artifacts/how_to_send_usdc_to_dydx_connect_web3_1.png)
![Connect to Web3 Disclaimer](../../artifacts/how_to_send_usdc_to_dydx_connect_web3_2.png)
![Connect Wallet](../../artifacts/how_to_send_usdc_to_dydx_connect_web3_3.png)
3. Now it turns green.
![Connected](../../artifacts/how_to_send_usdc_to_dydx_connect_web3_4.png)
4. Click on the first line `1. Approve (0x095ea7b3)` to expand it, input `0xbd3fa81b58ba92a82136038b25adec7066af3155` (the `TOKEN_MESSENGER_CONTRACT_ADDRESS`) in the spender (address) box and `115792089237316195423570985008687907853269984665640564039457584007913129639935` in the second box (value (`uint256`)) for unlimited. You can specify a smaller number here as well.
![Approve](../../artifacts/how_to_send_usdc_to_dydx_approve.png)
5. Click the `Write` button.

## Procedure
1. Starting with code provided here: [https://github.com/bd21/noble-tutorials/tree/master/tutorials/05-eth-noble-python](https://github.com/bd21/noble-tutorials/tree/master/tutorials/05-eth-noble-python), a few changes have been made to allow you to specify: `(1) a dYdX Chain address`, and `(2) the USDC amount`. Here is a diff showing the differences:
![Script Diff](../../artifacts/how_to_send_usdc_to_dydx_script_diff.png)
2. Save the source code (last section of this document) as `deposit_for_burn.py`, create a directory called `abi/`, and download `TokenMessengerWithMetadata.json` from the `abi/` directory at github above, and save it into `abi/`. You now have the following files in the working directory.
```bash
./deposit_for_burn.py
./abi/TokenMessengerWithMetadata.json
```
3. Run the program like this: 
```bash
python3 deposit_for_burn.py <dydxaddress> <burnamount>
```
where `<dydxaddress>` is your dYdX-Chain address and `<burnamount>` is the amount of USDC. For example:
```bash
python3 deposit_for_burn.py dydx1gem4xs643fjhaqvphrvv0adpg4435j7xx9pp4z 100
```
4. Be patient. It may take up to 30 minutes to see the funds show up on the Noble blockchain. After that you can connect your wallet to v4 and it will sweep the funds from Noble into v4.

## Source Code
```python
import hexbytes
from web3 import Web3
import bech32
from pprint import pprint
from sys import argv


TOKEN_MESSENGER_CONTRACT_ADDRESS = "0xbd3fa81b58ba92a82136038b25adec7066af3155"
USDC_ERC20_ADDRESS = "0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48"

########################## YOU FILL THIS OUT #################
private_key = '<FILL_THIS_OUT>'
RPC_URL = '<FILL_THIS_OUT>'
##############################################################

# requires a local file named 'private_key' with a hex encoded eth private key (no 0x prefix)
def deposit_for_burn(noble_address, dydx_address):
    # initialize client
    web3 = Web3(Web3.HTTPProvider(RPC_URL))
    assert web3.is_connected()

    # initialize account, smart contract
    account = web3.eth.account.from_key(private_key)
    file = open("abi/TokenMessenger.json")
    abi = file.read()

    contract_address = str(web3.to_checksum_address(TOKEN_MESSENGER_CONTRACT_ADDRESS))
    contract = web3.eth.contract(address=contract_address, abi=abi)

    print("Building Ethereum depositForBurn txn...")

    mint_recipient = convert(noble_address)  # intermediate noble minting address
    print("Derived Noble address: " + noble_address)

    burn_amount = int(burn_amount1) * 1000000
    usdc_address = str(Web3.to_checksum_address(USDC_ERC20_ADDRESS))

    print("Broadcasting...")

    call_function = contract.functions.depositForBurn(
        burn_amount,
        4,  # noble
        mint_recipient,
        usdc_address
    ).build_transaction({
        "chainId": web3.eth.chain_id,
        "from": account.address,
        "nonce": web3.eth.get_transaction_count(account.address),
    })
    signed_tx = web3.eth.account.sign_transaction(call_function, private_key=private_key)

    # Send the raw transaction:
    tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
    tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
    # print("eth tx hash: https://etherscan.io/tx/" + tx_hash.hex())
    print("eth tx hash: https://goerli.etherscan.io/tx/" + tx_hash.hex())
    print("eth tx receipt: ")
    pprint(tx_receipt)

    # print("Minting to https://testnet.mintscan.io/noble-testnet/account/" + noble_address)
    print("Minting to https://mintscan.io/noble/account/" + noble_address)


# Convert bech32 address to a format suited for CCTP
def convert(address) -> hexbytes.HexBytes:
    result = bytearray(32)
    decoded = bech32.convertbits(
        data=bech32.bech32_decode(address)[1],
        frombits=5,
        tobits=8,
        pad=False
    )
    result[32 - len(decoded):] = decoded
    return hexbytes.HexBytes(result)

if len(argv) < 3:
        print('Error: Please specify dydxaddress and burnamount')
        exit()
dydx_address1 = argv[1]
burn_amount1 = argv[2]
noble_address1 = bech32.bech32_encode("noble", bech32.bech32_decode(dydx_address1)[1])

if __name__ == "__main__":
    deposit_for_burn(
        noble_address=noble_address1,
        dydx_address=dydx_address1
    )
    # alternatively, you can derive the noble address
    # deposit_for_burn(
    #     dydx_address="dydx1kgjgvl3xer7rwskp6tlynmjrd2juas6nqxn8yg",
    #     noble_address=bech32.bech32_encode("noble", bech32.bech32_decode("dydx1kgjgvl3xer7rwskp6tlynmjrd2juas6nqxn8yg")[1]),
    # )
```


# File: v4-documentation/old-docs/pages/api_integration-deposits_and_withdrawals/rate_limits_and_gating.md

# Withdrawal rate limits and gating

In an effort to reduce risk across the protocol, withdrawals can be rate limited and gated in specific circumstances. 
​

## Withdrawal rate limits

As a default setting, withdrawals of Noble USDC are rate limited to ```max(1% of TVL, $1mm) per hour```

As a default setting, withdrawals of Noble USDC are rate limited to ```max(10% of TVL, $10mm) per day```

These rate limit parameters can be updated by governance.

 

## Withdrawal gating

All subaccount transfers and withdrawals will be gated for 50 blocks if a negative collateralized subaccount is seen in state and/or can't be liquidated or deleveraged

All subaccount transfers and withdrawals will also be gated for 50 blocks if a 5+ minute chain outage occurs.


# File: v4-documentation/old-docs/pages/users-rewards/overview.md

# Overview

![Rewards Overview](../../artifacts/rewards_overview.png)

There are several reward mechanisms available with the protocol software.

|                 | Target Users         | Rewards paid in     | Claim Process | Frequency               |
| --------------- | -------------------- | ------------------- | ------------- | ----------------------- |
| Staking Rewards | Validators & Stakers | USDC & NATIVE_TOKEN | Manual        | Per Block               |
| Trading Rewards | Traders              | NATIVE_TOKEN        | Automatic     | Per Block (with trades) |

## Staking Rewards

- Rewards distributed to `Validators` and `Stakers` (= Delegators)
- `Staking Rewards = Trading Fees + Gas Fees - Community Tax - Validator Commission`
- Distributed automatically every block
- Must be claimed manually

## Trading Rewards

- Rewards distributed to `Traders` after each successful trade
- Based on a specified `formula` with several inputs
- Distributed automatically every block with successful trades
- Claimed automatically


# File: v4-documentation/old-docs/pages/users-rewards/staking_rewards.md

# Staking Rewards

Staking rewards are designed to reward `Validators` and `Stakers` (=Delegators). The sources of staking rewards are trading fees and gas fees collected by the protocol.

The protocol uses the [CosmosSDK’s x/distribution module](https://docs.cosmos.network/main/build/modules/distribution) to allocate the accrued trading and gas fees to `Validators` and `Stakers`.

![Staking Rewards](../../artifacts/staking_rewards.png)

All trading fees (`USDC`) and gas fees (`USDC` and `NATIVE_TOKEN`) collected by the protocol are accrued and distributed within a block. Specifically — for each block, the fees generated are collected in `fee_collector` module account and then sent to the `distribution` module account in the following block. Then, the `community_tax` and `validator_commission` are subtracted from the collected pool and the resulting amount will be distributed to `Validators` and `Stakers` in accordance with their staked token amount.

>💡 Note that `Stakers` must claim the rewards manually. Unclaimed rewards will remain in the distribution module account until they are claimed.

## Details

```
Staking Rewards = 
   fee pool * (# of delegator's staked tokens / total # of staked tokens) 
   * (1 - community tax rate) * (1 - validator commission rate)
```

The details of how the Staking Rewards are calculated can be found in the [CosmosSDK’s x/distribution documentation](https://docs.cosmos.network/main/build/modules/distribution#the-distribution-scheme).

## Parameters

>💡 The current configuration and parameters can be found by querying the network.

- `x/distribution: community_tax` : specifies the proportion of fee pool that should be sent to `community_treasury` before staking rewards are distributed. This value can be configured via gov.
- `x/staking: validator_commission` : specifies the proportion of the staking rewards that a given validator will take from delegator’s reward. This is configured per validator and can be updated by the validator.

See [CosmosSDK doc](https://docs.cosmos.network/main/build/modules/distribution#params) for details.


# File: v4-documentation/old-docs/pages/users-rewards/trading_rewards.md

# Trading Rewards

Trading rewards are designed to incentivize `Traders` to trade on the protocol. The source of trading rewards is a configured `Rewards Treasury` account.

For each successful trade, `Traders` will be rewarded in `NATIVE_TOKEN` based on the formula outlined in the below section. Trading rewards are distributed automatically and directly to the trader’s account per block.

## Motivation

**The primary goal behind trading rewards is to incentivize trading on the protocol.**

To facilitate fair trading behaviors and to preserve the protocol’s safety, trading rewards have the following secondary goals:

- Self-trading should not be profitable
- Any distributed rewards should be proportional to fees paid to the protocol
- Trading rewards should be deterministic
- Trading rewards should be settled and distributed every block
- Trading rewards should limit the protocol overspending on trading activity

## Details

![Trading Rewards](../../artifacts/trading_rewards.png)

### Reward Treasury

The amount of tokens available to be distributed to traders is tracked by the protocol’s configured Rewards Treasury account. Call the size of this Rewards Treasury `T`. 

Each block, new tokens are transferred into this `T` from the vesting account and rewards are then distributed from `T`. 

Each block, `T` can grow or shrink based on protocol activity.

### Reward Treasury Vesting

The protocol’s default vesting behavior is to linearly vest `denom` tokens from `vester_account` to `treasury_account` from `start_time` to `end_time`.

The above is configured via `VestEntry`.

### Formula & Emission

Let `A` represent the amount of rewards that are distributed from this `T` to traders in a given block.

We define a trader X’s `rewards score` in a given block as:

![Trading Rewards Formula 1](../../artifacts/trading_rewards_formula_1.png)

Let `S` be the sum of all the rewards scores across all traders for a given block. `S` is given by:

![Trading Rewards Formula 2](../../artifacts/trading_rewards_formula_2.png)

Every block, the amount `A` of the native token that is distributed to traders is defined as:

![Trading Rewards Formula 3](../../artifacts/trading_rewards_formula_3.png)

Where `C` is a constant configurable via governance.

The amount remaining `(T - A)` is retained in the Rewards Treasury and new tokens are emitted into the Rewards Treasury the following block.

`A` is calculated and distributed to all the takers who traded in the block and `(T - A)` is rolled over and retained in the Rewards Treasury for the next block.

The rewards distributed, `A`, are allocated proportional to each trader’s score.

## FAQ

**How do trading rewards affect potential inflation of the governance token?**

Trading rewards distributed by the protocol, each block, are capped at the dollar equivalent of the total net trading fees generated by the protocol that block. Thus, trading rewards distributed can fluctuate on a block by block basis.

This can result in a large amount of “savings” by the protocol (via reduced inflation) by not overspending to incentivize trading activity.

## Parameters / Configurations

> 💡 The current configuration and parameters can be found by querying the network.


### Rewards

- `treasury_account`: referred to as `T` in the above. specifies which account the trading rewards come from. Can be configured via gov.
- `denom`: specifies the token that the trading rewards should use. Can be configured via gov.
- `fee_multiplier_ppm`: referred to as `C` in the above. Specifies the proportion (in ppm) that fees should be multiplied by to get the maximum rewards amount. Can be configured via gov.

### Vest

- `VestEntry` : specifies a vesting schedule from `vester_account` to `treasury_account` for a given `denom` token. The vesting happens linearly from `start_time` and `end_time`.


# File: v4-documentation/old-docs/pages/user-guides/how_to_troubleshoot_withdrawals_and_deposits.md

# dYdX Chain: Deposits, Withdrawals & Troubleshooting Guide

This guide provides a **step-by-step** explanation of deposit and withdrawal processes on the dYdX Chain. It includes instructions for **Skip Go Fast (“Instant”), Skip Go (“Default”), Coinbase deposits**, and **direct IBC transfers**, along with **troubleshooting methods** and best practices to ensure seamless transactions.

## Deposit & Withdrawal Methods

| Method                                           | Description                                                               | Finality      | Chains Supported                                                                                | Fee Range (USD)                                                                                                                         |
| :----------------------------------------------- | :------------------------------------------------------------------------ | :------------ | :---------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------- |
| **Skip Go Fast ("Instant Deposit")**             | The fastest bridging option for rapid deposits                            | 10-30 seconds | Ethereum Mainnet, Arbitrum, Optimism, Base, Polygon, Avalanche                                  | 10 bps on the transfer size \+ source chain fee: Ethereum: \~$2.5 L2s: $0.01-$0.10                                                      |
| **Skip Go ("Default")**                          | A universal interoperability platform supporting multiple bridges         | 2-30 minutes  | Ethereum Mainnet, Arbitrum, Optimism, Base, Polygon, Avalanche, Solana, Neutron, Osmosis, Noble | Deposits \~$0.02 Withdrawals: \~$0.1-$7 \+ source chain gas fee: Ethereum: gas price L2s: gas price Cosmos: gas price Solana: gas price |
| **Deposit / Withdrawal with Coinbase via Noble** | Direct deposit or withdrawal via Noble Wallet with automatic IBC transfer | 1-3 minutes   | Coinbase to dYdX only                                                                           | Coinbase withdrawal fee \+ IBC fee ($0.1-$0.2)                                                                                          |
| **Direct IBC Transfer**                          | For users familiar with Cosmos ecosystem transfers                        | 15-30 seconds | All Cosmos chains with IBC enabled                                                              | \~$0.1-0.5                                                                                                                              |

### 1\. Skip Go Fast ("Instant Deposit")

Skip Go Fast is a **decentralized bridging protocol**, developed by **Skip**, that enables **rapid and secure cross-chain transactions** across major blockchain ecosystems such as Ethereum, Cosmos, and Solana. Go Fast accelerates cross-chain actions by up to 25 times, **reducing onboarding times from 10+ minutes to seconds**. Learn more [here](https://docs.skip.build/go/advanced-transfer/go-fast#go-fast).

#### Supported Chains & Assets

- **Chains:** Ethereum Mainnet, Arbitrum, Avalanche, Base, Optimism, Polygon
- **Assets:** USDC, ETH, POL

#### Minimum & Maximum Transfer Sizes

| Source Chain     | Min Transfer (USD) | Max Transfer (USD) |
| ---------------- | ------------------ | ------------------ |
| Ethereum Mainnet | 50                 | 25,000             |
| Arbitrum         | 1                  | 25,000             |
| Base             | 1                  | 25,000             |
| Optimism         | 1                  | 25,000             |
| Polygon          | 1                  | 25,000             |

For the latest Minimum & Maximum Transfer Sizes, checkout the Skip API [documents](https://docs.skip.build/go/advanced-transfer/go-fast#what-are-the-minimum-and-maximum-transfer-sizes-for-go-fast%3F).

**Note:** If starting with an asset that is not USDC, Skip Go will swap the asset to USDC on the source chain, and the post-swap amount is used to determine if it falls within the min/max transfer size limits.

#### Fees

All Skip Go Fast

10 bps on the transfer size \+ source chain fee:

| Source Chain     | Fee (USD)                          |
| ---------------- | ---------------------------------- |
| Ethereum Mainnet | \~$2.5 (depends on gas fees)       |
| Arbitrum         | \~$0.01-$0.1 (depends on gas fees) |
| Base             | \~$0.01-$0.1 (depends on gas fees) |
| Optimism         | \~$0.01-$0.1 (depends on gas fees) |
| Polygon          | \~$0.01-$0.1 (depends on gas fees) |

For the latest source chain fees, checkout the Skip API [documents](https://docs.skip.build/go/advanced-transfer/go-fast#what-is-the-fee-model-for-go-fast%3F).

#### Process Flow (Deposit)

1. **Connect your wallet** to the dYdX interface and navigate to the "Deposit" section
2. **Enter the amount** you wish to transfer (ensure it meets minimum requirements)
3. **Select “Instant”** as your deposit method
4. **Choose the source chain and asset** you wish to deposit
5. **Review the transaction details** including estimated fees and finality time
6. **Confirm and sign** the transaction from your wallet
7. **Skip Go Fast protocol's solvers** monitor for confirmation of fund arrival at Noble
   - _Note: This process relies on Skip's decentralized solver network_
   - _If your source token is not USDC, an automatic swap occurs via integrated DEXs_
8. **Once confirmed**, funds are automatically **sent to dYdX Chain** via IBC transfer
   - _This step uses Cosmos IBC relayers to complete the cross-chain transfer_
9. **Final step:** Funds are **moved from the main account to the subaccount for trading**
   - _This internal transfer is handled by dYdX Chain’s infrastructure_

#### Example Deposit (Base → dYdX via Skip Go Fast)

```
{
    "operations": [
        {
            "evm_swap": {
                "from_chain_id": "8453",
                "denom_in": "base-native",
                "denom_out": "USDC",
                "amount_in": "10511954965182950",
                "amount_out": "21430265",
                "swap_venues": [
                    {"name": "base-uniswap"}
                ]
            }
        },
        {
            "cctp_transfer": {
                "from_chain_id": "8453",
                "to_chain_id": "noble-1",
                "denom_in": "USDC",
                "denom_out": "uusdc",
                "bridge_id": "CCTP"
            }
        },
        {
            "transfer": {
                "from_chain_id": "noble-1",
                "to_chain_id": "dydx-mainnet-1",
                "denom_in": "uusdc",
                "denom_out": "ibc/USDC",
                "bridge_id": "IBC"
            }
        }
    ]
}
```

#### How Skip Go Fast Works

Skip Go Fast uses an innovative solver-based approach to achieve near-instant finality:

1. **User Intent Submission**
   - When you initiate a transfer, you call the `submitOrder` function on the protocol contract
   - This broadcasts your intent to transfer assets across chains
   - Your intent specifies the assets, destination address, and any additional message payload
2. **Solver Network**
   - Permissionless participants called "solvers" watch for these intents
   - Solvers evaluate whether they can fulfill your intent based on:
     - Their available liquidity on the destination chain
     - Potential reward for fulfilling the intent
   - When a solver agrees to fulfill your intent, they use their own capital to front the assets
3. **Instant Fulfillment**
   - The solver calls the `fillOrder` function on the destination chain
   - This transfers the specified assets and processes any additional actions
   - From your perspective, the assets appear on the destination chain almost instantly
4. **Settlement Process**
   - After fulfilling your transfer, the solver initiates settlement to recover their fronted assets
   - The protocol verifies the solver's actions via a cross-chain messaging system
   - Once confirmed, the solver receives their assets back plus any earned fees
   - This settlement happens in the background and doesn't affect your user experience.

### 2\. Skip Go ("Normal")

Skip Go API is a **universal interoperability platform**, allowing **seamless swaps and transfers** across multiple blockchain ecosystems via **bridges such as CCTP and Axelar**.

Supported Chains & Assets

- **Chains:** Ethereum Mainnet, Arbitrum, Avalanche, Base, Optimism, Polygon, Solana, and Cosmos chains
- **Assets:** USDC, ETH, POL

#### Minimum & Maximum Transfer Sizes

| Source Chain     | Min Transfer (USD) | Max Transfer (USD) |
| ---------------- | ------------------ | ------------------ |
| Ethereum Mainnet | \~$0.05            | \~$1,000,000       |
| Other EVM Chains | \~$0.05            | \~$1,000,000       |
| Solana           | \~$0.05            | \~$1,000,000       |
| Cosmos Chains    | \~$0.05            | \~$1,000,000       |

####Fees  
Source chain gas fees \+ Deposits \~$0.02 Withdrawals: \~$0.1-$7

| Source Chain     | Fee (USD)                               |
| ---------------- | --------------------------------------- |
| Ethereum Mainnet | Deposits \~$0.02 Withdrawals: \~$0.1-$7 |
| Other EVM Chains | Deposits \~$0.02 Withdrawals: \~$0.1-$7 |
| Solana           | Deposits \~$0.02 Withdrawals: \~$0.1-$7 |
| Cosmos Chains    | Deposits \~$0.02 Withdrawals: \~$0.1-$7 |

#### Process Flow (Deposit)

1. **Connect your wallet** to the dYdX interface and navigate to the "Deposit" section
2. **Enter the amount** you wish to transfer (First time 1.25 USDC will be kept in wallet for gas fees)
3. **Select “Normal”** as your deposit method
4. **Choose source chain and asset** you wish to deposit
5. **Review the transaction details** including estimated fees and finality time
6. **Confirm and sign** the transaction from your wallet
7. **Third-party protocol interactions begin:**
   - _If your source token is not USDC, an automatic swap occurs via integrated DEXs_
   - _Funds are sent to bridge contracts (CCTP, Axelar, etc.) based on optimal route_
   - _These bridges rely on external validators and relayers to verify cross-chain transactions_
8. **Wait for confirmation** across all involved networks (may take 10-20 minutes)
   - _Multiple relayer networks and validators must reach consensus_
   - _Each bridge and network has its own finality period_
9. **Once confirmed**, funds are available in your dYdX account
   - _Relayers monitor and trigger the final IBC transfer to dYdX Chain_

#### Example Deposit (Ethereum → dYdX via Skip Go)

```
{
    "operations": [
        {
            "cctp_transfer": {
                "from_chain_id": "1",
                "to_chain_id": "noble-1",
                "denom_in": "USDC",
                "denom_out": "uusdc",
                "bridge_id": "CCTP"
            }
        },
        {
            "transfer": {
                "from_chain_id": "noble-1",
                "to_chain_id": "dydx-mainnet-1",
                "denom_in": "uusdc",
                "denom_out": "ibc/USDC",
                "bridge_id": "IBC"
            }
        }
    ]
}
```

### 3\. Deposit with Coinbase

**Coinbase deposits** involve an **automatic Noble Wallet to dYdX IBC transfer** without needing a third-party bridge.

Process Flow (Deposit)

1. **On dYdX, select "Coinbase" to display the Noble address associated with the trader's dYdX address.**
   - The trader can then scan the QR code on Coinbase using the Coinbase QR code scanner, or copy and paste the Noble address into the destination address on the Coinbase withdrawal modal. Traders should make sure the Noble address is correct when depositing from Coinbase.
2. **Open Coinbase app** and navigate to the USDC asset page
3. **Select "Send"** and choose "Coinbase Pay" as the destination
4. **Enter your Noble address wallet address** (starts with "noble1...")
5. **Enter the amount** you wish to transfer
6. **Confirm the transaction** in Coinbase
7. **Wait for confirmation** (typically 1-3 minutes)
   - _Note: This process relies on Coinbase's infrastructure and Noble's IBC integration_
   - _Coinbase handles the initial funds transfer to Noble's USDC hub_
8. **Funds will automatically route** through Noble to dYdX via IBC
   - _This automatic routing uses the IBC relayer network_
   - _No swaps occur in this process as USDC moves directly between compatible chains_

#### Example Deposit (Coinbase → dYdX)

```
{
    "operations": [
        {
            "transfer": {
                "from_chain_id": "noble-1",
                "to_chain_id": "dydx-mainnet-1",
                "denom_in": "uusdc",
                "denom_out": "ibc/USDC",
                "bridge_id": "IBC"
            }
        }
    ]
}
```

### 4\. Direct IBC Transfer

For users familiar with the Cosmos ecosystem, direct IBC transfers provide a straightforward method to deposit funds.

Supported Cosmos Chains

- Osmosis
- Cosmos Hub
- Kujira
- Noble
- Injective
- And other IBC-enabled chains

#### Process Flow (Deposit)

1. **Open your Cosmos wallet** (Keplr, Leap, etc.)
2. **Navigate to the IBC Transfer section**
3. **Select dYdX Chain as the destination**
4. **Enter your dYdX wallet address**
5. **Enter the amount** you wish to transfer
6. **Confirm the transaction**
7. **IBC relayer network processes the transfer:**
   - _IBC relayers run by validators and third-party services handle the cross-chain message delivery_
   - _No centralized entity controls this process; it's based on the Cosmos IBC protocol_
   - _If transferring a non-native token, ensure it's an IBC-supported asset on both chains_
8. **Wait for confirmation** (typically 15-30 seconds)
   - _Faster than bridging solutions as it doesn't require multi-chain consensus_

#### Withdrawal Process

Withdrawing from dYdX Chain requires first moving funds from your trading subaccount to your main account before bridging to your destination chain.

Step-by-Step Withdrawal Guide

1. **Connect your wallet** to the dYdX interface
2. **Navigate to "Portfolio" \> "Balances"**
3. **Navigate to "Withdraw" section**
4. **Select your preferred withdrawal method:**
   - Skip Go (for more chain options)
   - Direct IBC Transfer (for Cosmos destinations)
5. **Choose destination chain and asset**
   - _If withdrawing to a non-USDC token, a swap will be executed by third-party DEXs_
6. **Enter withdrawal amount (minimum 11 USDC)**
7. **Review transaction details**
   - _Pay attention to the relayers and bridges involved in your specific route_
8. **Confirm and sign the transaction**
9. **Third-party services process your withdrawal:**
   - _For Skip methods: Relayers monitor for your transaction and execute cross-chain transfers_
   - _For IBC transfers: IBC relayer network handles the IBC_
   - _Multiple validators may need to confirm your transaction depending on the route_
10. **Wait for confirmation** across all networks
    - _Timeframes vary based on network congestion and the third-party services involved_

#### Withdrawal Timeframes

| Withdrawal Method | Approximate Time |
| ----------------- | ---------------- |
| Skip Go           | 1-5 minutes      |
| Direct IBC        | 30 seconds       |

## **Troubleshooting**

### **Common Deposit Issues**

1. **Funds not appearing in your dYdX account**
   - Verify transaction succeeded on source blockchain explorer
   - Check Noble explorer for IBC transfer confirmation
   - Ensure you've connected the correct wallet to dYdX interface; this is important for the autosweeping to happen from noble to dYdX chain and to sweep into your dYdX subaccount
   - Check [Range Tracker Tool](https://usdc.range.org/usdc) to see if relayers have picked up your transaction
   - Wait at least 30 minutes for all confirmations to complete
2. **Transaction stuck or pending**
   - For EVM chains, check if gas price was too low
   - Verify if transaction was rejected on source chain
   - For Skip bridges, check status on [Range](https://usdc.range.org/usdc) to see if relayers have picked up your transaction
   - Check if relayer networks are experiencing delays or outages
   - Verify all involved third-party services are operational
3. **Insufficient funds error**
   - Ensure you're accounting for network fees in addition to transfer amount
   - Verify minimum transfer requirements are met
   - For swaps, account for price impact and slippage
4. **Failed at swap stage**
   - Check if the DEX had sufficient liquidity for your swap
   - Verify slippage settings were appropriate for market conditions
   - Consider trying another deposit method that doesn't require a swap

### **Bridge-Specific Troubleshooting**

For detailed troubleshooting guides specific to each bridge, please refer to:

1. **Skip Transaction Troubleshooting**
   - [Skip Documentation Portal](https://docs.skip.money)
   - Input _tx_hash_ and source chain _chain_id_ into [Skip API](https://docs.skip.build/go/api-reference/prod/transaction/get-v2txstatus?playground=open)
2. **CCTP Troubleshooting Guide**
   - [dYdX CCTP Documentation](https://dydx.exchange/blog/cctp)
   - [Circle CCTP Status Page](https://status.circle.com)
   - [USDC Tracker Tool](https://usdc.range.org/usdc)
   - **dYdX Chain Explorer**: [https://www.mintscan.io/dydx](https://www.mintscan.io/dydx)
   - **Noble Chain Explorer**: [https://www.mintscan.io/noble](https://www.mintscan.io/noble)
   - **Source Chain Explorer**: Etherscan, Arbiscan, etc.
3. **IBC Transfer Issues**
   - [Mintscan IBC Explorer](https://www.mintscan.io/ibc)
   - [IBC Relayer Status](https://ibc.range.org)
4. **Relayer issues**
   - Check status pages for relayer networks involved in your transaction
   - Wait for relayer networks to resume normal operation if experiencing downtime
   - Consider using an alternative deposit method if persistent issues occur

If you encounter persistent bridging issues, follow these steps:

1. **Identify where your funds are currently located**
   - Use block explorers for each relevant chain (source, Noble, dYdX)
   - For Skip transactions, check the `transfer_asset_release` field in the API response
2. **Try manual recovery methods if needed**
   - For IBC: Use Keplr or Leap wallet to manually complete pending transfers
   - For CCTP: Follow the manual process described in the CCTP section
   - For Skip: Contact Skip support through their Discord
3. **Contact appropriate support**
   - **Check the [dYdX Status Page](https://status.dydx.exchange)** for any known issues
   - **Join the [dYdX Discord](https://discord.gg/dydx)** for community support
   - **Open a support ticket** via the dYdX interface
   - **Skip issues:** [Skip Discord](https://discord.gg/skip-protocol)
   - **Noble issues:** [Noble Discord](https://discord.gg/noble)

Remember to include transaction details, wallet addresses, and a clear description of the issue for faster resolution.

## **Best Practices**

1. **Always start with a small test transaction** when using a new deposit or withdrawal method
2. **Keep your wallet connected** to dYdX frontend for auto-sweeping
3. **Save transaction hashes** for all operations
4. **Double-check all addresses** before confirming transactions
5. **Ensure your destination wallet supports** the asset you're withdrawing
6. **For large transfers, use Skip Go** instead of Skip Go Fast for better reliability
7. **Always move funds from sub account to main account** before initiating withdrawals
8. **Understand third-party dependencies** in your chosen transfer route:
   - _Skip relies on their own solver network and DEX integrations_
   - _IBC transfers depend on the Cosmos relayer infrastructure_
   - _Coinbase deposits rely on Coinbase's infrastructure and Noble's IBC integration_
9. **Monitor relayer and bridge status** during high network congestion periods
10. **Have backup withdrawal methods** in case one bridge or relayer network experiences issues


# File: v4-documentation/old-docs/pages/api_integration-guides/api_trading_with_classic_python_client.md

# API Trading with (Classic) v4 dYdX Python Client

## Pros and Cons of (Classic) V4 dYdX Python Client
1. Pro: Used by many traders already
2. Pro: Easy setup (this document)
3. Pro: Required for V4 dYdX CLI Tool
4. Con: Can only trade cross-margin markets in cross-margin mode.  As of December 3, 2024, the following markets are cross-margin capable or isolated-margin only.

![APITradingClassicPic1](../../artifacts/APITradingClassicPic1.png)

## Requirements (Initial Setup)
1. Recommended OS: Ubuntu 22.04.4 LTS server (ubuntu-22.04.4-live-server-amd64.iso)
2. Install dependencies.

`sudo apt-get install python3-pip`

`pip3 install v4-proto`

`pip3 install python-dateutil`

`pip3 install bip_utils`

`pip3 install bech32`

`pip3 install websocket-client`

`git clone https://github.com/kaloureyes3/v4-clients`

3. Create a APIKEY file.  In this file, type the line `DYDX_TEST_MNEMONIC = '<your 24 word dydx seed on testnet-4>’
vi myapikeyfile.py'`

![APITradingClassicPic2](../../artifacts/APITradingClassicPic2.png)

4. Add testnet parameters to API client:

`vi ./v4-clients/v4-client-py/v4_client_py/clients/constants.py`

![APITradingClassicPic4](../../artifacts/APITradingClassicPic4.png)

![APITradingClassicPic3](../../artifacts/APITradingClassicPic3.png)

`VALIDATOR_GRPC_ENDPOINT = 'test-dydx-grpc.kingnodes.com:443'`

`AERIAL_CONFIG_URL = 'https://test-dydx-grpc.kingnodes.com:443'`

`AERIAL_GRPC_OR_REST_PREFIX = "grpc"`

`INDEXER_REST_ENDPOINT = 'https://dydx-testnet.imperator.co'`

`INDEXER_WS_ENDPOINT = 'wss://indexer.v4testnet.dydx.exchange/v4/ws'`

`CHAIN_ID = "dydx-testnet-4"`

`ENV = 'testnet'`

5. Setup is complete.

## The V4 dYdX CLI Tool
1. Download the tool from https://github.com/chiwalfrm/solutions-public/tree/main/v4dydxcli
2. Refer to this document for instructions: https://docs.google.com/document/d/13aZz9o4g0WyLrteelBYDUOUmzJgOaPouVwRrF0kn-to/edit?usp=sharing


# File: v4-documentation/old-docs/pages/api_integration-guides/how_to_interpret_block_data_for_trades.md

## dYdX v4: How to Interpret the Block Data for Trades

![Interpret1](../../artifacts/interpret_block_data_1.png)

In dYdX Chain trading, quantities and prices are represented in quantums (for quantities) and subticks (for prices), which need conversion for practical understanding.

### Quantums

The smallest increment of position size. Determined from `atomicResolution`.

atomicResolution - Determines the size of a quantum. [For example](https://github.com/dydxprotocol/v4-testnets/blob/aa1c7ac589d6699124942a66c2362acad2e6f50d/dydx-testnet-4/genesis.json#L5776), an `atomicResolution` of -10 for `BTC`, means that 1 quantum is `1e-10` `BTC`.

### Subticks

Human-readable units: `USDC/<currency>` e.g. USDC/BTC

Units in V4 protocol: `quote quantums/base quantums` e.g. (`1e-14 USDC/1e-10 BTC`)

Determined by `quantum_conversion_exponent`, this allows for flexibility in the case that an asset’s prices plummet, since prices are represent in subticks, decreasing `subticks_per_tick` would allow for ticks to denote smaller increments between prices.

E.g. 1 `subtick` = `1e-14 USDC/1e-10 BTC` and if BTC was at 20,000 USDC/BTC, a `tick` being 100 USDC/BTC (`subtick_per_tick` = 10000) may make sense.

If BTC drops to 200 USDC/BTC, a `tick` being 100 USDC/BTC no longer makes sense, and we may want a `tick` to be 1 USDC/BTC, which lets us set `subtick_per_tick` to 100 to get to a `tick` size of 1 USDC/BTC.

### Now back to the interpretation of the above image:

1. First, notice column I is negative. That means this trade is a sell by the taker account. If It was positive, it would be a buy.

Result: Determined if this is a buy or a sell

2. Next, look at column N. The perpetual_id is 7, which maps to AVAX-USD market. You can see all the mappings from this endpoint for the dYdX Chain deployment by dYdX Operations Services Ltd. https://indexer.dydx.trade/v4/perpetualMarkets where the clobPairId is the perpetual_id.

Result: Determined the market

3. Next, we need to get the decimals for this market. First, get the atomicResolution from that endpoint above which we see is -7. Now we can get the size of the trade. From column I and J, take this number -500000000 and multiply by 10^(AtomicResolution) and you get: -500000000 x 10^-7 = 50, so the quantity is 50.

Result: Determined the quantity

4. Next, look at columns, E, F, G, H, I, and J

![Interpret2](../../artifacts/interpret_block_data_2.png)

The price of the trade is either `abs((G+E)/I)*10e(-6 - AtomicResolution)`, or `abs((H+F)/J)*10e(-6 - AtomicResolution)`, either one is the same. Note that the ‘-6’ is because the AtomicResolution of USDC is -6.

`abs((1479130125 + 369875)/-500000000)*10e(-6 + 7) = 29.59`

`abs((-1479337255 - 162745)/500000000)*10e(-6 +7) = 29.59`

Result: Determined the price

### Conclusion

In conclusion, we have determined that this trade is SELL 50 AVAX-USD at price $29.59


# File: v4-documentation/old-docs/pages/api_integration-guides/how_to_isolated.md

# How to integrate APIs with FE isolated positions

## Overview
This document covers how to use the API to query data on / trade with isolated positions that are managed with the dYdX V4 front end.

## Isolated positions on dYdX V4 front end
Isolated positions on the dYdX V4 front end are perpetual positions held in subaccounts with a subaccount number greater than 127, up to the limit of 128,000. Each isolated position is held in a separate subaccount.

### Mapping of isolated positions to subaccounts
The dYdX V4 front end implementation separates subaccounts (0 - 128,000) into 2 separate types:

**Parent subaccounts**

Subaccounts 0 to 127 are parent subaccounts. Parent subaccounts can have multiple positions opened and all positions are cross-margined.

**Child subaccounts**

Subaccounts 128 to 128,000 are child subaccounts. Child subaccounts will only ever have up to 1 position open. Each open isolated position on the front end is held by a separate child subaccount.
Once an isolated position is closed in the front end, the subaccount associated with isolated position can be re-used for the next isolated position.
Child subaccounts are mapped to parent subaccounts using the formula:
```
parent_subaccount_number = child_subaccount_number % 128
```

> Note that currently only parent subaccount 0 is exposed via the front end and so isolated positions will be held in subaccounts number 128, 256, ...

> Note that the above "types" of subaccounts are not enforced at a protocol level, and only on the front end. Any subaccount can hold any number of positions in cross-marginable markets which all will cross-margined at the protocol level.

### Getting data for parent subaccount
API endpoints exist to get data for a parent subaccount and all it's child subaccounts on the Indexer.

> Currently all data for an account viewable on the front end can be fetched by using the parent subaccount APIs to fetch data for parent subaccount number 0.

See the <a href="/developers/indexer/indexer_api">Indexer API</a> page for more details of the parent subaccount APIs.


# File: v4-documentation/old-docs/pages/api_integration-guides/how_to_permissioned_keys.md

# Permissioned Keys

## Overview

Permissioned Keys are a dYdX specific extension to the Cosmos authentication system that allows an account to add custom logic for verifying and confirming transactions placed on that account. For example, an account could enable other accounts to sign and place transactions on their behalf, limit those transactions to certain message types or clob pairs etc, all in a composable way.

To enable this there are currently six types of "authenticator" that can used, four that enable specific authentication methods and two that allow for composability:

**Sub-Authenticator Types**

- **SignatureVerification** – Enables authentication via a specific key
- **MessageFilter** – Restricts authentication to certain message types
- **SubaccountFilter** – Restricts authentication to certain subaccount constraints
- **ClobPairIdFilter** – Restricts transactions to specific CLOB pair IDs

**Composable Authenticators**

- **AnyOf** - Succeeds if *any* of its sub-authenticators succeeds
- **AllOf** - Succeeds only if *all* sub-authenticators succeed

## Capabilities

### Available Features ✅

1. **Account Access Control**

   - Limit withdrawals/transfers entirely
   - Multiple trading keys under same account
   - Trading key separation from withdrawal keys

2. **Asset-Specific Trading**

   - Whitelist specific trading pairs
   - E.g., Allow BTC/USD and ETH/USD, restrict others

3. **Subaccount Management**
   - Control trading permissions per subaccount
   - E.g., Enable trading on subaccount 0, restrict subaccount 1

### Current Limitations ❌

1. **Position Management**

   - Cannot set maximum position sizes
   - No order size restrictions
   - No custom leverage limits

---

## **Example: Setup permission keys using Golang**

### **Adding an AllOf Authenticator With SignatureVerification + MessageFilter**

The following example demonstrates how “Bob” can add an “AllOf” authenticator that grants “Alice” permission to submit only “MsgPlaceOrder” transactions on Bob’s account.

**1. Building Sub-Authenticators**

To allow Alice’s key to sign transactions, and to restrict transactions to the “MsgPlaceOrder” message type, construct two sub-authenticators:

- SignatureVerification: Uses Alice’s public key
- MessageFilter: Only allows `"/dydxprotocol.clob.MsgPlaceOrder"` messages.

In Go (pseudocode):

```go
subAuths := []aptypes.SubAuthenticatorInitData{
    {
        Type:   "SignatureVerification",
        Config: AlicePrivateKey.PubKey().Bytes(),
    },
    {
        Type:   "MessageFilter",
        Config: []byte("/dydxprotocol.clob.MsgPlaceOrder"),
    },
}

// Marshal sub-authenticators into JSON data for the AllOf authenticator.
allOfData, err := json.Marshal(subAuths)
require.NoError(t, err)
```

**2. Creating the AllOf Authenticator**

We want to associate this new authenticator with Bob’s account. Therefore, Bob must be the “Sender” of a “MsgAddAuthenticator.”

The “AuthenticatorType” is "AllOf," and the “Data” is the marshaled sub-authenticators from step 1.

```go
addAllOfMsg := &aptypes.MsgAddAuthenticator{
    Sender:            constants.BobAccAddress.String(),
    AuthenticatorType: "AllOf",
    Data:              allOfData,
}
```

This tells the chain to store a new “AllOf” authenticator on Bob’s account. The chain will return an authenticator ID (for example, 0).

**3. Submitting the Add Authenticator Transaction**

Because Bob owns the account, Bob’s signature is required to add this authenticator:

```go
tx, err := testtx.GenTx(
    ctx,
    txConfig,
    []sdk.Msg{addAllOfMsg},
    someFeeCoins,         // transaction fee
    someGasAmount,        // gas
    chainID,
    []uint64{bobAccNum},  // Bob’s account number
    []uint64{bobSeqNum},  // Bob’s sequence
    []cryptotypes.PrivKey{bobPrivKey},  // signature by Bob
    []cryptotypes.PrivKey{bobPrivKey},  // fee payer is also Bob
    nil,                  // no additional authenticators referenced here
)
```

Broadcast the transaction to the network. If successful, Bob’s account now has an AllOf authenticator. The chain references it by an ID (e.g. 0).

---

### **Submitting an Order With the New Authenticator**

After adding this AllOf authenticator, Bob implicitly allows transactions on his account, but only if they match both sub-authenticators (Alice must sign, and the message must be “MsgPlaceOrder”).

**4. Creating a PlaceOrder Message**

Construct a “MsgPlaceOrder.” In Go:

```go
placeOrderMsg := clobtypes.NewMsgPlaceOrder(
// Place order using Bob's account details
    ),
)
```

**5. Building and Signing the Transaction**

Even though the account belongs to Bob, the AllOf authenticator requires Alice’s signature. Hence, we sign the PlaceOrder transaction with Alice’s private key:

```go
orderTx, err := testtx.GenTx(
    ctx,
    txConfig,
    []sdk.Msg{placeOrderMsg},
    someFeeCoins,
    someGasAmount,
    chainID,
    []uint64{bobAccNum},              // Bob's account number
    []uint64{bobSeqNum},              // Bob's sequence
    []cryptotypes.PrivKey{alicePrivKey}, // sign with Alice’s key
    []cryptotypes.PrivKey{alicePrivKey}, // Alice is also paying fees
    []uint64{0},                      // reference the AllOf authenticator by ID = 0
)
```

Broadcast this transaction. During verification:

- SignatureVerification sub-authenticator checks that Alice signed the transaction.
- MessageFilter sub-authenticator checks that the message is `/dydxprotocol.clob.MsgPlaceOrder`
- AllOf requires that both sub-authenticators pass, which they do if Alice is indeed signing and the message is of the correct type.

Once successful, Bob’s account effectively “permits” the order to be placed, but only under the conditions enforced by the AllOf authenticator.

## **Example: Setup permission keys using Typescript**

### **Adding an AllOf Authenticator With multiple filters**

**1. Setup the client**

Make sure that you are using at least @dydxprotocol/v4-client-js `v1.16.0`

```typescript
import { CompositeClient, AuthenticatorType } from '@dydxprotocol/v4-client-js';

const client = await CompositeClient.connect(Network.mainnet());
```

**2. Define permissions**

Each authenticator can have one or multiple restrictions that are combined with `ALL_OF` or `ANY_OF`:

```typescript
import { toBase64 } from '@cosmjs/encoding';
import { TextEncoder } from 'util';

const subAuthenticators = [
  // Who: Allow this specific public key to sign transactions
  {
    type: AuthenticatorType.SIGNATURE_VERIFICATION,
    config: authedPubKey,
  },
  // What: Only allow placing e.g. orders
  {
    type: AuthenticatorType.MESSAGE_FILTER,
    config: toBase64(new TextEncoder().encode('/dydxprotocol.clob.MsgPlaceOrder')),
  },
  // Where: Only on subaccount 0
  {
    type: AuthenticatorType.SUBACCOUNT_FILTER,
    config: toBase64(new TextEncoder().encode('0')),
  },
  // Which market: Only ETH-USD (clobpair 1)
  {
    type: AuthenticatorType.CLOB_PAIR_ID_FILTER,
    config: toBase64(new TextEncoder().encode('1')),
  },
];
```

**3. Creating an All-Of Authenticator**

Encode the overall authenticator and submit the transaction.

```typescript
async function addAuthenticator(
  client: CompositeClient,
  subaccount: SubaccountInfo,
  authedPubKey: string
): Promise<void> {
  const jsonString = JSON.stringify(subAuthenticators);
  const encodedData = new TextEncoder().encode(jsonString);
  const auth = await client.addAuthenticator(subaccount, AuthenticatorType.ALL_OF, encodedData);
}
```

### **Submitting an Order With the New Authenticator**

**4. Place order with authenticator**

```typescript
// Wallet1 wants to allow Wallet2 to place ETH-USD orders on its subaccount 0
const subaccount1 = new SubaccountInfo(wallet1, 0);
const subaccount2 = new SubaccountInfo(wallet2, 0);

// Wallet1 Adds an authenticator to allow wallet2
await addAuthenticator(client, subaccount1, wallet2.pubKey!.value);
const authenticators = await client.getAuthenticators(wallet1.address!);

//  Get the authenticator ID, the last element in authenticators array is the most recently created
const lastElement = authenticators.accountAuthenticators.length - 1;
const authenticatorID = authenticators.accountAuthenticators[lastElement].id;

//  Now Wallet2 can place orders on Wallet1's subaccount
await placeOrder(client, subaccount2, subaccount1, authenticatorID);
```

**5. Remove the authenticator again**

```typescript
// Remove the authenticator
await removeAuthenticator(client, subaccount1, authenticatorID);

// Placing an order using subaccount2 will now fail
await placeOrder(client, subaccount2, subaccount1, authenticatorID);
```

### **End-to-end example**

Our Typescript client has helper functions for:

- Adding an authenticator ([link](https://github.com/dydxprotocol/v4-clients/blob/e0d1c76564dabb85715e34197799edc0b5d0ecc5/v4-client-js/src/clients/composite-client.ts#L1239))
- Removing an authenticator ([link](https://github.com/dydxprotocol/v4-clients/blob/e0d1c76564dabb85715e34197799edc0b5d0ecc5/v4-client-js/src/clients/composite-client.ts#L1247C9-L1247C28))
- Viewing all authenticators for an given address ([link](https://github.com/dydxprotocol/v4-clients/blob/e0d1c76564dabb85715e34197799edc0b5d0ecc5/v4-client-js/src/clients/composite-client.ts#L1254C9-L1254C26))

This guide demonstrates how to set up permissioned keys, allowing one wallet to execute trades on behalf of another wallet's subaccount with specific restrictions.

For the end to end example, adding an authenticator and placing a short term order with the authenticated account, see here:
[Link to e2e example](https://github.com/dydxprotocol/v4-clients/blob/adam/add-authentications-functions/v4-client-js/examples/permissioned_keys_example.ts)


# File: v4-documentation/old-docs/pages/api_integration-guides/how_to_uncross_orderbook.md

# How to uncross the orderbook

## Observation
First, let’s take a look at an actual example of a crossed orderbook for BTC-USD on v4 Testnet.

At the moment just before it crossed, the below is what is shown. There are no crossed prices here:
![Observation 1](../../artifacts/how_to_uncross_orderbook_observation_1.png)

At the next update, the below is what is shown and there was a crossed price:
![Observation 2](../../artifacts/how_to_uncross_orderbook_observation_2.png)

As shown above, the best bid was 26854 and the best ask was 26826, which is lower than the best bid.

## Explanation

v4 doesn't guarantee that order book prices don't cross because there is no centralized order book. For that reason, the software does not include a global offset. The “correct” order book at any given time is whatever the current block proposer has in its mempool, which is not what the indexer or the front end can directly see. The block proposer changes every block, so there is a new canonical mempool, and therefore, a new canonical order book every block. Due to the particulars of message propagation, that means there will be slight differences in the canonical order book every block. If the trader doesn’t need the order book prices uncrossed, simply listen to the updates given by the websocket and they should uncross eventually.

## How to uncross
If trader needs the order book uncrossed, then one way is to use the order of messages as a logical timestamp. That is, when a message is received, update a global locally-held offset. Each websocket update has a message-id which is a logical offset to use.

```python
if remove_crossed_prices == True:
                highestbidprice = 0
                lowestaskprice = 0
                while len(bidarray) > 0 and len(askarray) > 0 and ( highestbidprice == 0 or highestbidprice >= lowestaskprice ):
                        highestbid = bidarray[0]
                        lowestask = askarray[0]
                        highestbidprice = float(highestbid[0])
                        lowestaskprice = float(lowestask[0])
                        highestbidsize = float(highestbid[1])
                        lowestasksize = float(lowestask[1])
                        highestbidoffset = int(highestbid[2])
                        lowestaskoffset = int(lowestask[2])
                        if highestbidprice >= lowestaskprice:
                                if highestbidoffset < lowestaskoffset:
                                        bidarray.pop(0)
                                elif highestbidoffset > lowestaskoffset:
                                        askarray.pop(0)
                                else:
                                        fp = open(ramdiskpath+'/'+market+'/TRAPsameoffset', "a")
                                        fp.write(str(highestbidprice)+','+str(highestbidsize)+','+str(lowestaskprice)+','+str(lowestasksize)+','+str(highestbidoffset)+','+datetime.now().strftime("%Y-%m-%d %H:%M:%S")+'\n')
                                        fp.close()
                                        if highestbidsize > lowestasksize:
                                                askarray.pop(0)
                                                bidarray[0] = [ str(highestbidprice), str(highestbidsize - lowestasksize), str(highestbidoffset), highestbid[3], highestbid[4] ]
                                        elif highestbidsize < lowestasksize:
                                                askarray[0] = [ str(lowestaskprice), str(lowestasksize - highestbidsize), str(lowestaskoffset), lowestask[3], lowestask[4] ]
                                                bidarray.pop(0)
                                        else:
                                                askarray.pop(0)
                                                bidarray.pop(0)

```

v4 software stores the message-id for each bid/ask as the third element of a list, for example: `['26854.0', '0.556', '8468']` would be the best bid for the example above (`bidarray[0]`).  From left to right, the elements are price, size, and message-id.  And `['26826.0', '0.0027', '8489']` would be the corresponding best ask (`askarray[0]`).  (see box a in the graphic below)

Next, set the following variables in the first iteration of the while loop (see box b in the graphic below).
```
    highestbid =  ['26854.0', '0.556', '8468']
    lowestask = ['26826.0', '0.0027', '8489']
    highestbidprice = 26854
    lowestaskprice = 26826
    highestbidsize = 0.556
    lowestasksize = 0.0027
    highestbidoffset = 8468
    lowestaskoffset = 8489
```

Then, compare the two sides, using the offsets to determine whether to discard the bid or ask (see box c in the graphic below), or in the case where both bid/ask have the same offset, it compares the volume on each side (see box d in the graphic below).
![Sample Code](../../artifacts/how_to_uncross_orderbook_sample_code.png)


# File: v4-documentation/old-docs/pages/api_integration-guides/setting_up_raspberry_pi_for_api_trading.md

# Setting Up Raspberry Pi for API Trading

## Chapter 1: Initial Setup

1. Note that one of the micro-USB ports is for power only.  Do not plug your keyboard/mouse/hub in this port.  It won’t damage it but it won’t work.
![RaspberryPi1](../../artifacts/RaspberryPi1.png)

2. After installation, enable SSH.  Instructions here: https://www.onlogic.com/company/io-hub/how-to-ssh-into-raspberry-pi/
3. Use Terminal for all commands below.
4. Get the IP address with this command:
`ip addr show`
5. Install the latest updates with:
`sudo apt-get update`
`sudo apt-get upgrade`
6. Add more swap memory: Instructions here, except use “CONF_SWAPSIZE=4096” (your microSD memory card should be 16GB or more)
https://web.archive.org/web/20240228194730/https://nebl.io/neblio-university/enabling-increasing-raspberry-pi-swap/
7. Reboot with:
`sudo shutdown -r 0`
8. For the next part, you will need to know how to use the ‘vi’ text editor.  Take the simple tutorial here:
https://www.redhat.com/sysadmin/introduction-vi-editor

## Chapter 2: Install Pre-requisites

1. Install dependencies.

`sudo apt-get install python3-pip`

`sudo apt-get install git`

`pip3 install v4-proto`

`pip3 install python-dateutil`

`pip3 install grpcio`

`pip3 install bip_utils`

`pip3 install bech32`

`pip3 install websockets`

`pip3 install websocket-client`

`git clone https://github.com/kaloureyes3/v4-clients`

`git clone https://github.com/chiwalfrm/dydxexamples`

`ln -s dydxexamples/dydxcli/v4dydxcli.py .
^(note that’s a lowercase L at the beginning, not an uppercase-eye and there is a period at the end of the command)

`chmod 755 dydxexamples/dydxcli/v4closeallpositions.sh`

2. Create a APIKEY file.  In this file, type the line `DYDX_TEST_MNEMONIC = '<your 24 word dydx seed on testnet-4>’`

`vi myapikeyfile.py`

![RaspberryPi2](../../artifacts/RaspberryPi2.png)

3. Add testnet parameters to API client:

`vi ./v4-clients/v4-client-py/v4_client_py/clients/constants.py`

![RaspberryPi3](../../artifacts/RaspberryPi3.png)

![RaspberryPi4](../../artifacts/RaspberryPi4.png)

`VALIDATOR_GRPC_ENDPOINT = 'test-dydx-grpc.kingnodes.com:443'`

`AERIAL_CONFIG_URL = 'https://test-dydx-grpc.kingnodes.com:443'`

`AERIAL_GRPC_OR_REST_PREFIX = "grpc"`

`INDEXER_REST_ENDPOINT = 'https://dydx-testnet.imperator.co'`

`INDEXER_WS_ENDPOINT = 'wss://indexer.v4testnet.dydx.exchange/v4/ws'`

`CHAIN_ID = "dydx-testnet-4"`

`ENV = 'testnet'`

4. Test it out by checking your balance:

`python3 v4dydxcli.py myapikeyfile.py balance`

![RaspberryPi5](../../artifacts/RaspberryPi5.png)

5. Note that you can get a list of commands by typing the following command.  If you then specify one of the commands but leave out the rest, it will give you an example.

`python3 v4dydxcli.py myapikeyfile.py help`

6. Now you are ready for the workshop.

## Chapter 3: Periodic Updates

Periodic updates are recommended in order to get the latest changes from developers.

1. Install the latest OS updates with:

`sudo apt-get update`

`sudo apt-get upgrade`

2. Update the dydx packages:

`pip3 install v4-proto -U`

`rm -rf v4-clients dydxexamples`

`git clone https://github.com/kaloureyes3/v4-clients`

`git clone https://github.com/chiwalfrm/dydxexamples`

3. Note that you have to repeat the Chapter 2 step ‘Add testnet parameters to API client’ above.

## Chapter 4: Trade on Mainnet (Deployment by dYdX Operations Services Ltd.)

1. Repeat the Chapter 2 step ‘Add testnet parameters to API client’ except with the following changes:

`VALIDATOR_GRPC_ENDPOINT = 'dydx-grpc.publicnode.com:443'`

`AERIAL_CONFIG_URL = 'https://dydx-grpc.publicnode.com:443'`

`AERIAL_GRPC_OR_REST_PREFIX = "grpc"`

`INDEXER_REST_ENDPOINT = "https://indexer.dydx.trade/"`

`INDEXER_WS_ENDPOINT = "wss://indexer.dydx.trade/v4/ws"`

`CHAIN_ID = "dydx-mainnet-1"`

`ENV = 'mainnet'`



# File: v4-documentation/old-docs/pages/concepts-trading/margin.md

# Margining

As part of default settings on the dYdX Chain open source software, each market has two risk parameters, Initial Margin Fraction (IMF) and Maintenance Margin Fraction (MMF):

  - **Initial Margin Fraction**: A percentage (fixed until [certain level](#open-interest-based-imf) of Open Interest) that determines the minimum collateral required to open or increase positions.

  - **Maintenance Margin Fraction**: A percentage (fixed) that determines the minimum collateral required to maintain positions and avoid liquidation.

## Open-Interest-Based IMF

The IMF of a perpetual market scales linearly according to the current `open_notional` in the market, starting at `open_notional_lower_cap` to `open_notional_upper_cap` (USDC denominated):

```
open_notional = open_interest * oracle_price

scaling_factor = (open_notional - open_notional_lower_cap) / (open_notional_upper_cap - open_notional_lower_cap)

IMF_increase = scaling_factor * (1 - base_IMF)

effective_IMF = Min(base_IMF + Max(IMF_increase, 0), 100%)
```

I.e. the effective IMF is the base IMF while `open_notinal < lower_cap`, and increases linearly until `open_notional = upper_cap`, at which point the IMF stays at 100% (requiring 1:1 collateral for trading). Importantly, the MMF (Maintenance Margin Fraction) does not change.

The [Open Notional Lower Cap](https://github.com/dydxprotocol/v4-chain/blob/b829b28b0d71e754ac553fbeec29ce5309bd79f7/proto/dydxprotocol/perpetuals/perpetual.proto#L133) and [Open Notional Upper Cap](https://github.com/dydxprotocol/v4-chain/blob/b829b28b0d71e754ac553fbeec29ce5309bd79f7/proto/dydxprotocol/perpetuals/perpetual.proto#L138) are parameters defined as part of the market's [Liquidity Tier](https://github.com/dydxprotocol/v4-chain/blob/b829b28b0d71e754ac553fbeec29ce5309bd79f7/proto/dydxprotocol/perpetuals/perpetual.proto#L100).

## Detailed Margin Calculation

The margin requirement for a single position is calculated as follows:

    Initial Margin Requirement = abs(S × P × I) Maintenance Margin Requirement = abs(S × P × M)

Where:

- S is the size of the position (positive if long, negative if short)
- P is the oracle price for the market
- I is the initial margin fraction for the market
- M is the maintenance margin fraction for the market

The margin requirement for the account as a whole is the sum of the margin requirement over each market i in which the account holds a position:

    Total Initial Margin Requirement = Σ abs(Si × Pi × Ii) Total Maintenance Margin Requirement = Σ abs(Si × Pi × Mi)

The total margin requirement is compared against the total value of the account, which incorporates the quote asset (USDC) balance of the account as well as the value of the positions held by the account:

    Total Account Value = Q + Σ (Si × Pi)

The Total Account Value is also referred to as equity.

Where:

  - Q is the account's USDC balance (note that Q may be negative). In the API, this is called quoteBalance. Every time a transfer, deposit or withdrawal occurs for an account, the balance changes. Also, when a position is modified for an account, the quoteBalance changes. Also funding payments and liquidations will change an account's quoteBalance.
  - S and P are as defined above (note that S may be negative)

An account cannot open new positions or increase the size of existing positions if it would lead the total account value of the account to drop below the total initial margin requirement. If the total account value ever falls below the total maintenance margin requirement, the account may be liquidated.

Free collateral is calculated as:

    Free collateral = Total Account Value - Total Initial Margin Requirement

Equity and free collateral can be tracked over time using the latest oracle price.


# File: v4-documentation/old-docs/pages/concepts-trading/rewards_fees_and_parameters.md

## Rewards, Fees and Parameters

### Trading Rewards
_Trading rewards are subject to adjustments by the applicable Governance Community._

The software will allow the network to fund and utilize trading rewards. 

In addition to incentivizing trading on the protocol, the general goals of trading rewards include: 

1. Self-trading should not be profitable 
2. Any distributed rewards should be proportional to fees paid to the protocol
3. Trading rewards should be deterministic
4. Trading rewards should be settled and distributed every block 
5. Trading rewards should limit the protocol overspending on trading activity

#### How do trading rewards work from a user perspective? 

Traders are rewarded after each successful trade made on the protocol.

Immediately after each fill, a user is sent a certain amount of trading rewards directly to their dYdX Chain address, based on the formulas described below. Prior to each trade, the UI also shows the maximum amount of rewards a trade of that size could receive.

Users earn trading rewards up to, but not exceeding, 90% of a fill’s net-trading-fees, paid in the governance token of the network.

#### How do trading rewards affect potential inflation of the governance token? 

Trading rewards distributed by the protocol, each block, are capped at the dollar equivalent of the total net trading fees generated by the protocol that block. Thus, trading rewards distributed can fluctuate on a block by block basis. 

This can result in a large amount of “savings” by the protocol (via reduced inflation) by not overspending to incentivize trading activity.

#### What formula for trading rewards will exist within the open source software? 

The software reflects a Rewards Treasury of tokens that are available to be distributed to traders. Call the size of this Rewards Treasury T. Each block, new tokens are transferred into this T from the vesting contract and rewards are then distributed. Each block, T can grow or shrink based on protocol activity. 

Let A represent the amount of rewards that are distributed from this T to traders in a given block.

We define a trader X’s “rewards score” in a given block as:

![FRP1](../../artifacts/FRP1.png)

Let S be the sum of all the rewards scores across all traders for a given block. S is given by:

![FRP2](../../artifacts/FRP2.png)

Every block, the amount A of the native token that is distributed to traders is defined as:

![FRP3](../../artifacts/FRP3.png)

Where C is a constant configurable by the applicable Governance Community. The open source software is configured for the constant to be initially set at 0. 

The amount remaining (T - A) is retained in the Rewards Treasury and new tokens are emitted into the Rewards Treasury the following block.

A is calculated and distributed to all the takers who traded in the block and T - A is rolled over and retained in the Rewards Treasury for the next block.

The rewards distributed, A, are allocated proportional to each trader’s score. 

Once the Vesting Contract is funded, trading rewards will continue to run and settle automatically, every block.   

See below for a visual that summarizes trading rewards architecture.

![FRP4](../../artifacts/FRP4.png)

### Fee Schedule
_The fee schedule is subject to adjustments by the applicable Governance Community_

The basic structure for fees have been developed to reflect the following characteristics:

1. Fees differ based on side (maker/taker)
2. Users are eligible for lower fees based on their 30 day trading volume across sub accounts and markets
3. Fees are uniform across all markets

| Tier  | 30d Trailing Volume                     | Taker (bps) | Maker (bps) |
|-------|-----------------------------------------|-----------------|----------------------------------------|
| 1     | < $1M                                  | 5.0             | 1.0                                    |
| 2    | ≥ $1M                                  | 4.5             | 1.0                                    |
| 3   | ≥ $5M                                  | 4.0             | 0.5                                    |
| 4    | ≥ $25M                                 | 3.5             | —                                      |
| 5     | ≥ $125M                                | 3.0             | —                                      |
| 6    | ≥ $125M and ≥0.5% exchange mkt. share  | 2.5             | -0.5                                   |
| 7   | ≥ $125M and ≥1% maker mkt. share       | 2.5             | -0.7                                   |
| 8  | ≥ $125M and ≥2% maker mkt. share       | 2.5             | -0.9                                   |
| 9    | ≥ $125M and ≥4% maker mkt. share       | 2.5             | -1.1                                   |

**Parameters**

_Below is a summary of various notable parameters and what they mean for any chain utilizing the open source software. Parameters will be subject to adjustments by the applicable Governance Community and can be set to different values at Genesis by any deployer._

**Bank Parameters**

This parameter establishes whether transfers for any tokens are enabled at Genesis. Transfers will be enabled. 

**State Parameters**

The open source software will not pre-populate any bank-state on the network. Validators who participate in Genesis have the ability to determine the network’s initialized state. 

**Slashing Parameters**

These parameters establish punishments for detrimental behavior by validators.

|                 | Signed Blocks Window | Min Signed Per Window | Downtime Jail Duration | Slash Fraction Doublesign | Slash Fraction Downtime |
| --------------- | -------------------- | --------------------- | ---------------------- | ------------------------- | ----------------------- |
| Slashing Params | 8192 (-3 hrs)        | 20%                   | 7200s                  | 0%                        | 0%                      |

_SignedBlocksWindow_: Together with MinSignedPerWindow, specifies the number of blocks a validator must sign within a sliding window. Failure to maintain MinSignedPerWindow leads to validator being jailed (removed from active validator set). 

_SlashFractionDownTime_: Defines the slashing-penalty for downtime 

_DownTimeJailDuration_: How long before the validator can unjail themselves after being jailed for downtime.

Double-signing by a validator is considered a severe violation as it can cause instability and unpredictability in the network. When a validator double-signs, they are slashed for SlashFractionDoubleSign, jailed (removed from validator set) and tombstoned (cannot rejoin validator set). 

**Distribution Parameters**

These parameters handle the  distribution of gas and trading fees generated by the network to validators. 

|                     | Community Tax | WithdrawAddrEnable |
| ------------------- | ------------- | ------------------ |
| Distribution Params | 0%            | True               |

_CommunityTax_: Fraction of fees that goes to the community treasury. The software will initially reflect a 0% community tax.

_WithdrawAddrEnabled_: Whether a delegator can set a different withdrawal address (other than their delegator address) for their rewards.

**Staking Parameters**

These parameters define how staking works on the protocol and norms around staking.

*MaxValidators and UnbondingTime are particularly subject to change based on public testnet data and feedback. 

|                 | BondDenom                         | MaxValidators | MinCommissionRate | Unbonding Time |
| --------------- | --------------------------------- | ------------- | ----------------- | -------------- |
| Slashing Params | Decided at Genesis, by validators | 60            | 5%                | 30 days        |

_MaxValidators_: Every block, the top MaxValidators validators by stake weight are included in the active validator set.

_UnbondingTime_: Specifies the duration of the unbonding process, during which tokens are in a locked state and cannot be transferred or delegated (the tokens are still “at stake”).

_MinCommissionRate_: The chain-wide minimum commission rate that a validator can charge their delegators. The default commission rate will be 100%.

**Governance Parameters**

These parameters define how governance proposals can be submitted and executed. For more information on the governance module and its associated parameters, head to the official [Cosmos SDK docs](https://docs.cosmos.network/v0.47/modules/gov#parameters).

|            | Min Deposit             | MinInitialDepositRatio | Max Deposit Period | Voting Period | Quorum | Threshold | Veto  |
| ---------- | ----------------------- | ---------------------- | ------------------ | ------------- | ------ | --------- | ----- |
| Gov Params | 10,000 governance token | 20%                    | 1 Days             | 4 Days        | 33.4%  | 50%       | 33.4% |




# File: v4-documentation/old-docs/pages/users-governance/functionalities.md

# Governance Functionalities

Below is a current list of all module parameters that `x/gov` has the ability to update directly. Further documentation will be released which outlines overviews of each custom module, how modules interact with one another, and technical guides regarding how to properly submit governance proposals. 

## Trading Stats & Fees

### Stats Module

The Stats Module tracks user maker and taker volumes over a period of time (aka look-back window). This is currently set to 30 days. The maker and taker volume info is used to place users in corresponding fee-tiers. 

Governance has the ability to update the params of the Stats Module, which defines the look-back window (measured in seconds). [Proto](https://github.com/dydxprotocol/v4-chain/blob/4eb219b1b726df9ba17c9939e8bb9296f5e98bb3/proto/dydxprotocol/stats/params.proto#L10-L14)

### FeeTiers Module

Governance has the ability to update fee tiers ([proto](https://github.com/dydxprotocol/v4-chain/blob/4eb219b1b726df9ba17c9939e8bb9296f5e98bb3/proto/dydxprotocol/feetiers/params.proto#L6-L10)). To read more about fee tiers head to [V4 Deep Dive: Rewards and Parameters](https://dydx.exchange/blog/v4-rewards-and-parameters). 

## Trading Core

### Insurance Fund

Governance has the ability to send funds from the Protocol’s Insurance Fund. Funds can be sent to individual accounts, or other modules. 

Note: any account has the ability to send assets to the Insurance Fund. 

### Liquidations Config

Governance has the ability to adjust how liquidations are processed. [Proto](https://github.com/dydxprotocol/v4-chain/blob/4eb219b1b726df9ba17c9939e8bb9296f5e98bb3/proto/dydxprotocol/clob/liquidations_config.proto#L8-L34)

- Max Insurance Fund quantums for deleveraging: The maximum number of quote quantums (exclusive) that the insurance fund can have for deleverages to be enabled.
- The maximum liquidation fee, in parts-per-million. 100% of this fee goes to the Insurance Fund
- The maximum amount of how much a single position can be liquidated within one block.
- The maximum amount of how much a single subaccount can be liquidated within a single block
- Fillable price config: configuration regarding how the fillable-price spread from the oracle price increases based on the adjusted bankruptcy rating of the subaccount.

### Funding Rate

Governance has the ability to adjust Funding Rate parameters: 

- Funding rate clamp factor, premium vote clamp factor, and min number of votes per premium sample. [Proto](https://github.com/dydxprotocol/v4-chain/blob/4eb219b1b726df9ba17c9939e8bb9296f5e98bb3/proto/dydxprotocol/perpetuals/params.proto#L6-L19)
- Epoch information, which defines the funding interval and premium sampling interval. [Proto](https://github.com/dydxprotocol/v4-chain/blob/4eb219b1b726df9ba17c9939e8bb9296f5e98bb3/proto/dydxprotocol/epochs/epoch_info.proto#L6-L43)
- Liquidity Tier, which defines the impact notional value. [Proto](https://github.com/dydxprotocol/v4-chain/blob/4eb219b1b726df9ba17c9939e8bb9296f5e98bb3/proto/dydxprotocol/perpetuals/perpetual.proto#L100-L139)

## Trading Rewards

### Vest Module

The Vest Module is responsible for determining the rate of tokens that vest from Vester Accounts to other accounts such as a Community Treasury Account and a Rewards Treasury Account. The rate of token transfers is linear with respect to time. Thus, block timestamps are used to vest tokens.

Governance has the ability to create, update, or delete a `VestEntry` ([proto](https://github.com/dydxprotocol/v4-chain/blob/4eb219b1b726df9ba17c9939e8bb9296f5e98bb3/proto/dydxprotocol/vest/vest_entry.proto#L9-L30)), which defines:   

- The start and end time of vesting
- The token that is vested
- The account to vest tokens to
- The account to vest tokens from

### Rewards Module

The Rewards Module distributes trading rewards to traders (previously written about [V4 Deep Dive: Rewards and Parameters](https://dydx.exchange/blog/v4-rewards-and-parameters)). Governance has the ability to adjust the following ([proto](https://github.com/dydxprotocol/v4-chain/blob/4eb219b1b726df9ba17c9939e8bb9296f5e98bb3/proto/dydxprotocol/rewards/params.proto#L6-L26)): 

- Which account Trading Rewards are funded from
- The token Trading Rewards are funded in
- The market which tracks the oracle price of the token that Trading Rewards are funded in
- `C` which is a protocol constant further explained in the post linked above

## Markets

### Oracles

Governance has the ability to adjust the list of oracles used for each market. [Proto](https://github.com/dydxprotocol/v4-chain/blob/4eb219b1b726df9ba17c9939e8bb9296f5e98bb3/proto/dydxprotocol/prices/market_param.proto#L31-L33) 

Note that this functionality does not include creating / removing an exchange-source supported by the protocol as a whole, which will require a binary upgrade. 

### Liquidity Tiers

Liquidity Tiers group markets of similar risk into standardized risk parameters. Liquidity tiers specify the margin requirements needed for each market and should be determined based on the depth of the relative market’s spot book as well as the token’s market capitalization. 

Current Liquidity Tiers include: 

| ID | Name | initial margin fraction | maintenance fraction (what fraction MMF is of IMF) | impact notional |  maintenance margin fraction (as is) | impact notional (as is) | Lower Cap (USDC Millions) | Upper Cap (USDC Millions) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | Large-Cap | 0.02 | 0.6 | 500 USDC / IM | 0.012 | 10_000 USDC | None | None |
| 1 | Small-Cap | 0.1 | 0.5 | 500 USDC / IM | 0.05 | 5_000 USDC | 20 | 50 |
| 2 | Long-Tail | 0.2 | 0.5 | 500 USDC / IM | 0.1 | 2_500 USDC | 5 | 10 |
| 3 | Safety | 1 | 0.2 | 2500 USDC / IM | 0.2 | 2_500 USDC | 2 | 5 |
| 4 | Isolated | 0.05 | 0.6 | 125 USDC / IM | 0.03 | 2_500 USDC | 0.5 | 1 |
| 5 | Mid-Cap | 0.05 | 0.6 | 250 USDC / IM | 0.03 | 5_000 USDC | 40 | 100 |
| 6 | FX | 0.01 | 0.5 | 25 USDC / IM | 0.0005 | 2_500 USDC | 0.5 | 1 |

- Each market has a `Lower Cap` and `Upper Cap` denominated in USDC.
- Each market already has a `Base IMF`.
- At any point in time, for each market:
    - Define
        - `Open Notional = Open Interest * Oracle Price`
        - `Scaling Factor = (Open Notional - Lower Cap) / (Upper Cap - Lower Cap)`
        - `IMF Increase = Scaling Factor * (1 - Base IMF)`
    - Then a market’s `Effective IMF = Min(Base IMF + Max(IMF Increase, 0), 1.0)`
- The effective IMF is the base IMF while the Open Notional < Lower Cap, and increases linearly until Open Notional = Upper Cap, at which point the IMF stays at 1.0 (requiring 1:1 collateral for trading)

Governance has the ability to create and modify Liquidity Tiers as well as update existing markets’ Liquidity Tier placements. ([proto](https://github.com/dydxprotocol/v4-chain/blob/4eb219b1b726df9ba17c9939e8bb9296f5e98bb3/proto/dydxprotocol/perpetuals/perpetual.proto#L100-L139))

### Updating a Live Market

This functionality allows the community to update parameters of a live market, which can be composed of 4 parts

- Updating a liquidity tier
- Perpetual (`x/perpetuals`), governance-updatable through `MsgUpdatePerpetualFeeParams` ([proto definition](https://github.com/dydxprotocol/v4-chain/blob/4eb219b1b726df9ba17c9939e8bb9296f5e98bb3/proto/dydxprotocol/feetiers/tx.proto#L19))
- Market (`x/prices`), governance-updatable through `MsgUpdateMarketParam` ([proto](https://github.com/dydxprotocol/v4-chain/blob/4eb219b1b726df9ba17c9939e8bb9296f5e98bb3/proto/dydxprotocol/prices/market_param.proto#L6-L34))
- Clob pair (`x/clob`), governance-updatable through `MsgUpdateClobPair` ([proto](https://github.com/dydxprotocol/v4-chain/blob/b2c6062b4e588b98a51454f50da9e8e712cfc2d9/proto/dydxprotocol/clob/tx.proto#L102))

### Adding New Markets

The action of a governance proposal is defined by the [list of messages that are executed](https://github.com/dydxprotocol/cosmos-sdk/blob/4fadfe5a4606b6dc76644d377ed34420f3b80801/x/gov/abci.go#L72-L90) when it’s accepted. A proposal to add a new market should include the following messages (in this particular order):

```
MsgCreateOracle (create objects in x/prices)
MsgCreatePerpetual (create object in x/perpetual)
MsgCreatePerpetualClobPair (create object in x/clob)
MsgDelayMessage (schedule a MsgSetClobPairStatus to enable trading in x/clob)
```

## Safety

### Spam Mitigation

To prevent spam on the orderbook and prevent the blockchain state from getting too large, governance has the ability to adjust: 

- How many open orders a subaccount can have based on its equity tier. [Proto](https://github.com/dydxprotocol/v4-chain/blob/4eb219b1b726df9ba17c9939e8bb9296f5e98bb3/proto/dydxprotocol/clob/equity_tier_limit_config.proto#L8-L19)
- Order placement rate limits. [Proto](https://github.com/dydxprotocol/v4-chain/blob/4eb219b1b726df9ba17c9939e8bb9296f5e98bb3/proto/dydxprotocol/clob/block_rate_limit_config.proto#L8-L35)

## Bridge

### Bridge Module

The Bridge Module is responsible for receiving bridged tokens from the Ethereum blockchain.

Governance has the ability to update: 

- Event Parameters: Specifies which events to recognize and which tokens to mint. [Proto](https://github.com/dydxprotocol/v4-chain/blob/4eb219b1b726df9ba17c9939e8bb9296f5e98bb3/proto/dydxprotocol/bridge/params.proto#L9-L20)
- Proposal Parameters: Determines how long a validator should wait until it proposes a bridge event to other validators, and how many or often to propose new bridge events. [Proto](https://github.com/dydxprotocol/v4-chain/blob/4eb219b1b726df9ba17c9939e8bb9296f5e98bb3/proto/dydxprotocol/bridge/params.proto#L22-L45)
- Safety Parameters: Determines if bridging is enabled/disabled and how many blocks mints are delayed after being accepted by consensus. [Proto](https://github.com/dydxprotocol/v4-chain/blob/4eb219b1b726df9ba17c9939e8bb9296f5e98bb3/proto/dydxprotocol/bridge/params.proto#L47-L55)

## Community Assets

### Community Pool & Treasury

There are two addresses intended for managing funds owned by the community: 

1. a Community Pool and 
2. a Community Treasury. 

The Community Pool is the recipient of any Community Tax that is implemented via the Distribution Module. The Community Pool is controllable by governance.  

The Community Treasury is an account controlled by governance and can be funded via any account or module sending tokens to it.  

## CosmosSDK Default Modules

For more information on default modules, head to the [Cosmos SDK official documentation](https://docs.cosmos.network/v0.47/modules). dYdX Chain inherits the same governance properties of any standard CosmosSDK modules that are present on dYdX Chain,


# File: v4-documentation/old-docs/pages/users-governance/proposing_a_new_market.md

# Proposing a new market

**💡 Important: always test proposals on testnets before submitting to any production environment**.

## Proposal Messages

The proposal should consist of 4 messages to be executed **atomically and in order** when the proposal passes onchain.

| Message Index | Message                                                                                                                                                 | Description                                                                                                            | Params Documentation                                                                                                                                    |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0             | [MsgCreateOracleMarket](https://github.com/dydxprotocol/v4-chain/blob/0a01da5ba17b6ca26cef6c0e183c6676a1a4e5dc/proto/dydxprotocol/prices/tx.proto#L28)  | Sets the oracle list and other parameters in `x/prices`, used by the protocol to track an oracle price                 | [MarketParams](https://github.com/dydxprotocol/v4-chain/blob/0a01da5ba17b6ca26cef6c0e183c6676a1a4e5dc/proto/dydxprotocol/prices/market_param.proto#L10) |
| 1             | [MsgCreatePerpetual](https://github.com/dydxprotocol/v4-chain/blob/316473cf115ee901a1371151512a8e97987f66da/proto/dydxprotocol/perpetuals/tx.proto#L31) | Sets the perpetual parameters in `x/perpetuals`, used by the protocol to represent a perpetual market.                 | [Params](https://github.com/dydxprotocol/v4-chain/blob/316473cf115ee901a1371151512a8e97987f66da/proto/dydxprotocol/perpetuals/params.proto#L7)          |
| 2             | [MsgCreateClobPair](https://github.com/dydxprotocol/v4-chain/blob/35b87db422b0ef4138101ba73b0f00d16780ba89/proto/dydxprotocol/clob/tx.proto#L50)        | Sets the orderbook parameters in `x/clob`, used by protocol to set up the market orderbook (in `INITIALIZING` status). | [ClobPair](https://github.com/dydxprotocol/v4-chain/blob/35b87db422b0ef4138101ba73b0f00d16780ba89/proto/dydxprotocol/clob/clob_pair.proto#L25)          |
| 3             | [MsgDelayMessage](https://github.com/dydxprotocol/v4-chain/blob/35b87db422b0ef4138101ba73b0f00d16780ba89/proto/dydxprotocol/delaymsg/tx.proto#L18)      | Transitions the orderbook created by `MsgCreateClobPair` to `ACTIVE` status, after some amount of blocks               | [delay_blocks](https://github.com/dydxprotocol/v4-chain/blob/35b87db422b0ef4138101ba73b0f00d16780ba89/proto/dydxprotocol/delaymsg/tx.proto#L27)         |

Notes:

- For guideline on choosing values for individual params, see next [section](./proposing_a_new_market.md#choosing-market-parameters).
- Liquidity tiers are mentioned throughout this page. The liquidity tier documentation can be found [here](../users-governance/functionalities.md#liquidity-tiers). 
- The exact ordering of messages above is necessary for successful onchain execution.
- Each of the 4 top-level messages should have `Authority = dydx10d07y265gmmuvt4z0w9aw880jnsr700jnmapky`, the [gov module](https://github.com/dydxprotocol/v4-chain/blob/5e72896719e2f8d2fe6e10fddbde18b363a6bbe3/protocol/app/module_accounts_test.go#L28).
- The `MsgCreateClobPair` message wrapped in `messages[3]: MsgDelayMessage` should have `Authority = dydx1mkkvp26dngu6n8rmalaxyp3gwkjuzztq5zx6tr`, the [delaymsg module](https://github.com/dydxprotocol/v4-chain/blob/5e72896719e2f8d2fe6e10fddbde18b363a6bbe3/protocol/app/module_accounts_test.go#L36).
- The identifier fields must be consistent for a perpetual market: `params.id`, `params.market_id`, `clob_pair.id`, `clob_pair.perpetual_clob_metadata.perpertual_id`.  An `id` value is valid as long as it's a `uint32` unique from existing markets (they do not need to follow existing market ids).

## Choosing Values for Market Parameters

The following decribes how to set various parameters for a new market and assumes that the market listed is:

- Safe (Not susceptible to market manipulation e.g. [Mango](https://www.coindesk.com/tech/2022/10/20/defi-exchange-mangos-114m-exploit-was-market-manipulation-not-a-hack-ex-fbi-special-agent-says/))
- Worth listing (Will this generate sufficient trading volume to consume throughput?)
- Oracle sources are known (Which spot exchanges should be selected when determining the oracle price?)

### Inputs

- Ticker Symbol (e.g. `BTC-USD` )
- Reference price (e.g. `40,000`) and `p` value
  - Defines the exponent on the reference price as `p:=FLOOR(log10(reference_price))`. For example: `p:=FLOOR(log10(40,000))=4`
- Exchanges required for oracles (`exchange_config_json`)
- Liquidity Tier (can be updated through governance vote at a later date.)
  - 0: Large Cap (BTC/ETH)
  - 1: Mid-Cap (Markets with at least 8 robust oracle sources with liquidity >= 50K on both sides and 30d daily spot trading volume >= $100M.)
  - 2: Long-tail (All others)

### Outputs

- See the [Parameter Calculator](https://docs.google.com/spreadsheets/d/1zjkV9R7R_7KMItuzqzvKGwefSBRfE-ZNAx1LH55OcqY/edit?usp=sharing) sheet to see an example of how output values are calculated from the input values of reference price and liquidity tier. 
- Below formulas ensure that 
  - Tick size is in the range of `[1, 10] bps` of the `reference_price` for markets in liquidity tier 1 and 2 and `[0.1, 1] bps` for markets in liquidity tier 0.
  - Minimum order size is `>= $1` and position size increments by approximately `$1`.

| Message Type                 | Field                         | Description                                                                                              | Value                                                                                |
| ---------------------------- | ----------------------------- | -------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------ |
| `MsgCreateOracleMarket`      | `exponent`                    | Denotes the number of decimals a value should be shifted in the price daemon                             | `p-9`                                                                                |
| `MsgCreateOracleMarket`      | `min_exchanges`               | Used for an index price to be valid.                                                                     | `3`                                                                                  |
| `MsgCreateOracleMarket`      | `min_price_change_ppm`        | The minimum amount the index price has to change for an oracle price update to be valid.                 | Liquidity Tier 0: `1000` <br> Liquidity Tier 1: `2500` <br> Liquidity Tier 2: `800` |
| `MsgCreateOracleMarket`      | `exchange_config_json`        | Spot exchange query configuration for the oracle price                                                   | See [below](./proposing_a_new_market.md#Choosing-oracle-sources)                     |
| `MsgCreatePerpetual`         | `atomic_resolution`           | L the exponent for converting an atomic amount (`size = 1`) to a full coin.                              | `-6 - p`                                                                             |
| `MsgCreatePerpetual`         | `default_funding_ppm`         | The default funding payment if there is no price premium. In parts-per-million.                          | `0`                                                                                  |
| `Msg[Update/Create]ClobPair` | `quantum_conversion_exponent` | `10^quantum_conversion_exponent` gives the number of quote quantum traded per base quantum.              | `-9`                                                                                 |
| `Msg[Update/Create]ClobPair` | `subticks_per_tick`           | Defines the tick size of the orderbook by defining how many subticks are in one tick.                    | Liquidity Tier 0: `100000` <br> Liquidity Tier 1 and 2 : `1000000`                   |
| `Msg[Update/Create]ClobPair` | `step_base_quantums`          | (aka step size): min increment in the size of orders (number of coins) on the CLOB in base quantums.     | `1000000`                                                                            |
| `MsgDelayMessage`            | `delay_blocks`                | number of blocks before which the `MsgUpdateClobPair` is executed and transitions the market to `ACTIVE` | `3600` (equal to an hour at `1 sec` blocktime)                                       |


## Choosing oracle sources

One way of evaluating whether a new market is optimally compatible with the software is based on the number of 1. robust oracles and 2. queryable oracles. A market should have at least 6 robust oracles to deter oracle manipulation attacks and 5 queryable oracles to prevent consensus failures.

To select robust oracle sources, follow the procedure below: 

1. Find spot market tickers from eligible exchanges with the desired symbol as the base asset. The quote asset should be USD, USDT, BTC, or ETH. See [below](./proposing_a_new_market.md###List-of-eligible-exchanges) for a list of eligible exchanges. Note that pools in certain DEXes are eligible to be considered a robust source but no DEXes is queryable as of 3/5/24. 
  - If the quote asset is not USD, add the following flag `"adjustByMarket":"quote_asset-USD"`. This flag ensures that the base asset oracle price is adjusted by the oracle price of the quote asset. 
2. Currently the software supports only one source from an exchange per market. Among the tickers from an exchange, choose the most liquid spot market with the highest trading volume. If one market is more liquid but another has more trading volume, choose the one with deeper liquidity. 
  - When counting the number of robust oracles, two pools with different quote assets from one DEX can be considered as two independent sources. DEX pools can have quote assets that are not specified above. 
3. Exclude oracle sources that do not meet the depth and daily trading volume threshold over the past month. 
  - Both sides of liquidity at 2% from the midprice should be at least `$50,000`. 
  - The average daily trading volume should be at least `$100,000`. 
4. Ensure there are at least 6 robust sources that meet the depth and trading volume requirement and 5 of them are queryable. If there are less than 6 sources, this market should not be added to prevent potential market manipulation attacks and consensus failures from oracle price updates unless more robust oracle sources are available and/or queryable.

### List of eligible exchanges

Recommended Exchanges:
- Binance
- Coinbase
- OKX
- Bybit
- Gate
- Kraken
- Kucoin
- MEXC

Only use if necessary:
- HTX (previously Huobi)
- Bitstamp

Not recommended: 
- Bitfinex
- BinanceUS
- Crypto.com

Recommended DEX sources (can be considered for robust oracles but are not queryable):
- Uniswap V2/V3
- Raydium
- Orca
- Osmosis

Exchanges not included in the above list are not currently supported by the software.

### Recently listed markets
If a market is relatively new, one month of past liquidity and volume data may not be available. If the underlying token launched within 1 day, one can consider the modified requirement below to ensure compatibility and relevance without sufficient data.
1. There should be at least 4 oracle sources that meet the following criteria:
  - Both sides of liquidity at 2% from the midprice should be at least `$50,000`. 
  - The 24 hour trading volume should be at least `$1,000,000`. 
2. Additionally, there should be 2 oracle sources that meet the following criteria:
  - Both sides of liquidity at 2% from the midprice should be at least `$30,000`. 
  - The 24 hour trading volume should be at least `$1,000,000`. 
3. At least 5 of the oracle sources should be queryable. 

## Example

### Example of markets with robust oracle sources
Here is a [list](https://docs.google.com/spreadsheets/d/1zjkV9R7R_7KMItuzqzvKGwefSBRfE-ZNAx1LH55OcqY/edit#gid=1489690476) of certain markets and their oracle sources, likely compatibilility with optimal software performance, and parameters, based on the methodology above.  

### `exchange_config_json`

Below is an example `json` string for `exchange_config_json`. To convert this string into a single-line, quote-escaped string:

```bash
cat exchange_config.json | jq -c . | sed 's/"/\\"/g'
```

```json
{
   "exchanges":[
      {
         "exchangeName":"Binance",
         "ticker":"BTCUSDT",
         "adjustByMarket":"USDT-USD"
      },
      {
         "exchangeName":"Bybit",
         "ticker":"BTCUSDT",
         "adjustByMarket":"USDT-USD"
      },
      {
         "exchangeName":"CoinbasePro",
         "ticker":"BTC-USD"
      },
      {
         "exchangeName":"Huobi",
         "ticker":"btcusdt",
         "adjustByMarket":"USDT-USD"
      },
      {
         "exchangeName":"Kraken",
         "ticker":"XXBTZUSD"
      },
      {
         "exchangeName":"Kucoin",
         "ticker":"BTC-USDT",
         "adjustByMarket":"USDT-USD"
      },
      {
         "exchangeName":"Mexc",
         "ticker":"BTC_USDT",
         "adjustByMarket":"USDT-USD"
      },
      {
         "exchangeName":"Okx",
         "ticker":"BTC-USDT",
         "adjustByMarket":"USDT-USD"
      }
   ]
}
```

### Example Proposal Json

Below is an example proposal JSON file to propose adding `BTC-USD` as a new perpetual market (if it had not been added yet).

```json
{
    "title": "Add BTC-USD perpetual market",
    "deposit": "10000000000000000000000adv4tnt",
    "summary": "Add the `x/prices`, `x/perpetuals` and `x/clob` parameters needed for a BTC-USD perpetual market. Create the market in `INITIALIZING` status and transition it to `ACTIVE` status after 3600 blocks.",
    "messages": [
      {
        "@type": "/dydxprotocol.prices.MsgCreateOracleMarket",
        "authority": "dydx10d07y265gmmuvt4z0w9aw880jnsr700jnmapky",
        "params": {
            "exchange_config_json": "{\"exchanges\":[{\"exchangeName\":\"Binance\",\"ticker\":\"BTCUSDT\",\"adjustByMarket\":\"USDT-USD\"},{\"exchangeName\":\"Bybit\",\"ticker\":\"BTCUSDT\",\"adjustByMarket\":\"USDT-USD\"},{\"exchangeName\":\"CoinbasePro\",\"ticker\":\"BTC-USD\"},{\"exchangeName\":\"Huobi\",\"ticker\":\"btcusdt\",\"adjustByMarket\":\"USDT-USD\"},{\"exchangeName\":\"Kraken\",\"ticker\":\"XXBTZUSD\"},{\"exchangeName\":\"Kucoin\",\"ticker\":\"BTC-USDT\",\"adjustByMarket\":\"USDT-USD\"},{\"exchangeName\":\"Mexc\",\"ticker\":\"BTC_USDT\",\"adjustByMarket\":\"USDT-USD\"},{\"exchangeName\":\"Okx\",\"ticker\":\"BTC-USDT\",\"adjustByMarket\":\"USDT-USD\"}]}",
            "exponent": -5,
            "id": 1001,
            "min_exchanges": 3,
            "min_price_change_ppm": 1000,
            "pair": "BTC-USD"
        }
      },
      {
        "@type": "/dydxprotocol.perpetuals.MsgCreatePerpetual",
        "authority": "dydx10d07y265gmmuvt4z0w9aw880jnsr700jnmapky",
        "params": {
            "atomic_resolution": -10,
            "default_funding_ppm": 0,
            "id": 1001,
            "liquidity_tier": 0,
            "market_id": 1001,
            "ticker": "BTC-USD"
        }
      },
      {
        "@type": "/dydxprotocol.clob.MsgCreateClobPair",
        "authority": "dydx10d07y265gmmuvt4z0w9aw880jnsr700jnmapky",
        "clob_pair": {
            "id": 1001,
            "perpetual_clob_metadata": {
              "perpetual_id": 1001
            },
            "quantum_conversion_exponent": -9,
            "status": "STATUS_INITIALIZING",
            "step_base_quantums": 1000000,
            "subticks_per_tick": 100000
        }
      },
      {
        "@type": "/dydxprotocol.delaymsg.MsgDelayMessage",
        "authority": "dydx10d07y265gmmuvt4z0w9aw880jnsr700jnmapky",
        "msg": {
            "@type": "/dydxprotocol.clob.MsgUpdateClobPair",
            "authority": "dydx1mkkvp26dngu6n8rmalaxyp3gwkjuzztq5zx6tr",
            "clob_pair": {
                "id": 1001,
                "perpetual_clob_metadata": {
                  "perpetual_id": 1001
                },
                "quantum_conversion_exponent": -9,
                "status": "STATUS_ACTIVE",
                "step_base_quantums": 1000000,
                "subticks_per_tick": 100000
            }
        },
        "delay_blocks" : 3600
      }
    ]
  }
  ```

## Submitting an Onchain Proposal

Follow instructions [here](./submitting_a_proposal.md) to submit an onchain proposal.


#### Disclaimer
Users considering using the permissionless markets function of the dYdx v4 software are 
encouraged to consult qualified legal counsel to ensure compliance with the laws of their 
jurisdiction. The information on this page does not constitute and should not be relied on as 
investment, legal, or any other form of professional advice. This page does not recommend 
any specific market, and analyzes only compatibility and functionality from a technical 
standpoint. Use of the v4 software is prohibited in the United States, Canada, and 
sanctioned jurisdictions as described in the [v4 Terms of Use](https://dydx.exchange/v4-terms).


# File: v4-documentation/old-docs/pages/users-governance/reading_new_market_proposal.md

# Reading a Proposal
A governance proposal is a json document submitted to the dYdX Chain governance module. One of the most popular types of governance proposals is a new market proposal which add new markets to the dYdX Chain if passed. A new market proposal specifies parameters necessary to specify a market, such as the name of the market, oracle sources, and liquidity tier. This page will outline how to interpret the market parameters so that the community can assess the proposal and be prepared to trade with correct configurations if the market becomes live. See [proposing a new market](../users-governance/proposing_a_new_market.md) for more information on how the market parameters can be calculated.


## Example Proposal
Below is an example proposal JSON file for adding a perpetual market, `BTC-USD`.

```json
{
    "title": "Add BTC-USD perpetual market",
    "deposit": "10000000000000000000000adv4tnt",
    "summary": "Add the `x/prices`, `x/perpetuals` and `x/clob` parameters needed for a BTC-USD perpetual market. Create the market in `INITIALIZING` status and transition it to `ACTIVE` status after 3600 blocks.",
    "messages": [
      {
        "@type": "/dydxprotocol.prices.MsgCreateOracleMarket",
        "authority": "dydx10d07y265gmmuvt4z0w9aw880jnsr700jnmapky",
        "params": {
            "exchange_config_json": "{\"exchanges\":[{\"exchangeName\":\"Binance\",\"ticker\":\"BTCUSDT\",\"adjustByMarket\":\"USDT-USD\"},{\"exchangeName\":\"Bybit\",\"ticker\":\"BTCUSDT\",\"adjustByMarket\":\"USDT-USD\"},{\"exchangeName\":\"CoinbasePro\",\"ticker\":\"BTC-USD\"},{\"exchangeName\":\"Huobi\",\"ticker\":\"btcusdt\",\"adjustByMarket\":\"USDT-USD\"},{\"exchangeName\":\"Kraken\",\"ticker\":\"XXBTZUSD\"},{\"exchangeName\":\"Kucoin\",\"ticker\":\"BTC-USDT\",\"adjustByMarket\":\"USDT-USD\"},{\"exchangeName\":\"Mexc\",\"ticker\":\"BTC_USDT\",\"adjustByMarket\":\"USDT-USD\"},{\"exchangeName\":\"Okx\",\"ticker\":\"BTC-USDT\",\"adjustByMarket\":\"USDT-USD\"}]}",
            "exponent": -5,
            "id": 1001,
            "min_exchanges": 3,
            "min_price_change_ppm": 1000,
            "pair": "BTC-USD"
        }
      },
      {
        "@type": "/dydxprotocol.perpetuals.MsgCreatePerpetual",
        "authority": "dydx10d07y265gmmuvt4z0w9aw880jnsr700jnmapky",
        "params": {
            "atomic_resolution": -10,
            "default_funding_ppm": 0,
            "id": 1001,
            "liquidity_tier": 0,
            "market_id": 1001,
            "ticker": "BTC-USD"
        }
      },
      {
        "@type": "/dydxprotocol.clob.MsgCreateClobPair",
        "authority": "dydx10d07y265gmmuvt4z0w9aw880jnsr700jnmapky",
        "clob_pair": {
            "id": 1001,
            "perpetual_clob_metadata": {
              "perpetual_id": 1001
            },
            "quantum_conversion_exponent": -9,
            "status": "STATUS_INITIALIZING",
            "step_base_quantums": 1000000,
            "subticks_per_tick": 100000
        }
      },
      {
        "@type": "/dydxprotocol.delaymsg.MsgDelayMessage",
        "authority": "dydx10d07y265gmmuvt4z0w9aw880jnsr700jnmapky",
        "msg": {
            "@type": "/dydxprotocol.clob.MsgUpdateClobPair",
            "authority": "dydx1mkkvp26dngu6n8rmalaxyp3gwkjuzztq5zx6tr",
            "clob_pair": {
                "id": 1001,
                "perpetual_clob_metadata": {
                  "perpetual_id": 1001
                },
                "quantum_conversion_exponent": -9,
                "status": "STATUS_ACTIVE",
                "step_base_quantums": 1000000,
                "subticks_per_tick": 100000
            }
        },
        "delay_blocks" : 3600
      }
    ]
  }
```

### Understanding Proposal Values

A new market proposal consists of 4 messages: 

1. Create Oracle Market
2. Create Perpetual
3. Create CLOB Pair
4. Delay Message

#### Create Oracle Market
Create Oracle Market message specifies the oracle sources and their parameters that will be used to compute the oracle price. 
- `exchange_config_json` includes the exchange, ticker, and parameters (if applicable) that constitute oracle sources. 
  - adjust_by_market specifies the ticker to adjust the returned price if the quote asset for the spot ticker is not USD. ex: If the spot ticker is BTCUSDT, the adjust_by_market may be USDT-USD.
  - invert specifies whether to invert the price. ex: If the oracle market is TRY-USD and the spot ticker is USDTTRY, the invert may be true.
- `exponent` is the number of decimal places to use to show prices.
- `id` is the id of the oracle market. This should be the same as the perpetual_id and clob_pair_id.
- `min_exchanges` is the number of exchanges that should be responsive for the oracle price to be updated in that block.
- `min_price_change_ppm` is the threshold for which the oracle price will update only if the proposed price change is greater than min_price_change_ppm. 
- `pair` is the ticker of the market being added.

#### Create Perpetual
Create Perpetual message specifies the parameters specific to the perpetual.
- `atomic_resolution` determines the precision of the size of the coin. If the atomic resolution is -10, then the perpetual positions are represented as multiples of 10^-10.
- `default_funding_ppm` is the default funding rate in parts per million.
- `id` is the id of the perpetual. This should be the same as the oracle_market_id and clob_pair_id.
- `liquidity_tier` is the liquidity tier of the proposed market. This should be set based on [dYdX liquidity tier guidelines](./functionalities.md#liquidity-tiers)
- `market_id` is the id of the oracle market. This should be the same as the id.
- `ticker` is the ticker of the market being added.

#### Create CLOB Pair
Create CLOB Pair message sets up the orderbook parameters for the market.
- `id` is the id of the CLOB pair. This should be the same as the oracle_market_id and perpetual_id.
- `perpetual_clob_metadata.perpetual_id` is the id of the perpetual. This should be the same as the id.
- `quantum_conversion_exponent`is used to convert the value of a position in protocol to/from a human readable value in $.
- `status` is set to "STATUS_INITIALIZING" to create the market in initializing status.
- `step_base_quantums` deteremines `step_size`, which is the minimum amount by which you can increase or decrease an order.
- `subticks_per_tick` determines the `tick_size` for the market. 

#### Delay Message
Delay Message is used to transition the market from INITIALIZING to ACTIVE status after a specified number of blocks.
- `clob_pair` contains the same parameters as in the Create CLOB Pair message, but with `status` set to "STATUS_ACTIVE".
- `delay_blocks` specifies the number of blocks to wait before activating the market.

### Derived Values
You can calculate the following values based on parameters in a new market proposal.

- Tick Size:
  - Minimum amount in USDC by which valid prices for an order increment by. The formula corresponds to the tick size falling between 1 and 10 bps of the base asset price in USDC.
  -`tick_size` = `subtick_size` * `subticks_per_tick` where `subtick_size` = 10^(-`atomic_resolution` + `quantum_conversion_exponent` + `quote_quantum_resolution`) and `quote_quantum_resolution := -6` for USDC.

- Step Size:
  - Minimum amount in base_asset by which you can increase or decrease an order. This formula corresponds to the step size falling between 1 and 10 USDC.
  - `step_size` = 10^(`atomic_resolution`) * `step_base_quantums`

- Minimum Order Size:
  - Minimum amount in base_asset required to place an order. Protocol uses the same values for step size and minimum order size.
  - `min_order_size` = 10^ (`atomic_resolution`) * `step_base_quantums`

- From the example proposal above, we can calculate the above values for `BTC-USD` as the following:
  - `tick_size` = `subtick_size` * `subticks_per_tick` = 10^(10 - 9 - 6) * 100000 = $1
  - `step_size` = 10^(-10) * 1000000 = 0.0001 BTC
  - `min_order_size` = 10^(-10) * 1000000 = 0.0001 BTC

## Next Steps
If you are a dYdX Chain user, you can [vote on a proposal](../users-governance/voting.md) or [submit your own](../users-governance/submitting_a_proposal.md).

If you are a market maker aiming to provide liquidity to a new market, you can configure a trading strategy using values and derived values from the proposal.


# File: v4-documentation/old-docs/pages/users-governance/slashing_a_validator.md

# Slashing a validator

The chain supports slashing of misbehaving validators through governance vote.

## Proposal Message

The proposal should contain a single [MsgSlashValidator](https://github.com/dydxprotocol/v4-chain/blob/4eb219b1b726df9ba17c9939e8bb9296f5e98bb3/proto/dydxprotocol/govplus/tx.proto#L19) message for each validator that should be slashed.

Notes:
- The slashing will occur when the proposal is passed, not the `infraction_height`.
- The `infraction_height` must be set so that `time(proposal pass height) - time(infraction_height) < unbonding period`. Typically a good choice for `infraction_height` is the current height unless there is a recent unbonding undelegation/redelegation that should be included in the slash. In that case the `infraction_height` should be set prior to the initiation of the undelegation/redelegation.
- Both `tokens_at_infraction_height` and `slash_factor` must be set correctly, otherwise undelegations and redelegations might be slashed disproportionately to the rest of the validator's stake. `tokens_at_infraction_height * slash_factor` determines the total amount of tokens to be slashed. Unbonding delegations and redelegations are first slashed by `slash_factor`, and then the remaining amount is taken from the validator's stake.
- The x/staking `HistoricalInfo` query endpoint can be used to find the correct value for `tokens_at_infraction_height`.
- See the [MsgSlashValidator](https://github.com/dydxprotocol/v4-chain/blob/4eb219b1b726df9ba17c9939e8bb9296f5e98bb3/proto/dydxprotocol/govplus/tx.proto#L19) inline comments for further details on the above requirements.

### Example Proposal Json

Below is an example proposal JSON file to propose a slashing a validator's total bonded tokens (both user delegated and self-delegated) by 0.2 at block height 5000. In other words:
* assuming that the proposal passes governance vote
* assuming that the validator has 1000 total bonded tokens at height 5000
* once the proposal is passed, the validator will lose 200 tokens
* if there are unbonding undelegations and redelegations since height 5000, they will lose 0.2 of their stake, and the remaining will be taken from the validator for a total of 200 tokens lost
```json
{
    "title": "Slash a validator",
    "summary": "We are proposing to slash this misbehaving validator for X reasons.",
    "deposit": "10000000000000000000000adv4tnt",
    "messages": [
        {
          "@type": "/dydxprotocol.govplus.MsgSlashValidator",
          "authority": "dydx10d07y265gmmuvt4z0w9aw880jnsr700jnmapky",
          "validator_address": "dydxvalcons1z79h40nmd777scs93qjxaeak8m2cl6hpqg2rx9",
          "slash_factor": "0.2",
          "tokens_at_infraction_height": "1000",
          "infraction_height": 5000
        }
    ]
}
  ```

## Submitting an Onchain Proposal

Follow instructions [here](./submitting_a_proposal.md) to submit an onchain proposal.


# File: v4-documentation/old-docs/pages/users-governance/submitting_a_proposal.md

# Submitting a Proposal

## Obtaining the `dydxprotocold` Binary
For instructions on compiling the `protocold` binary locally, refer to the dYdX Protocol's [README](https://github.com/dydxprotocol/v4-chain/tree/main/protocol#readme).

Alternatively, if your platform is supported by the prebuilt binaries found in the [releases section](https://github.com/dydxprotocol/v4-chain/releases) of the repository, you can opt to download and use these binaries directly.

## Save your Chain ID in `dydxprotocold` config
Save the [chain-id](../infrastructure_providers-network/network_constants.mdx#chain-id). This will make it so you do not have to manually pass in the chain-id flag for every CLI command.

```bash
dydxprotocold config set client chain-id [chain_id]
```

## Confirming Connectivity
To ensure that you are successfully connecting, use any of the RPC endpoints listed in the [resources](../infrastructure_providers-network/resources.mdx#full-node-endpoints). Remember to append `:443` to the end of the RPC URI for proper access. Execute the following command, replacing `[RPC ENDPOINT]` with your chosen endpoint:

```bash
dydxprotocold status --node https://[RPC ENDPOINT]:443
```

## Registering an Account in the Keychain
- Choose a unique key name to replace `[KEY NAME]`. This name will be used to identify your key within the keychain.
```bash
dydxprotocold keys add [KEY NAME] --recover
```
- Input your MNEMONIC into the terminal when prompted.

## Crafting a Proposal File
To create a proposal, follow the template provided below. This structure outlines the essential elements of a proposal, including its title, deposit amount, summary, and specific messages. 

```json
{
  "title": "[TEXT TITLE OF THE PROPOSAL]",
  "deposit": "[DEPOSIT AMOUNT IN NATIVE COINS - INCLUDE DENOMINATION]",
  "summary": "[TEXT SUMMARY OF THE PROPOSAL]",
  "messages": [
      {
          [MESSAGE 1]
      },
      {
          [MESSAGE 2]
      },
      ...
  ]
}
```

Once you have filled in the necessary details, save this structure as a JSON file. This file will be used in the submission process of your proposal.

## Submitting the Proposal
```bash
dydxprotocold tx gov submit-proposal [PROPOSAL JSON FILE] --from [KEY NAME] --gas auto --fees [FEE AMOUNT IN TOKEN DENOMINATION] --node https://[RPC ENDPOINT]:443
```
- `[PROPOSAL JSON FILE]`: This is the path to the JSON file containing your proposal details.
- `[KEY NAME]`: This refers to the name of the key you added to your dYdX keychain. It identifies the account from which the proposal is being submitted. Replace this with the key name you chose when you added your account to the keychain.
- `[FEE AMOUNT IN TOKEN DENOMINATION]`: This is the transaction fee for submitting the proposal, specified in the native token of the dYdX blockchain. You need to replace this with the actual amount and the token denomination.
- `[RPC ENDPOINT]`: This is the endpoint of the RPC (Remote Procedure Call) node you are connecting to on the dYdX network. Replace this with the actual RPC endpoint URL you intend to use. Make sure to include `:443` at the end of the URL for the correct port.


# File: v4-documentation/old-docs/pages/users-governance/voting.md

# Voting

## Save your Chain ID in `dydxprotocold` config

Save the [chain-id](../infrastructure_providers-network/network_constants.mdx#chain-id). This will make it so you do not have to manually pass in the chain-id flag for every CLI command.

```bash
dydxprotocold config set client chain-id [chain_id]
```

## View the status of a proposal

To view the status of a proposal, use the following command:

```bash
dydxprotocold query gov proposal [proposal_id]
```

The status of the proposal will be returned:

```bash
deposit_end_time: "2023-04-02T19:21:27.467932675Z"
final_tally_result:
  abstain_count: "0"
  no_count: "0"
  no_with_veto_count: "0"
  yes_count: "0"
id: "1"
messages:
- '@type': /cosmos.upgrade.v1beta1.MsgSoftwareUpgrade
  authority: dydx10d07y265gmmuvt4z0w9aw880jnsr700jnmapky
  plan:
    height: "60400"
    info: ""
    name: v0.1.0
    time: "0001-01-01T00:00:00Z"
    upgraded_client_state: null
metadata: ""
proposer: dydx199tqg4wdlnu4qjlxchpd7seg454937hjrknju4
status: PROPOSAL_STATUS_VOTING_PERIOD
submit_time: "2023-03-31T19:21:27.467932675Z"
summary: This is a proposal to schedule v0.1.0 software upgrade at block height 60400,
  estimated to occur on Tuesday April 4th at 1PM EDT.
title: dYdX Protocol v1.0.0 Upgrade
total_deposit:
- amount: "10000000"
  denom: stake
voting_end_time: "2023-03-31T19:22:27.467932675Z"
voting_start_time: "2023-03-31T19:21:27.467932675Z"
```

## Voting for a proposal

To vote for a governance proposal, use the following command:

```bash
dydxprotocold tx gov vote [proposal_id] [option] --from [key]
```

The option can be either `Yes`, `No`, `NoWithVeto`, `Abstain`. See [here](https://docs.cosmos.network/v0.47/modules/gov#option-set) for the descriptions of the these options.

## To see the votes

```bash
dydxprotocold query gov votes [proposal_id]
```

```bash
pagination:
  next_key: null
  total: "0"
votes:
- metadata: ""
  options:
  - option: VOTE_OPTION_YES
    weight: "1.000000000000000000"
  proposal_id: "1"
  voter: dydx199tqg4wdlnu4qjlxchpd7seg454937hjrknju4
...
```

## To see the tally of votes

To query tally of votes on a proposal:

```bash
dydxprotocold query gov tally [proposal_id]
```

This will return something like:

```bash
abstain_count: "0"
no_count: "0"
no_with_veto_count: "0"
yes_count: "0"

```


