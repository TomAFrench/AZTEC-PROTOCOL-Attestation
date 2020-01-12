from eth_account import Account
from eth_account.messages import encode_defunct

message = 'https://www.aztecprotocol.com/ignition/participant/0xb51da5f6a840098a2b78a381a2a9716ff1f112c1/?timestamp=1578775929139'
hash = '0x09b6524742eab624e8aff260bf168b17d546429a7471ca43f860f7a1a59899d8'
signature = '0x316c44c5db370af3cadde8101c298b6ff3bffb64147295d76446f12d2a623c9f59eec8834fd45c4bb2be950af2b5ea9db2813d1af35036866d3d035a086c844c1b'


success = Account.recover_message(encode_defunct(text=message), signature=signature) == Account.recoverHash(hash, signature=signature)

if success:
  print("Success! Verified Attestation!")
else:
  print("WARNING! Could not verify Attestation!")
