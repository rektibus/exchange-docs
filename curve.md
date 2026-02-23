# Curve API Documentation

Auto-fetched from 1 page(s)


---

# Source: https://docs.curve.fi/

[](https://docs.curve.finance/cdn-cgi/content?id=ORCMnezDBrvEzKyTdprlkWO_AKnSnRikB12NaZiBhVU-1771865227.847331-1.0.1.1-7PqjjwGzy905wuMOtTG1g4mMyj5i1wqm_5_70kI7Yxk)

New documentation for Savings crvUSD (scrvUSD) is now available! Learn about the Vault implementation, Rewards Distribution, and more in the [scrvUSD section](/scrvusd/overview/). 

[ ](. "Curve Technical Docs")

Curve Technical Docs 

Home 

Initializing search 




[ CurveDocs/curve-docs  ](https://github.com/CurveDocs/curve-docs "Go to repository")

# Curve Technical Docs

Comprehensive documentation detailing the architecture, functionality, and security aspects of Curve's core smart contracts, exchange contracts, and crvUSD stablecoin.

[ Overview ](/documentation-overview/ "Protocol Overview") [ Integration Docs ](/integration/overview/ "Integration")

[ ](. "Curve Technical Docs") Curve Technical Docs 

[ CurveDocs/curve-docs  ](https://github.com/CurveDocs/curve-docs "Go to repository")

  * [ Documentation Overview  ](documentation-overview/)
  * [ Curve DAO Token  ](curve_dao/crv-token/)
  * Vote-Escrowed CRV  Vote-Escrowed CRV 
    * [ VotingEscrow (veCRV)  ](curve_dao/voting-escrow/voting-escrow/)
    * [ SmartWalletChecker  ](curve_dao/voting-escrow/smartwalletchecker/)
    * Crosschain veCRV  Crosschain veCRV 
      * [ veCRV Oracle  ](curve_dao/voting-escrow/crosschain/vecrv-oracle/)
      * [ veCRV Delegation  ](curve_dao/voting-escrow/crosschain/vecrv-delegation/)
      * [ veCRV Verifiers  ](curve_dao/voting-escrow/crosschain/vecrv-verifiers/)
  * Liquidity Gauges and Minting CRV  Liquidity Gauges and Minting CRV 
    * [ Overview & Implementation  ](liquidity-gauges-and-minting-crv/overview/)
    * [ GaugeController  ](liquidity-gauges-and-minting-crv/gauge-controller/GaugeController/)
    * [ Minter  ](liquidity-gauges-and-minting-crv/minter/Minter/)
    * Gauges  Gauges 
      * [ Overview  ](liquidity-gauges-and-minting-crv/gauges/overview/)
      * [ LiquidityGaugeV6  ](liquidity-gauges-and-minting-crv/gauges/LiquidityGaugeV6/)
    * Gauges for EVM Sidechains  Gauges for EVM Sidechains 
      * [ Overview  ](liquidity-gauges-and-minting-crv/xchain-gauges/overview/)
      * [ RootGaugeFactory  ](liquidity-gauges-and-minting-crv/xchain-gauges/RootGaugeFactory/)
      * [ ChildGaugeFactory  ](liquidity-gauges-and-minting-crv/xchain-gauges/ChildGaugeFactory/)
      * [ RootGauge  ](liquidity-gauges-and-minting-crv/xchain-gauges/RootGauge/)
      * [ ChildGauge  ](liquidity-gauges-and-minting-crv/xchain-gauges/ChildGauge/)
      * [ Bridgers  ](liquidity-gauges-and-minting-crv/xchain-gauges/Bridgers/)
  * Governance and Voting  Governance and Voting 
    * [ Overview  ](governance/overview/)
    * [ Curve Voting Library  ](governance/curve-dao/)
    * L2 Governance (x-gov)  L2 Governance (x-gov) 
      * [ Overview  ](governance/x-gov/overview/)
      * [ Broadcaster  ](governance/x-gov/broadcaster/)
      * [ Relayer  ](governance/x-gov/relayer/)
      * [ Agents  ](governance/x-gov/agents/)
      * [ Vault  ](governance/x-gov/vault/)
  * Fee Collection & Distribution  Fee Collection & Distribution 
    * [ Overview  ](fees/overview/)
    * [ FeeSplitter  ](fees/FeeSplitter/)
    * [ FeeCollector  ](fees/FeeCollector/)
    * [ CoWSwapBurner  ](fees/CowSwapBurner/)
    * [ Hooker  ](fees/Hooker/)
    * [ FeeDistributor  ](fees/FeeDistributor/)
    * Original Architecture  Original Architecture 
      * [ Overview  ](fees/original-architecture/overview/)
      * [ Burner  ](fees/original-architecture/burner/)
      * [ FeeDistributor  ](fees/original-architecture/distributor/)
      * [ Sidechains  ](fees/original-architecture/sidechains/)
      * [ Withdraw and Burn  ](fees/original-architecture/withdraw-and-burn/)
  * Registry  Registry 
    * [ Overview  ](registry/overview/)
    * [ MetaRegistry API  ](registry/MetaRegistryAPI/)
  * Curve API  Curve API 
    * [ curve-api  ](curve-api/curve-api/)
    * [ curve-prices  ](curve-api/curve-prices/)
  * Routers  Routers 
    * [ CurveRouterNG  ](router/CurveRouterNG/)
    * [ CurveRegistryExchange  ](router/CurveRegistryExchange/)
  * Curve Block Oracle  Curve Block Oracle 
    * [ Overview  ](block-oracle/overview/)
    * [ BlockOracle  ](block-oracle/BlockOracle/)
    * [ MainnetBlockView  ](block-oracle/MainnetBlockView/)
    * [ HeaderVerifier  ](block-oracle/HeaderVerifier/)
    * [ LZBlockRelay  ](block-oracle/LZBlockRelay/)
  * Fast Bridge  Fast Bridge 
    * [ Overview  ](fast-bridge/overview/)
    * [ FastBridgeL2  ](fast-bridge/FastBridgeL2/)
    * [ FastBridgeVault  ](fast-bridge/FastBridgeVault/)
    * [ L2MessengerLZ  ](fast-bridge/L2MessengerLZ/)
    * [ VaultMessengerLZ  ](fast-bridge/VaultMessengerLZ/)
  * crvUSD  crvUSD 
    * [ Overview  ](crvUSD/overview/)
    * [ crvUSD Token  ](crvUSD/crvUSD/)
    * [ Controller  ](crvUSD/controller/)
    * [ LLAMMA  ](crvUSD/amm/)
    * [ Monetary Policy  ](crvUSD/monetarypolicy/)
    * [ PriceAggregator  ](crvUSD/priceaggregator/)
    * [ Oracle  ](crvUSD/oracle/)
    * [ FlashLender  ](crvUSD/flashlender/)
    * PegKeepers  PegKeepers 
      * [ Overview  ](crvUSD/pegkeepers/overview/)
      * [ PegKeeperV1  ](crvUSD/pegkeepers/PegKeeperV1/)
      * [ PegKeeperV2  ](crvUSD/pegkeepers/PegKeeperV2/)
      * [ PegKeeperRegulator  ](crvUSD/pegkeepers/PegKeeperRegulator/)
    * Leverage  Leverage 
      * [ Overview  ](crvUSD/leverage/overview/)
      * [ Curve Pools  ](crvUSD/leverage/LeverageZap/)
      * [ 1inch Router  ](crvUSD/leverage/LeverageZap1inch/)
      * [ Odos Router  ](crvUSD/leverage/LlamaLendOdosLeverageZap/)
    * Factory  Factory 
      * [ Overview  ](crvUSD/factory/overview/)
      * [ Deployer API  ](crvUSD/factory/deployer-api/)
      * [ Admin Controls  ](crvUSD/factory/admin-controls/)
  * Savings crvUSD  Savings crvUSD 
    * [ Overview  ](scrvusd/overview/)
    * [ RewardsHandler  ](scrvusd/RewardsHandler/)
    * [ StablecoinLens  ](scrvusd/StablecoinLens/)
    * Crosschain Oracles  Crosschain Oracles 
      * [ Oracle V0  ](scrvusd/crosschain/oracle-v0/oracle/)
      * Oracle V1/V2  Oracle V1/V2 
        * [ Overview  ](scrvusd/crosschain/oracle-v2/overview/)
        * [ Oracle  ](scrvusd/crosschain/oracle-v2/oracle/)
        * [ Verifier  ](scrvusd/crosschain/oracle-v2/verifier/)
        * [ BlockHash  ](scrvusd/crosschain/oracle-v2/blockhash/)
  * Curve Lending  Curve Lending 
    * [ Overview  ](lending/overview/)
    * [ Vault  ](lending/contracts/vault/)
    * [ LLAMMA and Controller  ](lending/contracts/controller-llamma/)
    * [ OneWay Lending Factory  ](lending/contracts/oneway-factory/)
    * [ Leverage  ](lending/contracts/leverage/)
    * Monetary Policies  Monetary Policies 
      * [ Overview  ](lending/contracts/mp-overview/)
      * [ Semilog Monetary Policy  ](lending/contracts/semilog-mp/)
      * [ Secondary Monetary Policy  ](lending/contracts/secondary-mp/)
    * Oracles Contracts  Oracles Contracts 
      * [ Overview & Examples  ](lending/contracts/oracle-overview/)
      * [ CryptoFromPool.vy  ](lending/contracts/cryptofrompool/)
      * [ CryptoFromPoolsRate.vy  ](lending/contracts/cryptofrompoolsrate/)
      * [ CryptoFromPoolVault.vy  ](lending/contracts/cryptofrompoolvault/)
  * Stableswap Exchange  Stableswap Exchange 
    * [ Overview  ](stableswap-exchange/overview/)
    * Stableswap  Stableswap 
      * Pools  Pools 
        * [ Overview  ](stableswap-exchange/stableswap/pools/overview/)
        * [ Plain Pools  ](stableswap-exchange/stableswap/pools/plain_pools/)
        * [ Lending Pools  ](stableswap-exchange/stableswap/pools/lending_pools/)
        * [ Metapools  ](stableswap-exchange/stableswap/pools/metapools/)
        * [ Admin Controls  ](stableswap-exchange/stableswap/pools/admin_pool_settings/)
      * Liquidity Pool Tokens  Liquidity Pool Tokens 
        * [ Overview  ](stableswap-exchange/stableswap/lp_tokens/overview/)
        * [ Curve Token V1  ](stableswap-exchange/stableswap/lp_tokens/curve_token_v1/)
        * [ Curve Token V2  ](stableswap-exchange/stableswap/lp_tokens/curve_token_v2/)
        * [ Curve Token V3  ](stableswap-exchange/stableswap/lp_tokens/curve_token_v3/)
      * Deposit Contracts  Deposit Contracts 
        * [ Overview  ](stableswap-exchange/stableswap/deposit_contracts/overview/)
        * [ Lending Pool Deposits  ](stableswap-exchange/stableswap/deposit_contracts/lending_pool_deposits/)
        * [ Metapool Deposits  ](stableswap-exchange/stableswap/deposit_contracts/metapool_deposits/)
    * Stableswap-NG  Stableswap-NG 
      * [ Overview  ](stableswap-exchange/stableswap-ng/overview/)
      * Pools  Pools 
        * [ Overview  ](stableswap-exchange/stableswap-ng/pools/overview/)
        * [ Plain Pools  ](stableswap-exchange/stableswap-ng/pools/plainpool/)
        * [ Metapools  ](stableswap-exchange/stableswap-ng/pools/metapool/)
        * [ Oracles  ](stableswap-exchange/stableswap-ng/pools/oracles/)
        * [ Admin Controls  ](stableswap-exchange/stableswap-ng/pools/admin_controls/)
      * Utility Contracts  Utility Contracts 
        * [ Math  ](stableswap-exchange/stableswap-ng/utility_contracts/math/)
        * [ Views  ](stableswap-exchange/stableswap-ng/utility_contracts/views/)
      * Custom Implementations  Custom Implementations 
        * [ Custom Admin Controls (EYWA)  ](stableswap-exchange/stableswap-ng/implementations/custom1/)
  * Cryptoswap Exchange  Cryptoswap Exchange 
    * [ Overview  ](cryptoswap-exchange/overview/)
    * [ In Depth  ](cryptoswap-exchange/in-depth/)
    * Cryptoswap  Cryptoswap 
      * Pools  Pools 
        * [ Crypto Pool  ](cryptoswap-exchange/cryptoswap/pools/crypto-pool/)
        * [ Admin Controls  ](cryptoswap-exchange/cryptoswap/pools/admin-controls/)
      * Liquidity Pool Tokens  Liquidity Pool Tokens 
        * [ Overview  ](cryptoswap-exchange/cryptoswap/lp_tokens/overview/)
        * [ Curve Token V5  ](cryptoswap-exchange/cryptoswap/lp_tokens/lp-token-V5/)
    * Twocrypto-NG  Twocrypto-NG 
      * [ Overview  ](cryptoswap-exchange/twocrypto-ng/overview/)
      * Pools  Pools 
        * [ Overview  ](cryptoswap-exchange/twocrypto-ng/pools/overview/)
        * [ Twocrypto Pool  ](cryptoswap-exchange/twocrypto-ng/pools/twocrypto/)
        * [ Admin Controls  ](cryptoswap-exchange/twocrypto-ng/pools/admin-controls/)
      * Implementations  Implementations 
        * [ Refuels  ](cryptoswap-exchange/twocrypto-ng/implementations/refuel/)
      * Utility Contracts  Utility Contracts 
        * [ Math  ](cryptoswap-exchange/twocrypto-ng/utility-contracts/math/)
        * [ Views  ](cryptoswap-exchange/twocrypto-ng/utility-contracts/views/)
    * Tricrypto-NG  Tricrypto-NG 
      * [ Overview  ](cryptoswap-exchange/tricrypto-ng/overview/)
      * Pools  Pools 
        * [ Tricrypto Pool  ](cryptoswap-exchange/tricrypto-ng/pools/tricrypto/)
        * [ Oracles  ](cryptoswap-exchange/tricrypto-ng/pools/oracles/)
        * [ Admin Controls  ](cryptoswap-exchange/tricrypto-ng/pools/admin-controls/)
      * Utility Contracts  Utility Contracts 
        * [ Math  ](cryptoswap-exchange/tricrypto-ng/utility-contracts/math/)
        * [ Views  ](cryptoswap-exchange/tricrypto-ng/utility-contracts/views/)
  * Pool Factory  Pool Factory 
    * [ Overview  ](factory/overview/)
    * Stableswap-NG  Stableswap-NG 
      * [ Overview  ](factory/stableswap-ng/overview/)
      * [ Deployer API  ](factory/stableswap-ng/deployer-api/)
    * Twocrypto-NG  Twocrypto-NG 
      * [ Overview  ](factory/twocrypto-ng/overview/)
      * [ Deployer API  ](factory/twocrypto-ng/deployer-api/)
    * Tricrypto-NG  Tricrypto-NG 
      * [ Overview  ](factory/tricrypto-ng/overview/)
      * [ Deployer API  ](factory/tricrypto-ng/deployer-api/)
    * Stableswap  Stableswap 
      * [ Overview  ](factory/stableswap/overview/)
      * [ Deployer API  ](factory/stableswap/deployer-api/)
      * [ Implementations  ](factory/stableswap/implementations/)
    * Cryptoswap  Cryptoswap 
      * [ Overview  ](factory/cryptoswap/overview/)
      * [ Deployer API  ](factory/cryptoswap/deployer-api/)
      * [ Implementations  ](factory/cryptoswap/implementations/)
  * Integration & Guides  Integration & Guides 
    * [ Overview  ](integration/overview/)
    * [ Address Provider  ](integration/address-provider/)
    * [ Meta Registry  ](integration/metaregistry/)
    * [ Rate Provider  ](integration/rate-provider/)
  * [ Bug Bounty & Audits  ](security/security/)
  * References  References 
    * [ Whitepapers, Derivations and Useful Resources  ](references/whitepaper/)
    * [ Contract Ownership  ](references/curve-practices/)
    * [ Notebooks  ](references/notebooks/)
  * Deployment Addresses  Deployment Addresses 
    * [ Interactive Deployments  ](deployments/interactive-deployments/)
    * [ Implementations  ](deployments/implementations/)



[ Suggest changes ](https://github.com/CurveDocs/curve-docs/issues/new?title=\[Feature/Change Request\]&body=**Description**%0AProvide a detailed description of the feature or change you would like.%0A%0A**Use Case**%0ADescribe the use case or context for this request.%0A%0A**Additional Information**%0AInclude any other relevant details or references here. "Suggest changes or request new features")

# 

2025-11-04

Back to top 

Made with [ Material for MkDocs Insiders ](https://squidfunk.github.io/mkdocs-material/)
