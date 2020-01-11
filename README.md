This repository is an attestation that I am participant #179 of the AZTEC PROTOCOL Ignition MPC

Ethereum Address: 0xb51da5f6a840098a2b78a381a2a9716ff1f112c1

Transcript Hash: 0x7fcdbe016c23dfc054afd81b330b06dbb70efccb5ceb944258b1a2fb78154b5f

Contribution URL: https://www.aztecprotocol.com/ignition/participant/0xb51da5f6a840098a2b78a381a2a9716ff1f112c1/

# Attestation:

### Message:

https://www.aztecprotocol.com/ignition/participant/0xb51da5f6a840098a2b78a381a2a9716ff1f112c1/?timestamp=1578775929139

### Hash: 

0x09b6524742eab624e8aff260bf168b17d546429a7471ca43f860f7a1a59899d8

### Signature:

0x316c44c5db370af3cadde8101c298b6ff3bffb64147295d76446f12d2a623c9f59eec8834fd45c4bb2be950af2b5ea9db2813d1af35036866d3d035a086c844c1b


# Verification

To verify this attestation (and my ownership of the private key which took place in the MPC) use the python code below.

```python
from eth_account import Account
from eth_account.messages import encode_defunct

message = 'https://www.aztecprotocol.com/ignition/participant/0xb51da5f6a840098a2b78a381a2a9716ff1f112c1/?timestamp=1578775929139'
hash = '0x09b6524742eab624e8aff260bf168b17d546429a7471ca43f860f7a1a59899d8'
signature = '0x316c44c5db370af3cadde8101c298b6ff3bffb64147295d76446f12d2a623c9f59eec8834fd45c4bb2be950af2b5ea9db2813d1af35036866d3d035a086c844c1b'

>>> Account.recover_message(encode_defunct(text=message), signature=signature)
'0xb51da5f6a840098a2b78a381a2a9716ff1f112c1'

>>> Account.recoverHash(hash, signature=signature)
'0xb51da5f6a840098a2b78a381a2a9716ff1f112c1'
```
