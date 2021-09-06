>./puppeth

> cliquernet

> 2 #Configure new genesis

> 1 #Create new genesis from scratch

> 2 #Clique - proof-of-authority

> 0xab3BD0f1dc49a323ed0A1d5a982048cd4a866BC2
> 0x

> 2 #Manage existing genesis

$ ./geth account new --datadir node1
#Public address of the key:   0x91630D9D6B6d5CDAb20d186e8d0fBBF5C4FC3444
#Path of the secret key file: node1\keystore\UTC--2021-08-20T22-28-08.011651800Z--91630d9d6b6d5cdab20d186e8d0fbbf5c4fc3444


$ ./geth account new --datadir node2
#Public address of the key:   0x9F2394750DD48377352913Be3b79E544cC62510A
#Path of the secret key file: node2\keystore\UTC--2021-08-20T22-29-22.634667900Z--9f2394750dd48377352913be3b79e544cc62510a

$ ./geth init cliquernet.json --datadir node1
#self=enode://59af06905ebdac7cae301c32a000615b95e0a8019631de311d76655bc495bbb198bb98109ed7e5f4259d123564814687b33dcf77e32d586248fa54ce17e54268@127.0.0.1:30303

$ ./geth --datadir node2 --port 30304 --rpc --bootnode "enode://59af06905ebdac7cae301c32a000615b95e0a8019631de311d76655bc495bbb198bb98109ed7e5f4259d123564814687b33dcf77e32d586248fa54ce17e54268@127.0.0.1:30303" --ipcdisable
#self=enode://3073783a309f0ed93fcc6fbc1575691d601c6e832f5541da5e15d3a6726082e6d998b00ed962af2b6dc9dbd4e2ff30123771c5db9386a7c83b18c49ebc81ed56@127.0.0.1:30304


