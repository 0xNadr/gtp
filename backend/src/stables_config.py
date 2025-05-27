# Token metadata
# a dictionary of tokens that can be considered stablecoins
# each token has a name, symbol, decimals, coingecko_id, fiat currency, logo and addresses
# the addresses are the contract addresses for the token on the ethereum network

# name: the name is the name of the token
# symbol: the symbol is the ticker symbol of the token
# decimals: the number of decimals the token has
# coingecko_id: the coingecko_id is the id of the token on coingecko
# fiat: the fiat currency is the currency that the token is pegged to
# logo: (optional) the logo is a link to the token's logo 
# addresses: the addresses are the contract addresses for the token on the Ethereum network

#TODO: add logic for non-usd backed stables (should be enough to add the token to the total supply calculation)

stables_metadata = {
    "usdc": {
        "name": "USD Coin",
        "symbol": "USDC",
        "decimals": 6,
        "coingecko_id": "usd-coin",
        "fiat": "usd",
        "logo": "https://assets.coingecko.com/coins/images/6319/large/usdc.png?1696506694",
        "addresses": {
            "ethereum": "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48",
        }
    },
    "tether": {
        "name": "Tether USD",
        "symbol": "USDT",
        "decimals": 6,
        "coingecko_id": "tether",
        "fiat": "usd",
        "logo": "https://coin-images.coingecko.com/coins/images/325/large/Tether.png?1696501661",
        "addresses": {
            "ethereum": "0xdac17f958d2ee523a2206206994597c13d831ec7",
            "celo": "0x48065fbBE25f71C9282ddf5e1cD6D6A887483D5e",
        }
    },
    "dai": {
        "name": "Dai",
        "symbol": "DAI",
        "decimals": 18,
        "coingecko_id": "dai",
        "fiat": "usd",
        "logo": "https://coin-images.coingecko.com/coins/images/9956/large/Badge_Dai.png?1696509996",
        "addresses": {
            "ethereum": "0x6b175474e89094c44da98b954eedeac495271d0f",
        }
    },
    "usds": {
        "name": "USDS (former DAI)",
        "symbol": "USDS",
        "decimals": 18,
        "coingecko_id": "usds",
        "fiat": "usd",
        "logo": "https://coin-images.coingecko.com/coins/images/39926/large/usds.webp?1726666683",
        "addresses": {
            "ethereum": "0xdc035d45d973e3ec169d2276ddab16f1e407384f",
        }
    },
    "ethena-usde": {
        "name": "Ethena USDe",
        "symbol": "USDe",
        "decimals": 18,
        "coingecko_id": "ethena-usde",
        "fiat": "usd",
        "logo": "https://coin-images.coingecko.com/coins/images/33613/large/usde.png?1733810059",
        "addresses": {
            "ethereum": "0x4c9edd5852cd905f086c759e8383e09bff1e68b3",
        }
    },
    "binance_usd": {
        "name": "Binance USD",
        "symbol": "BUSD",
        "decimals": 18,
        "coingecko_id": "binance-usd",
        "fiat": "usd",
        "logo": "https://assets.coingecko.com/coins/images/9576/large/BUSDLOGO.jpg?1696509654",
        "addresses": {
            "ethereum": "0x4fabb145d64652a948d72533023f6e7a623c7c53",
        }
    },
    "true_usd": {
        "name": "TrueUSD",
        "symbol": "TUSD",
        "decimals": 18,
        "coingecko_id": "true-usd",
        "fiat": "usd",
        "logo": "https://assets.coingecko.com/coins/images/3449/large/tusd.png?1696504140",
        "addresses": {
            "ethereum": "0x0000000000085d4780b73119b644ae5ecd22b376",
        }
    },
    "frax": {
        "name": "Frax",
        "symbol": "FRAX",
        "decimals": 18,
        "coingecko_id": "frax",
        "fiat": "usd",
        "logo": "https://assets.coingecko.com/coins/images/13422/large/FRAX_icon.png?1696513182",
        "addresses": {
            "ethereum": "0x853d955acef822db058eb8505911ed77f175b99e",
        }
    },
    "pax-dollar": {
        "name": "Pax Dollar",
        "symbol": "USDP",
        "decimals": 18,
        "coingecko_id": "paxos-standard",
        "fiat": "usd",
        "logo": "https://assets.coingecko.com/coins/images/6013/large/Pax_Dollar.png?1696506427",
        "addresses": {
            "ethereum": "0x8e870d67f660d95d5be530380d0ec0bd388289e1",
        }
    },
    "gemini-usd": {
        "name": "Gemini Dollar",
        "symbol": "GUSD",
        "decimals": 2,
        "coingecko_id": "gemini-dollar",
        "fiat": "usd",
        "logo": "https://assets.coingecko.com/coins/images/5992/large/gemini-dollar-gusd.png?1696506408",
        "addresses": {
            "ethereum": "0x056fd409e1d7a124bd7017459dfea2f387b6d5cd",
        }
    },
    "paypal-usd": {
        "name": "PayPal USD",
        "symbol": "PYUSD",
        "decimals": 18,
        "coingecko_id": "paypal-usd",
        "fiat": "usd",
        "logo": None,
        "addresses": {
            "ethereum": "0x6c3ea9036406852006290770bedfcaba0e23a0e8",
        }
    },
    "liquity-usd": {
        "name": "Liquity USD",
        "symbol": "LUSD",
        "decimals": 18,
        "coingecko_id": "liquity-usd",
        "fiat": "usd",
        "logo": "https://assets.coingecko.com/coins/images/14666/large/Group_3.png?1696514341",
        "addresses": {
            "ethereum": "0x5f98805a4e8be255a32880fdec7f6728c6568ba0",
        }
    },
    "mountain-protocol-usdm": {
        "name": "Mountain Protocol USD",
        "symbol": "USDM",
        "decimals": 18,
        "coingecko_id": "mountain-protocol-usdm",
        "fiat": "usd",
        "logo": "https://coin-images.coingecko.com/coins/images/31719/large/usdm.png?1696530540",
        "addresses": {
            "ethereum": "0x59d9356e565ab3a36dd77763fc0d87feaf85508c",
        }
    },
    "izumi-bond-usd": {
        "name": "iZUMi Bond USD",
        "symbol": "IUSD",
        "decimals": 18,
        "coingecko_id": "izumi-bond-usd",
        "fiat": "usd",
        "logo": "https://assets.coingecko.com/coins/images/25388/large/iusd-logo-symbol-10k%E5%A4%A7%E5%B0%8F.png?1696524521",
        "addresses": {
            "ethereum": "0x0a3bb08b3a15a19b4de82f8acfc862606fb69a2d",
        }
    },
    "electronic-usd": {
        "name": "Electronic USD",
        "symbol": "eUSD",
        "decimals": 18,
        "coingecko_id": "electronic-usd",
        "fiat": "usd",
        "logo": "https://coin-images.coingecko.com/coins/images/28445/large/0xa0d69e286b938e21cbf7e51d71f6a4c8918f482f.png?1696527441",
        "addresses": {
            "ethereum": "0xa0d69e286b938e21cbf7e51d71f6a4c8918f482f",
        }
    },
    "curve-usd": {
        "name": "Curve USD",
        "symbol": "crvUSDC",
        "decimals": 18,
        "coingecko_id": "crvusd",
        "fiat": "usd",
        "logo": "https://coin-images.coingecko.com/coins/images/30118/large/crvusd.jpeg?1696529040",
        "addresses": {
            "ethereum": "0xf939e0a03fb07f59a73314e73794be0e57ac1b4e",
        }
    },
    "dola": {
        "name": "Dola",
        "symbol": "DOLA",
        "decimals": 18,
        "coingecko_id": "dola-usd",
        "fiat": "usd",
        "logo": None,
        "addresses": {
            "ethereum": "0x865377367054516e17014ccded1e7d814edc9ce4",
        }
    },
    "alchemix-usd": {
        "name": "Alchemix USD",
        "symbol": "ALUSD",
        "decimals": 18,
        "coingecko_id": "alchemix-usd",
        "fiat": "usd",
        "logo": "https://assets.coingecko.com/coins/images/14114/large/Alchemix_USD.png?1696513835",
        "addresses": {
            "ethereum": "0xbc6da0fe9ad5f3b0d58160288917aa56653660e9",
        }
    },
    "first-digital-usd": {
        "name": "First Digital USD",
        "symbol": "FDUSD",
        "decimals": 18,
        "coingecko_id": "first-digital-usd",
        "fiat": "usd",
        "logo": None,
        "addresses": {
            "ethereum": "0xc5f0f7b66764f6ec8c8dff7ba683102295e16409",
        }
    },
    "usual-usd": {
        "name": "Usual USD",
        "symbol": "USD0",
        "decimals": 18,
        "coingecko_id": "usual-usd",
        "fiat": "usd",
        "logo": None,
        "addresses": {
            "ethereum": "0x73a15fed60bf67631dc6cd7bc5b6e8da8190acf5",
        }
    },
    "celo-dollar": {
        "name": "Celo Dollar",
        "symbol": "cUSD",
        "decimals": 18,
        "coingecko_id": "celo-dollar",
        "fiat": "usd",
        "logo": None,
        "addresses": {
            "celo": "0x765DE816845861e75A25fCA122bb6898B8B1282a",
        }
    },
    "glo-dollar": {
        "name": "Glo Dollar",
        "symbol": "USDGLO",
        "decimals": 18,
        "coingecko_id": "glo-dollar",
        "fiat": "usd",
        "logo": None,
        "addresses": {
            "ethereum": "0x4f604735c1cf31399c6e711d5962b2b3e0225ad3",
            "celo": "0x4f604735c1cf31399c6e711d5962b2b3e0225ad3"
        }
    },
    "usdx": {
        "name": "Stables Labs USDX",
        "symbol": "USDX",
        "decimals": 18,
        "coingecko_id": "usdx-money-usdx",
        "fiat": "usd",
        "logo": None,
        "addresses": {
            "arbitrum": "0xf3527ef8dE265eAa3716FB312c12847bFBA66Cef",
        }
    },
}


# Layer 2 bridge or direct token mapping
## bridged: locked value is calculated based on bridge contracts on different chains
### Check for any stable that we track if it is locked in here

## direct: token is directly minted on Layer 2
### Call method to get total supply of the token on the chain

## locked_supply: list of tokens that should be subtracted from the total supply
### This is useful for tokens that are locked in contracts of the issuer

stables_mapping = {
    "swell": {
        "bridged": {
            "ethereum": [
                "0x7aA4960908B13D104bf056B23E2C76B43c5AACc8" ##proxy, 0 tokens in it on March 3rd, 2025
            ], 
        },
        "direct": {
            "ethena-usde": {
                "token_address" : "0x5d3a1Ff2b6BAb83b63cd9AD0787074081a52ef34",
                "method_name": "totalSupply",
            },
            "tether": {
                "token_address" : "0xb89c6ED617f5F46175E41551350725A09110bbCE",
                "method_name": "totalSupply",
            }
            ## staked ethena-staked-usde??
        }
    },
    "soneium": {
        "bridged": {
            "ethereum": [
                "0xeb9bf100225c214Efc3E7C651ebbaDcF85177607", ## Generic escrow contract
                "0xC67A8c5f22b40274Ca7C4A56Db89569Ee2AD3FAb" ## Escrow for USDC
            ],
        },
    },
    "base": {},
    "arbitrum": {
        "bridged": {
            "ethereum": [
                "0xa3A7B6F88361F48403514059F1F16C8E78d60EeC", # Arbitrum L1 ERC20 Gateway
                "0xcEe284F754E854890e311e3280b767F80797180d", # Arbitrum: L1 Arb-Custom Gateway
                "0xA10c7CE4b876998858b1a9E12b10092229539400" # DAI Escrow contract
            ],
        },
        "direct": {
            "usdc": {
                "token_address": "0xaf88d065e77c8cC2239327C5EDb3A432268e5831",  # USDC native on Arbitrum
                "method_name": "totalSupply",
            },
            "usdx": {
                "token_address": "0xf3527ef8dE265eAa3716FB312c12847bFBA66Cef",  # USDX native on Arbitrum
                "method_name": "totalSupply",
            },
            "frax": {
                "token_address": "0x17FC002b466eEc40DaE837Fc4bE5c67993ddBd6F",  # FRAX native on Arbitrum
                "method_name": "totalSupply",
            },
            "mountain-protocol-usdm": {
                "token_address": "0x59D9356E565Ab3A36dD77763Fc0d87fEaf85508C",  # USDM native on Arbitrum
                "method_name": "totalSupply",
            },
            "tether": {
                "token_address": "0xFd086bC7CD5C481DCC9C85ebE478A1C0b69FCbb9",  # USDT native on Arbitrum
                "method_name": "totalSupply",
            },
            "ethena-usde": {
                "token_address": "0x5d3a1Ff2b6BAb83b63cd9AD0787074081a52ef34",  # USDe native on Arbitrum
                "method_name": "totalSupply",
            },
        }

    },
    "arbitrum_nova": {
        "bridged": {
            "ethereum": [
                "0xB2535b988dcE19f9D71dfB22dB6da744aCac21bf", # Arbitrum Nova L1 ERC20 Gateway
                "0x23122da8C581AA7E0d07A36Ff1f16F799650232f", # Arbitrum Nova: L1 Arb-Custom Gateway
                "0xA2e996f0cb33575FA0E36e8f62fCd4a9b897aAd3" # DAI Escrow contract
            ], 
        },
    },
    "optimism": {},

    "taiko": {},
    "linea": {},
    "mantle": {},
    "ink": {},
    "zksync_era": {
        "bridged": {
            "ethereum": [
                "0xbeD1EB542f9a5aA6419Ff3deb921A372681111f6",  # Shared brigde with other zkStack chains
                "0x57891966931Eb4Bb6FB81430E6cE0A03AAbDe063",  # Legacy escrow bridge
                "0xD7f9f54194C633F36CCD5F3da84ad4a1c38cB2cB"
            ],
        },
        "direct": {
            "usdc": {
                "token_address": "0x1d17CBcF0D6D143135aE902365D2E5e2A16538D4",  # USDC native on zkSync Era
                "method_name": "totalSupply",
            },
            "mountain-protocol-usdm": {
                "token_address": "0x7715c206A14Ac93Cb1A6c0316A6E5f8aD7c9Dc31",  # USDM
                "method_name": "totalSupply",
            },
        }

    },
    "worldchain": {},
    "manta": {},
    "scroll": {},
    "blast": {},
    "mode": {},
    "real": {},
    "redstone": {},
    "unichain": {
        "bridged": {
            "ethereum": [
                "0x81014F44b0a345033bB2b3B21C7a1A308B35fEeA"  # Bridge contract locking USDT and DAI for Unichain
            ]
        },
        "direct": {
            "usdc": {
                "token_address": "0x078D782b760474a361dDA0AF3839290b0EF57AD6",  # USDC native on Unichain
                "method_name": "totalSupply",
            }
        }
    },
    "lisk": {
        "bridged": {
            "ethereum": [
                "0x2658723Bf70c7667De6B25F99fcce13A16D25d08", # Canonical: Generic escrow (L1StandardBridge) - holds LSK, USDT, WBTC, TRB
                "0xE3622468Ea7dD804702B56ca2a4f88C0936995e6"  # External: Escrow for USDC (L1OpUSDCBridgeAdapter) - holds USDC
            ],
        },
        # LSK is primarily accounted for via its balance in the L1StandardBridge.
        "direct": {},
    },
    "celo": {
        "direct": {
            "tether": {
                "token_address": "0x48065fbBE25f71C9282ddf5e1cD6D6A887483D5e", 
                "method_name": "totalSupply",
            },
            "usdc": {
                "token_address": "0xcebA9300f2b948710d2653dD7B07f33A8B32118C",  
                "method_name": "totalSupply",
            },
            "celo-dollar": {
                "token_address": "0x765DE816845861e75A25fCA122bb6898B8B1282a",  
                "method_name": "totalSupply",
            },
            "glo-dollar": {
                "token_address": "0x4F604735c1cF31399C6E711D5962b2B3E0225AD3",  
                "method_name": "totalSupply",
            }
        },
        "locked_supply": {
            "tether": {
                "celo": [
                    "0x5754284f345afc66a98fbB0a0Afe71e0F007B949"  # Tether Treasury
                ]
            }
        }
    },
    #"gravity": {},
    #"mint": {},
    #"metis": {},
    #"zora": {},
    #"starknet": {},
    #"imx": {},
    #"polygon_zkevm": {},
    #"fraxtal": {},
    #"loopring": {},
    #"orderly": {},
    #"rhino": {},
    #"derive": {},
}

