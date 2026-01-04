# Simple Blockchain Prototype

This project implements a basic blockchain in Python with block creation, validation, and a Proof-of-Work mechanism.

---

## Block Structure
Each block in the chain contains:
- **Index**: Position of the block in the chain.
- **Nonce**: A number used for Proof-of-Work to satisfy difficulty requirements.
- **Previous Hash**: The SHA-256 hash of the previous block, ensuring linkage.
- **Data**: Transaction records (sender, recipient, quantity).
- **Timestamp**: Time when the block was created.
- **Hash (calculated)**: A SHA-256 digest of the block’s contents, uniquely identifying it.

This structure ensures immutability: any change in block data alters its hash, breaking the chain.

---

## Validation Logic (Tampering Detection)
The blockchain validates blocks using the following rules:
1. **Index Check**: Each block’s index must be exactly one greater than the previous block.
2. **Hash Link Check**: The `prev_hash` stored in the current block must equal the calculated hash of the previous block.
3. **Proof-of-Work Check**: The nonce must satisfy the difficulty rule (`hash starts with "0000"`).
4. **Timestamp Check**: A block’s timestamp must be greater than the previous block’s timestamp.

If any of these conditions fail the blockchain will be corrupted.
