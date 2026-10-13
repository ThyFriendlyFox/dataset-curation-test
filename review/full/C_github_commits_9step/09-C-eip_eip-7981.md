# 9. Ethereum EIP: Increase Access List Cost

`C-eip_eip-7981` · [full/C_github_commits_9step](README.md)

Source: <https://github.com/ethereum/EIPs/blob/4fbe53b41d524e98c811503aae1c9d6470af28e8/EIPS/eip-7981.md> · License: CC0-1.0 · 13 commits touching the file; 11 distinct versions

| step | name | words | citations | similarity to final | provenance |
|---|---|---|---|---|---|
| 0 | title | 4 | 0 | 0.00 | source_title |
| 1 | revision_1 | 538 | 0 | 0.25 | commit a18e175964 (2025-07-13) |
| 2 | revision_2 | 921 | 0 | 0.31 | commit 5aea12c20e (2025-09-04) |
| 3 | revision_3 | 921 | 0 | 0.32 | commit 0fdeb4ce5d (2026-01-20) |
| 4 | revision_4 | 621 | 0 | 0.69 | commit 1356811a15 (2026-01-21) |
| 5 | revision_5 | 598 | 0 | 0.72 | commit 87def23e7d (2026-03-27) |
| 6 | revision_6 | 623 | 0 | 0.79 | commit 706296e06b (2026-04-23) |
| 7 | revision_7 | 556 | 0 | 0.91 | commit 71d3353c3f (2026-05-05) |
| 8 | final | 567 | 0 | 1.00 | commit ff38d6d99b (2026-05-07) |

<details><summary><b>Step 0 — title</b> (4 words)</summary>

````text
Increase Access List Cost
````

</details>

<details><summary><b>Step 1 — revision_1</b> (538 words)</summary>

````text
## Abstract

This EIP charges access lists 16 gas per byte for their data footprint, closing a loophole that allows circumventing [EIP-7623](./eip-7623.md) floor pricing.

## Motivation

Access lists can circumvent [EIP-7623](./eip-7623.md) by filling blocks with uncharged data. Each address uses 20 bytes and each storage key uses 32 bytes, but these are not charged for their data footprint. This allows transactions to achieve larger block sizes than intended by combining access lists with calldata.

## Specification

| Parameter                              | Value |
| -------------------------------------- | ----- |
| `ACCESS_LIST_ADDRESS_COST`            | `2400` |
| `ACCESS_LIST_STORAGE_KEY_COST`        | `1900` |
| `ACCESS_LIST_DATA_COST_PER_BYTE`      | `16`   |

Let `access_list_data_bytes = access_list_addresses * 20 + access_list_storage_keys * 32`.

The current formula for access list costs in [EIP-2930](./eip-2930.md) is:

```python
access_list_cost = (
    ACCESS_LIST_ADDRESS_COST * access_list_addresses
    + ACCESS_LIST_STORAGE_KEY_COST * access_list_storage_keys
)
```

The formula for access list costs changes to:

```python
# Standard access list functionality cost
standard_access_list_cost = (
    ACCESS_LIST_ADDRESS_COST * access_list_addresses
    + ACCESS_LIST_STORAGE_KEY_COST * access_list_storage_keys
)

# Additional data cost for access list bytes
access_list_data_cost = ACCESS_LIST_DATA_COST_PER_BYTE * access_list_data_bytes

# Total access list cost
access_list_cost = standard_access_list_cost + access_list_data_cost
```

Transactions pay both the existing [EIP-2930](./eip-2930.md) functionality costs plus 16 gas per byte for data.

## Rationale

Adding 16 gas per byte ensures consistent pricing across all transaction data:

- Address: 2720 gas (2400 + 320)
- Storage key: 2412 gas (1900 + 512)

No threshold mechanism is used. The 16 gas per byte is always applied to maintain simplicity and prevent circumvention.

The additional cost makes EIP-2930 access lists economically irrational for gas optimization, effectively deprecating their use while maintaining compatibility.

### Maximum Block Size Impact

Current pricing with 36M gas limit:

- 1 address + 18,946 storage keys: 2400 + (18,946 × 1900) = 36,000,100 gas (~607 KB)

With data pricing:

- 1 address + 14,924 storage keys: 2720 + (14,924 × 2412) = 36,000,688 gas (~478 KB)

## Backwards Compatibility

This is a backwards incompatible gas repricing that requires a scheduled network upgrade.

Requires updates to gas estimation in wallets and nodes. Normal usage patterns remain largely unaffected.

## Test Cases

### Case 1: Normal Transaction

- Addresses: 5
- Storage keys: 10  
- Old cost: 5 × 2400 + 10 × 1900 = 31,000 gas
- New cost: 5 × 2720 + 10 × 2412 = 37,720 gas
- Additional cost: 6,720 gas (21.7% increase)

### Case 2: Large Access List Transaction

- Addresses: 1000
- Storage keys: 0
- Old cost: 1000 × 2400 = 2,400,000 gas
- New cost: 1000 × 2720 = 2,720,000 gas  
- Additional cost: 320,000 gas (13.3% increase)

### Case 3: Combined Access List + Calldata

- Addresses: 500
- Calldata: 5,000 bytes
- Old access list cost: 500 × 2400 = 1,200,000 gas
- Old calldata cost: 5,000 × 4 = 20,000 gas (standard rate, avoiding floor)
- New access list cost: 500 × 2720 = 1,360,000 gas
- New calldata cost: Applied through [EIP-7623](./eip-7623.md) mechanism
- Result: Can no longer circumvent [EIP-7623](./eip-7623.md) floor pricing

## Security Considerations

Reduces maximum block size from access lists, improving network stability. The additional cost is proportional to data usage while maintaining access list utility for backwards compatibility.

## Copyright

Copyright and related rights waived via [CC0](../LICENSE.md).
````

</details>

<details><summary><b>Step 2 — revision_2</b> (921 words)</summary>

````text
## Abstract

This EIP charges access lists for their data footprint, closing a loophole that allows circumventing [EIP-7623](./eip-7623.md) floor pricing. This effectively reduces the worst-case block size by ~21% with minimal impact on users.

## Motivation

Access lists are only priced for storage but not for their data.

Furthermore, access lists can circumvent the [EIP-7623](./eip-7623.md) floor pricing by contributing to EVM gas while still leaving a non-negligible data footprint. This enables to achieve the maximal possible block size by combining access lists with calldata at a certain ratio.

## Specification

| Parameter                              | Value | Source |
| -------------------------------------- | ----- | ------ |
| `ACCESS_LIST_ADDRESS_COST`            | `2400` | [EIP-2930](./eip-2930.md) |
| `ACCESS_LIST_STORAGE_KEY_COST`        | `1900` | [EIP-2930](./eip-2930.md) |
| `TOTAL_COST_FLOOR_PER_TOKEN`          | `10`   | [EIP-7623](./eip-7623.md) |

Let `access_list_nonzero_bytes` and `access_list_zero_bytes` be the count of non-zero and zero bytes respectively in the addresses (20 bytes each) and storage keys (32 bytes each) contained within the access list.

The current formula for access list costs in [EIP-2930](./eip-2930.md) is:

```python
access_list_cost = (
    ACCESS_LIST_ADDRESS_COST * access_list_addresses
    + ACCESS_LIST_STORAGE_KEY_COST * access_list_storage_keys
)
```

The formula for access list costs changes to:

```python
# Standard access list functionality cost
standard_access_list_cost = (
    ACCESS_LIST_ADDRESS_COST * access_list_addresses
    + ACCESS_LIST_STORAGE_KEY_COST * access_list_storage_keys
)

# Additional data cost for access list bytes
access_list_tokens = access_list_nonzero_bytes * 4 + access_list_zero_bytes
access_list_data_cost = access_list_tokens * TOTAL_COST_FLOOR_PER_TOKEN

# Total access list cost
access_list_cost = standard_access_list_cost + access_list_data_cost
```

Transactions pay both the existing [EIP-2930](./eip-2930.md) functionality costs plus 40 gas per non-zero byte and 10 gas per zero byte counted across all addresses and storage keys in the access list.

## Rationale

Adding 40 gas per non-zero byte and 10 gas per zero byte ensures consistent pricing across all transaction data:

- Address (20 bytes, typically mostly non-zero): ~3200 gas (2400 + 800 assuming all non-zero)
- Storage key (32 bytes, typically mostly non-zero): ~3180 gas (1900 + 1280 assuming all non-zero)

No threshold mechanism is used. The per-byte costs are always applied to maintain simplicity and prevent circumvention.

The additional cost makes [EIP-2930](./eip-2930.md) access lists economically irrational for gas optimization, effectively deprecating their use while maintaining compatibility.

### Access List Size Impact

At a gas limit of 60M:

- 1 address + 31,578 storage keys: 2400 + (31,578 × 1900) = 59,998,200 gas (~1,012 KB)

With data pricing (assuming all non-zero bytes):

- 1 address + 18,866 storage keys: 3200 + (18,866 × 3180) = 59,998,280 gas (~604 KB)

### Maximum Block Size Impact

The maximum possible Snappy compressed block size can be achieved by using access lists and calldata together at a ratio were the transaction keeps paying the lower calldata price.

At a gas limit of 60M, the maximum possible compressed block size will be reduced from 2.71 MiB to 2.13 MiB.

## Backwards Compatibility

This is a backwards incompatible gas repricing that requires a scheduled network upgrade.

Requires updates to gas estimation in wallets and nodes. Normal usage patterns remain largely unaffected.

## Test Cases

### Case 1: Normal Transaction

- Addresses: 5 (100 bytes, assume all non-zero)
- Storage keys: 10 (320 bytes, assume all non-zero)
- Old cost: 5 × 2400 + 10 × 1900 = 31,000 gas
- New cost: 5 × 3200 + 10 × 3180 = 47,800 gas
- Additional cost: 16,800 gas (54.2% increase)

### Case 2: Large Access List Transaction

- Addresses: 1000 (20,000 bytes, assume all non-zero)
- Storage keys: 0
- Old cost: 1000 × 2400 = 2,400,000 gas
- New cost: 1000 × 3200 = 3,200,000 gas  
- Additional cost: 800,000 gas (33.3% increase)

### Case 3: Combined Access List + Calldata

- Addresses: 500 (10,000 bytes, assume all non-zero)
- Calldata: 5,000 bytes
- Old access list cost: 500 × 2400 = 1,200,000 gas
- Old calldata cost: 5,000 × 4 = 20,000 gas (standard rate, avoiding floor)
- New access list cost: 500 × 3200 = 1,600,000 gas
- New calldata cost: Applied through [EIP-7623](./eip-7623.md) mechanism
- Result: Can no longer circumvent [EIP-7623](./eip-7623.md) floor pricing

## Reference Implementation

The following is the EELS (Ethereum Execution Layer Specification) implementation:

```python
TX_ACCESS_LIST_NONZERO_BYTE_COST = Uint(40)
TX_ACCESS_LIST_ZERO_BYTE_COST = Uint(10)

def count_access_list_bytes(access_list: Tuple[Access, ...]) -> Tuple[int, int]:
    """
    Count zero and non-zero bytes in access list addresses and storage keys.
    
    Returns a tuple of (zero_bytes, nonzero_bytes).
    """
    zero_bytes = 0
    nonzero_bytes = 0
    
    for access in access_list:
        # Count bytes in address (20 bytes)
        for byte in access.account:
            if byte == 0:
                zero_bytes += 1
            else:
                nonzero_bytes += 1
        
        # Count bytes in storage keys (32 bytes each)
        for slot in access.slots:
            for byte in slot:
                if byte == 0:
                    zero_bytes += 1
                else:
                    nonzero_bytes += 1
    
    return zero_bytes, nonzero_bytes

def calculate_intrinsic_cost(tx: Transaction) -> Tuple[Uint, Uint]:
    """
    Calculates the gas that is charged before execution is started.
    """
    # ... existing calldata and base cost calculations ...
    
    access_list_cost = Uint(0)
    access_list_data_cost = Uint(0)
    
    if isinstance(tx, (AccessListTransaction, FeeMarketTransaction, 
                      BlobTransaction, SetCodeTransaction)):
        # Standard EIP-2930 access list functionality costs
        for access in tx.access_list:
            access_list_cost += TX_ACCESS_LIST_ADDRESS_COST
            access_list_cost += (
                ulen(access.slots) * TX_ACCESS_LIST_STORAGE_KEY_COST
            )
        
        # EIP-7981: Additional data cost for access list bytes
        zero_bytes, nonzero_bytes = count_access_list_bytes(tx.access_list)
        access_list_data_cost = (
            Uint(zero_bytes) * TX_ACCESS_LIST_ZERO_BYTE_COST +
            Uint(nonzero_bytes) * TX_ACCESS_LIST_NONZERO_BYTE_COST
        )
    
    return (
        Uint(
            TX_BASE_COST
            + data_cost
            + create_cost
            + access_list_cost
            + access_list_data_cost  # Added by EIP-7981
            + auth_cost
        ),
        calldata_floor_gas_cost,
    )
```

## Security Considerations

Reduces maximum block size from access lists, improving network stability. The additional cost is proportional to data usage while maintaining access list utility for backwards compatibility.

## Copyright

Copyright and related rights waived via [CC0](../LICENSE.md).
````

</details>

<details><summary><b>Step 3 — revision_3</b> (921 words)</summary>

````text
## Abstract

This EIP charges access lists for their data footprint, preventing the circumvention of the [EIP-7623](./eip-7623.md) floor pricing. This effectively reduces the worst-case block size by ~21% with minimal impact on users.

## Motivation

Access lists are only priced for storage but not for their data.

Furthermore, access lists can circumvent the [EIP-7976](./eip-7976.md) floor pricing by contributing to EVM gas while still leaving a non-negligible data footprint. This enables to achieve the maximal possible block size by combining access lists with calldata at a certain ratio.

## Specification

| Parameter                              | Value | Source |
| -------------------------------------- | ----- | ------ |
| `ACCESS_LIST_ADDRESS_COST`            | `2400` | [EIP-2930](./eip-2930.md) |
| `ACCESS_LIST_STORAGE_KEY_COST`        | `1900` | [EIP-2930](./eip-2930.md) |
| `TOTAL_COST_FLOOR_PER_TOKEN`          | `15`   | [EIP-7976](./eip-7976.md) |

Let `access_list_nonzero_bytes` and `access_list_zero_bytes` be the count of non-zero and zero bytes respectively in the addresses (20 bytes each) and storage keys (32 bytes each) contained within the access list.

The current formula for access list costs in [EIP-2930](./eip-2930.md) is:

```python
access_list_cost = (
    ACCESS_LIST_ADDRESS_COST * access_list_addresses
    + ACCESS_LIST_STORAGE_KEY_COST * access_list_storage_keys
)
```

The formula for access list costs changes to:

```python
# Standard access list functionality cost
standard_access_list_cost = (
    ACCESS_LIST_ADDRESS_COST * access_list_addresses
    + ACCESS_LIST_STORAGE_KEY_COST * access_list_storage_keys
)

# Additional data cost for access list bytes
access_list_tokens = access_list_nonzero_bytes * 4 + access_list_zero_bytes
access_list_data_cost = access_list_tokens * TOTAL_COST_FLOOR_PER_TOKEN

# Total access list cost
access_list_cost = standard_access_list_cost + access_list_data_cost
```

Transactions pay both the existing [EIP-2930](./eip-2930.md) functionality costs plus 60 gas per non-zero byte and 15 gas per zero byte counted across all addresses and storage keys in the access list.

## Rationale

Adding 60 gas per non-zero byte and 15 gas per zero byte ensures consistent pricing across all transaction data:

- Address (20 bytes, typically mostly non-zero): ~3600 gas (2400 + 1200 assuming all non-zero)
- Storage key (32 bytes, typically mostly non-zero): ~3820 gas (1900 + 1920 assuming all non-zero)

No threshold mechanism is used. The per-byte costs are always applied to maintain simplicity and prevent circumvention.

The additional cost makes [EIP-2930](./eip-2930.md) access lists economically irrational for gas optimization, effectively deprecating their use while maintaining compatibility.

### Access List Size Impact

At a gas limit of 60M:

- 1 address + 31,578 storage keys: 2400 + (31,578 × 1900) = 59,998,200 gas (~1,012 KB)

With data pricing (assuming all non-zero bytes):

- 1 address + 15,705 storage keys: 3600 + (15,705 × 3820) = 59,996,700 gas (~491 KB)

### Maximum Block Size Impact

The maximum possible Snappy compressed block size can be achieved by using access lists and calldata together at a ratio where the transaction keeps paying the lower calldata price.

At a gas limit of 60M, the maximum possible compressed block size will be reduced from 2.71 MiB to approximately 1.7 MiB.

## Backwards Compatibility

This is a backwards incompatible gas repricing that requires a scheduled network upgrade.

Requires updates to gas estimation in wallets and nodes. Normal usage patterns remain largely unaffected.

## Test Cases

### Case 1: Normal Transaction

- Addresses: 5 (100 bytes, assume all non-zero)
- Storage keys: 10 (320 bytes, assume all non-zero)
- Old cost: 5 × 2400 + 10 × 1900 = 31,000 gas
- New cost: 5 × 3600 + 10 × 3820 = 56,200 gas
- Additional cost: 25,200 gas (81.3% increase)

### Case 2: Large Access List Transaction

- Addresses: 1000 (20,000 bytes, assume all non-zero)
- Storage keys: 0
- Old cost: 1000 × 2400 = 2,400,000 gas
- New cost: 1000 × 3600 = 3,600,000 gas
- Additional cost: 1,200,000 gas (50% increase)

### Case 3: Combined Access List + Calldata

- Addresses: 500 (10,000 bytes, assume all non-zero)
- Calldata: 5,000 bytes
- Old access list cost: 500 × 2400 = 1,200,000 gas
- Old calldata cost: 5,000 × 4 = 20,000 gas (standard rate, avoiding floor)
- New access list cost: 500 × 3600 = 1,800,000 gas
- New calldata cost: Applied through [EIP-7976](./eip-7976.md) mechanism
- Result: Can no longer circumvent [EIP-7976](./eip-7976.md) floor pricing

## Reference Implementation

The following is the EELS (Ethereum Execution Layer Specification) implementation:

```python
TX_ACCESS_LIST_NONZERO_BYTE_COST = Uint(60)
TX_ACCESS_LIST_ZERO_BYTE_COST = Uint(15)

def count_access_list_bytes(access_list: Tuple[Access, ...]) -> Tuple[int, int]:
    """
    Count zero and non-zero bytes in access list addresses and storage keys.
    
    Returns a tuple of (zero_bytes, nonzero_bytes).
    """
    zero_bytes = 0
    nonzero_bytes = 0
    
    for access in access_list:
        # Count bytes in address (20 bytes)
        for byte in access.account:
            if byte == 0:
                zero_bytes += 1
            else:
                nonzero_bytes += 1
        
        # Count bytes in storage keys (32 bytes each)
        for slot in access.slots:
            for byte in slot:
                if byte == 0:
                    zero_bytes += 1
                else:
                    nonzero_bytes += 1
    
    return zero_bytes, nonzero_bytes

def calculate_intrinsic_cost(tx: Transaction) -> Tuple[Uint, Uint]:
    """
    Calculates the gas that is charged before execution is started.
    """
    # ... existing calldata and base cost calculations ...
    
    access_list_cost = Uint(0)
    access_list_data_cost = Uint(0)
    
    if isinstance(tx, (AccessListTransaction, FeeMarketTransaction, 
                      BlobTransaction, SetCodeTransaction)):
        # Standard EIP-2930 access list functionality costs
        for access in tx.access_list:
            access_list_cost += TX_ACCESS_LIST_ADDRESS_COST
            access_list_cost += (
                ulen(access.slots) * TX_ACCESS_LIST_STORAGE_KEY_COST
            )
        
        # EIP-7981: Additional data cost for access list bytes
        zero_bytes, nonzero_bytes = count_access_list_bytes(tx.access_list)
        access_list_data_cost = (
            Uint(zero_bytes) * TX_ACCESS_LIST_ZERO_BYTE_COST +
            Uint(nonzero_bytes) * TX_ACCESS_LIST_NONZERO_BYTE_COST
        )
    
    return (
        Uint(
            TX_BASE_COST
            + data_cost
            + create_cost
            + access_list_cost
            + access_list_data_cost  # Added by EIP-7981
            + auth_cost
        ),
        calldata_floor_gas_cost,
    )
```

## Security Considerations

Reduces maximum block size from access lists, improving network stability. The additional cost is proportional to data usage while maintaining access list utility for backwards compatibility.

## Copyright

Copyright and related rights waived via [CC0](../LICENSE.md).
````

</details>

<details><summary><b>Step 4 — revision_4</b> (621 words)</summary>

````text
## Abstract

This EIP charges access lists for their data footprint, preventing the circumvention of the [EIP-7623](./eip-7623.md) floor pricing. This effectively reduces the worst-case block size by ~21% with minimal impact on users.

## Motivation

Access lists are only priced for storage but not for their data.

Furthermore, access lists can circumvent the [EIP-7623](./eip-7623.md) floor pricing by contributing to EVM gas while still leaving a non-negligible data footprint. This enables achieving the maximal possible block size by combining access lists with calldata at a certain ratio.

## Specification

| Parameter                              | Value | Source |
| -------------------------------------- | ----- | ------ |
| `ACCESS_LIST_ADDRESS_COST`            | `2400` | [EIP-2930](./eip-2930.md) |
| `ACCESS_LIST_STORAGE_KEY_COST`        | `1900` | [EIP-2930](./eip-2930.md) |
| `TOTAL_COST_FLOOR_PER_TOKEN`          | `10`   | [EIP-7623](./eip-7623.md) |

Let `access_list_nonzero_bytes` and `access_list_zero_bytes` be the count of non-zero and zero bytes respectively in the addresses (20 bytes each) and storage keys (32 bytes each) contained within the access list.

Let `tokens_in_access_list = access_list_zero_bytes + access_list_nonzero_bytes * 4`.

The access list cost formula changes from [EIP-2930](./eip-2930.md) to include data cost:

```python
access_list_cost = (
    ACCESS_LIST_ADDRESS_COST * access_list_addresses
    + ACCESS_LIST_STORAGE_KEY_COST * access_list_storage_keys
    + TOTAL_COST_FLOOR_PER_TOKEN * tokens_in_access_list
)
```

The [EIP-7623](./eip-7623.md) floor calculation is modified to include access list tokens:

```python
tokens_in_calldata = zero_bytes_in_calldata + nonzero_bytes_in_calldata * 4
total_data_tokens = tokens_in_calldata + tokens_in_access_list

data_floor_gas_cost = TX_BASE_COST + TOTAL_COST_FLOOR_PER_TOKEN * total_data_tokens
```

The gas used calculation becomes:

```python
tx.gasUsed = (
    21000
    +
    max(
        STANDARD_TOKEN_COST * tokens_in_calldata
        + execution_gas_used
        + isContractCreation * (32000 + INITCODE_WORD_COST * words(calldata))
        + access_list_cost,
        TOTAL_COST_FLOOR_PER_TOKEN * total_data_tokens
    )
)
```

Any transaction with a gas limit below `21000 + TOTAL_COST_FLOOR_PER_TOKEN * total_data_tokens` or below its intrinsic gas cost is considered invalid.

## Rationale

Access list data is always charged at floor rate (added to `access_list_cost`), and access list tokens are included in the floor calculation. This ensures:

- Access list data always pays floor rate regardless of execution level
- Access lists cannot be used to bypass the calldata floor pricing
- Consistent pricing across all transaction data sources

## Backwards Compatibility

This is a backwards incompatible gas repricing that requires a scheduled network upgrade.

Requires updates to gas estimation in wallets and nodes. Normal usage patterns remain largely unaffected.

## Reference Implementation

```python
def calculate_access_list_tokens(access_list: Tuple[Access, ...]) -> Uint:
    """Count data tokens in access list addresses and storage keys."""
    zero_bytes = Uint(0)
    nonzero_bytes = Uint(0)

    for access in access_list:
        for byte in access.account:
            if byte == 0:
                zero_bytes += Uint(1)
            else:
                nonzero_bytes += Uint(1)
        for slot in access.slots:
            for byte in slot:
                if byte == 0:
                    zero_bytes += Uint(1)
                else:
                    nonzero_bytes += Uint(1)

    return zero_bytes + nonzero_bytes * Uint(4)

def calculate_intrinsic_cost(tx: Transaction) -> Tuple[Uint, Uint]:
    """
    Calculate intrinsic gas cost and floor gas cost.
    Returns (intrinsic_gas, floor_gas).
    """
    # Calldata tokens
    calldata_zero_bytes = Uint(0)
    for byte in tx.data:
        if byte == 0:
            calldata_zero_bytes += Uint(1)
    tokens_in_calldata = (
        calldata_zero_bytes + (ulen(tx.data) - calldata_zero_bytes) * Uint(4)
    )

    # Access list tokens and cost
    tokens_in_access_list = Uint(0)
    access_list_cost = Uint(0)
    if has_access_list(tx):
        tokens_in_access_list = calculate_access_list_tokens(tx.access_list)
        for access in tx.access_list:
            access_list_cost += TX_ACCESS_LIST_ADDRESS_COST
            access_list_cost += ulen(access.slots) * TX_ACCESS_LIST_STORAGE_KEY_COST
        # EIP-7981: Always charge data cost
        access_list_cost += tokens_in_access_list * TOTAL_COST_FLOOR_PER_TOKEN

    # EIP-7981: Floor includes all data tokens
    total_data_tokens = tokens_in_calldata + tokens_in_access_list
    floor_gas = TX_BASE_COST + total_data_tokens * TOTAL_COST_FLOOR_PER_TOKEN

    # Intrinsic gas
    calldata_cost = tokens_in_calldata * STANDARD_TOKEN_COST
    create_cost = TX_CREATE_COST + init_code_cost(tx.data) if is_create(tx) else Uint(0)

    intrinsic_gas = TX_BASE_COST + calldata_cost + create_cost + access_list_cost

    return intrinsic_gas, floor_gas
```

## Security Considerations

This EIP closes a loophole that allows circumventing [EIP-7623](./eip-7623.md) floor pricing. Without this fix, attackers can achieve larger blocks than intended by combining access lists with calldata. All transaction data sources now contribute to the floor calculation consistently.

## Copyright

Copyright and related rights waived via [CC0](../LICENSE.md).
````

</details>

<details><summary><b>Step 5 — revision_5</b> (598 words)</summary>

````text
## Abstract

This EIP charges access lists for their data footprint, preventing the circumvention of the [EIP-7623](./eip-7623.md) floor pricing. This effectively reduces the worst-case block size by ~21% with minimal impact on users.

## Motivation

Access lists are only priced for storage but not for their data.

Furthermore, access lists can circumvent the [EIP-7623](./eip-7623.md) floor pricing by contributing to EVM gas while still leaving a non-negligible data footprint. This enables achieving the maximal possible block size by combining access lists with calldata at a certain ratio.

## Specification

| Parameter                              | Value | Source |
| -------------------------------------- | ----- | ------ |
| `ACCESS_LIST_ADDRESS_COST`            | `2400` | [EIP-2930](./eip-2930.md) |
| `ACCESS_LIST_STORAGE_KEY_COST`        | `1900` | [EIP-2930](./eip-2930.md) |
| `TOTAL_COST_FLOOR_PER_TOKEN`          | `16`   | [EIP-7976](./eip-7976.md) |

Let `access_list_bytes` be the total byte count of addresses (20 bytes each) and storage keys (32 bytes each) in the access list.

Let `floor_tokens_in_access_list = access_list_bytes * 4`.

The access list cost formula changes from [EIP-2930](./eip-2930.md) to include data cost:

```python
access_list_cost = (
    ACCESS_LIST_ADDRESS_COST * access_list_addresses
    + ACCESS_LIST_STORAGE_KEY_COST * access_list_storage_keys
    + TOTAL_COST_FLOOR_PER_TOKEN * floor_tokens_in_access_list
)
```

The [EIP-7976](./eip-7976.md) floor calculation is modified to include access list tokens:

```python
floor_tokens_in_calldata = (zero_bytes_in_calldata + nonzero_bytes_in_calldata) * 4
total_floor_data_tokens = floor_tokens_in_calldata + floor_tokens_in_access_list

data_floor_gas_cost = TX_BASE_COST + TOTAL_COST_FLOOR_PER_TOKEN * total_floor_data_tokens
```

The gas used calculation becomes:

```python
tx.gasUsed = (
    21000
    +
    max(
        STANDARD_TOKEN_COST * tokens_in_calldata
        + execution_gas_used
        + isContractCreation * (32000 + INITCODE_WORD_COST * words(calldata))
        + access_list_cost,
        TOTAL_COST_FLOOR_PER_TOKEN * total_floor_data_tokens
    )
)
```

Any transaction with a gas limit below `21000 + TOTAL_COST_FLOOR_PER_TOKEN * total_floor_data_tokens` or below its intrinsic gas cost is considered invalid.

## Rationale

Access list data is always charged at floor rate (added to `access_list_cost`), and access list tokens are included in the floor calculation. This ensures:

- Access list data always pays floor rate regardless of execution level
- Access lists cannot be used to bypass the calldata floor pricing
- Consistent pricing across all transaction data sources

## Backwards Compatibility

This is a backwards incompatible gas repricing that requires a scheduled network upgrade.

Requires updates to gas estimation in wallets and nodes. Normal usage patterns remain largely unaffected.

## Reference Implementation

```python
def calculate_access_list_floor_tokens(access_list: Tuple[Access, ...]) -> Uint:
    """Count floor data tokens in access list addresses and storage keys."""
    total_bytes = Uint(0)

    for access in access_list:
        total_bytes += ulen(access.account)
        for slot in access.slots:
            total_bytes += ulen(slot)

    return total_bytes * Uint(4)

def calculate_intrinsic_cost(tx: Transaction) -> Tuple[Uint, Uint]:
    """
    Calculate intrinsic gas cost and floor gas cost.
    Returns (intrinsic_gas, floor_gas).
    """
    # Calldata tokens (EIP-7976)
    calldata_zero_bytes = Uint(0)
    for byte in tx.data:
        if byte == 0:
            calldata_zero_bytes += Uint(1)
    calldata_nonzero_bytes = ulen(tx.data) - calldata_zero_bytes
    tokens_in_calldata = (
        calldata_zero_bytes + calldata_nonzero_bytes * Uint(4)
    )
    floor_tokens_in_calldata = (
        (calldata_zero_bytes + calldata_nonzero_bytes) * Uint(4)
    )

    # Access list floor tokens and cost
    floor_tokens_in_access_list = Uint(0)
    access_list_cost = Uint(0)
    if has_access_list(tx):
        floor_tokens_in_access_list = calculate_access_list_floor_tokens(tx.access_list)
        for access in tx.access_list:
            access_list_cost += TX_ACCESS_LIST_ADDRESS_COST
            access_list_cost += ulen(access.slots) * TX_ACCESS_LIST_STORAGE_KEY_COST
        # EIP-7981: Always charge data cost
        access_list_cost += floor_tokens_in_access_list * TOTAL_COST_FLOOR_PER_TOKEN

    # EIP-7981: Floor includes all floor data tokens
    total_floor_data_tokens = floor_tokens_in_calldata + floor_tokens_in_access_list
    floor_gas = TX_BASE_COST + total_floor_data_tokens * TOTAL_COST_FLOOR_PER_TOKEN

    # Intrinsic gas
    calldata_cost = tokens_in_calldata * STANDARD_TOKEN_COST
    create_cost = TX_CREATE_COST + init_code_cost(tx.data) if is_create(tx) else Uint(0)

    intrinsic_gas = TX_BASE_COST + calldata_cost + create_cost + access_list_cost

    return intrinsic_gas, floor_gas
```

## Security Considerations

This EIP closes a loophole that allows circumventing [EIP-7623](./eip-7623.md) floor pricing. Without this fix, attackers can achieve larger blocks than intended by combining access lists with calldata. All transaction data sources now contribute to the floor calculation consistently.

## Copyright

Copyright and related rights waived via [CC0](../LICENSE.md).
````

</details>

<details><summary><b>Step 6 — revision_6</b> (623 words)</summary>

````text
## Abstract

This EIP charges access lists for their data footprint, preventing the circumvention of the [EIP-7623](./eip-7623.md) floor pricing. This effectively reduces the worst-case block size by ~21% with minimal impact on users.

## Motivation

Access lists are only priced for storage but not for their data.

Furthermore, access lists can circumvent the [EIP-7623](./eip-7623.md) floor pricing by contributing to EVM gas while still leaving a non-negligible data footprint. This enables achieving the maximal possible block size by combining access lists with calldata at a certain ratio.

## Specification

| Parameter                              | Value | Source |
| -------------------------------------- | ----- | ------ |
| `ACCESS_LIST_ADDRESS_COST`            | `2400` | [EIP-2930](./eip-2930.md) |
| `ACCESS_LIST_STORAGE_KEY_COST`        | `1900` | [EIP-2930](./eip-2930.md) |
| `TOTAL_COST_FLOOR_PER_TOKEN`          | `16`   | [EIP-7976](./eip-7976.md) |

Let `access_list_bytes` be the total byte count of addresses (20 bytes each) and storage keys (32 bytes each) in the access list.

Let `floor_tokens_in_access_list = access_list_bytes * 4`.

Equivalently, the access list data is charged `64` gas per byte, which amounts to `1280` gas per address (20 bytes × 64) and `2048` gas per storage key (32 bytes × 64). The token abstraction is retained only for consistency with [EIP-7623](./eip-7623.md) and [EIP-7976](./eip-7976.md).

The access list cost formula changes from [EIP-2930](./eip-2930.md) to include data cost:

```python
access_list_cost = (
    ACCESS_LIST_ADDRESS_COST * access_list_addresses
    + ACCESS_LIST_STORAGE_KEY_COST * access_list_storage_keys
    + TOTAL_COST_FLOOR_PER_TOKEN * floor_tokens_in_access_list
)
```

The [EIP-7976](./eip-7976.md) floor calculation is modified to include access list tokens:

```python
floor_tokens_in_calldata = (zero_bytes_in_calldata + nonzero_bytes_in_calldata) * 4
total_floor_data_tokens = floor_tokens_in_calldata + floor_tokens_in_access_list

data_floor_gas_cost = TX_BASE_COST + TOTAL_COST_FLOOR_PER_TOKEN * total_floor_data_tokens
```

The gas used calculation becomes:

```python
tx.gasUsed = (
    21000
    +
    max(
        STANDARD_TOKEN_COST * tokens_in_calldata
        + execution_gas_used
        + isContractCreation * (32000 + INITCODE_WORD_COST * words(calldata))
        + access_list_cost,
        TOTAL_COST_FLOOR_PER_TOKEN * total_floor_data_tokens
    )
)
```

Any transaction with a gas limit below `21000 + TOTAL_COST_FLOOR_PER_TOKEN * total_floor_data_tokens` or below its intrinsic gas cost is considered invalid.

## Rationale

Access list data is always charged at floor rate (added to `access_list_cost`), and access list tokens are included in the floor calculation. This ensures:

- Access list data always pays floor rate regardless of execution level
- Access lists cannot be used to bypass the calldata floor pricing
- Consistent pricing across all transaction data sources

## Backwards Compatibility

This is a backwards incompatible gas repricing that requires a scheduled network upgrade.

Requires updates to gas estimation in wallets and nodes. Normal usage patterns remain largely unaffected.

## Reference Implementation

```python
def calculate_access_list_floor_tokens(access_list):
    """Count floor data tokens (4 per byte) in access list."""
    # Each access entry: 20-byte address + 32 bytes per storage key
    total_bytes = sum(20 + 32 * len(access.slots) for access in access_list)
    return total_bytes * 4

def calculate_intrinsic_cost(tx):
    """
    Calculate intrinsic gas cost and floor gas cost.
    Returns (intrinsic_gas, floor_gas).
    """
    # Calldata tokens (EIP-7976)
    zero_bytes = count_zero_bytes(tx.data)
    nonzero_bytes = len(tx.data) - zero_bytes
    tokens_in_calldata = zero_bytes + nonzero_bytes * 4
    floor_tokens_in_calldata = len(tx.data) * 4

    # Access list floor tokens and cost
    floor_tokens_in_access_list = 0
    access_list_cost = 0
    if has_access_list(tx):
        floor_tokens_in_access_list = calculate_access_list_floor_tokens(tx.access_list)
        for access in tx.access_list:
            access_list_cost += (
                ACCESS_LIST_ADDRESS_COST
                + len(access.slots) * ACCESS_LIST_STORAGE_KEY_COST
            )
        # EIP-7981: Always charge data cost
        access_list_cost += floor_tokens_in_access_list * TOTAL_COST_FLOOR_PER_TOKEN

    # EIP-7981: Floor includes all floor data tokens
    total_floor_data_tokens = floor_tokens_in_calldata + floor_tokens_in_access_list
    floor_gas = TX_BASE_COST + total_floor_data_tokens * TOTAL_COST_FLOOR_PER_TOKEN

    # Intrinsic gas
    calldata_cost = tokens_in_calldata * STANDARD_TOKEN_COST
    create_cost = TX_CREATE_COST + init_code_cost(tx.data) if is_create(tx) else 0
    intrinsic_gas = TX_BASE_COST + calldata_cost + create_cost + access_list_cost

    return intrinsic_gas, floor_gas
```

## Security Considerations

This EIP closes a loophole that allows circumventing [EIP-7623](./eip-7623.md) floor pricing. Without this fix, attackers can achieve larger blocks than intended by combining access lists with calldata. All transaction data sources now contribute to the floor calculation consistently.

## Copyright

Copyright and related rights waived via [CC0](../LICENSE.md).
````

</details>

<details><summary><b>Step 7 — revision_7</b> (556 words)</summary>

````text
## Abstract

This EIP charges access lists for their data footprint, preventing the circumvention of the [EIP-7623](./eip-7623.md) floor pricing. This effectively reduces the worst-case block size by ~21% with minimal impact on users.

## Motivation

Access lists are only priced for storage but not for their data.

Furthermore, access lists can circumvent the [EIP-7623](./eip-7623.md) floor pricing by contributing to EVM gas while still leaving a non-negligible data footprint. This enables achieving the maximal possible block size by combining access lists with calldata at a certain ratio.

## Specification

| Parameter                              | Value | Source |
| -------------------------------------- | ----- | ------ |
| `ACCESS_LIST_ADDRESS_COST`            | `2400` | [EIP-2930](./eip-2930.md) |
| `ACCESS_LIST_STORAGE_KEY_COST`        | `1900` | [EIP-2930](./eip-2930.md) |
| `TOTAL_COST_FLOOR_PER_TOKEN`          | `16`   | [EIP-7976](./eip-7976.md) |

Let `access_list_bytes` be the total byte count of addresses (20 bytes each) and storage keys (32 bytes each) in the access list.

Let `access_list_data_cost = 64 * access_list_bytes` (i.e. `1280` gas per address and `2048` gas per storage key). The `64` gas-per-byte rate matches the [EIP-7976](./eip-7976.md) calldata floor.

The access list data cost is added as a flat surcharge to the gas used calculation, leaving the [EIP-2930](./eip-2930.md) `access_list_cost` and the [EIP-7976](./eip-7976.md) floor calculation unchanged:

```python
tx.gasUsed = (
    21000
    + access_list_data_cost
    +
    max(
        STANDARD_TOKEN_COST * tokens_in_calldata
        + execution_gas_used
        + isContractCreation * (32000 + INITCODE_WORD_COST * words(calldata))
        + access_list_cost,
        TOTAL_COST_FLOOR_PER_TOKEN * floor_tokens_in_calldata
    )
)
```

Any transaction with a gas limit below `tx.gasUsed` evaluated with `execution_gas_used = 0` is considered invalid.

## Rationale

Access list data is always charged at floor rate (added to `access_list_cost`), and access list tokens are included in the floor calculation. This ensures:

- Access list data always pays floor rate regardless of execution level
- Access lists cannot be used to bypass the calldata floor pricing
- Consistent pricing across all transaction data sources

## Backwards Compatibility

This is a backwards incompatible gas repricing that requires a scheduled network upgrade.

Requires updates to gas estimation in wallets and nodes. Normal usage patterns remain largely unaffected.

## Reference Implementation

```python
def calculate_access_list_floor_tokens(access_list):
    """Count floor data tokens (4 per byte) in access list."""
    # Each access entry: 20-byte address + 32 bytes per storage key
    total_bytes = sum(20 + 32 * len(access.slots) for access in access_list)
    return total_bytes * 4

def calculate_intrinsic_cost(tx):
    """
    Calculate intrinsic gas cost and floor gas cost.
    Returns (intrinsic_gas, floor_gas).
    """
    # Calldata tokens (EIP-7976)
    zero_bytes = count_zero_bytes(tx.data)
    nonzero_bytes = len(tx.data) - zero_bytes
    tokens_in_calldata = zero_bytes + nonzero_bytes * 4
    floor_tokens_in_calldata = len(tx.data) * 4

    # Access list floor tokens and cost
    floor_tokens_in_access_list = 0
    access_list_cost = 0
    if has_access_list(tx):
        floor_tokens_in_access_list = calculate_access_list_floor_tokens(tx.access_list)
        for access in tx.access_list:
            access_list_cost += (
                ACCESS_LIST_ADDRESS_COST
                + len(access.slots) * ACCESS_LIST_STORAGE_KEY_COST
            )
        # EIP-7981: Always charge data cost
        access_list_cost += floor_tokens_in_access_list * TOTAL_COST_FLOOR_PER_TOKEN

    # EIP-7981: Floor includes all floor data tokens
    total_floor_data_tokens = floor_tokens_in_calldata + floor_tokens_in_access_list
    floor_gas = TX_BASE_COST + total_floor_data_tokens * TOTAL_COST_FLOOR_PER_TOKEN

    # Intrinsic gas
    calldata_cost = tokens_in_calldata * STANDARD_TOKEN_COST
    create_cost = TX_CREATE_COST + init_code_cost(tx.data) if is_create(tx) else 0
    intrinsic_gas = TX_BASE_COST + calldata_cost + create_cost + access_list_cost

    return intrinsic_gas, floor_gas
```

## Security Considerations

This EIP closes a loophole that allows circumventing [EIP-7623](./eip-7623.md) floor pricing. Without this fix, attackers can achieve larger blocks than intended by combining access lists with calldata. All transaction data sources now contribute to the floor calculation consistently.

## Copyright

Copyright and related rights waived via [CC0](../LICENSE.md).
````

</details>

<details><summary><b>Step 8 — final</b> (567 words)</summary>

````text
## Abstract

This EIP charges access lists for their data footprint, preventing the circumvention of the [EIP-7623](./eip-7623.md) floor pricing. This effectively reduces the worst-case block size by ~21% with minimal impact on users.

## Motivation

Access lists are only priced for storage but not for their data.

Furthermore, access lists can circumvent the [EIP-7623](./eip-7623.md) floor pricing by contributing to EVM gas while still leaving a non-negligible data footprint. This enables achieving the maximal possible block size by combining access lists with calldata at a certain ratio.

## Specification

| Parameter                              | Value | Source |
| -------------------------------------- | ----- | ------ |
| `ACCESS_LIST_ADDRESS_COST`            | `2400` | [EIP-2930](./eip-2930.md) |
| `ACCESS_LIST_STORAGE_KEY_COST`        | `1900` | [EIP-2930](./eip-2930.md) |
| `TOTAL_COST_FLOOR_PER_TOKEN`          | `16`   | [EIP-7976](./eip-7976.md) |

Let `access_list_bytes` be the total byte count of addresses (20 bytes each) and storage keys (32 bytes each) in the access list.

Let `access_list_data_cost = 64 * access_list_bytes` (i.e. `1280` gas per address and `2048` gas per storage key). The `64` gas-per-byte rate matches the [EIP-7976](./eip-7976.md) calldata floor.

The access list data cost is added as a flat surcharge to the gas used calculation, leaving the [EIP-2930](./eip-2930.md) `access_list_cost` and the [EIP-7976](./eip-7976.md) floor calculation unchanged:

```python
tx.gasUsed = (
    21000
    + access_list_data_cost
    +
    max(
        STANDARD_TOKEN_COST * tokens_in_calldata
        + execution_gas_used
        + isContractCreation * (32000 + INITCODE_WORD_COST * words(calldata))
        + access_list_cost,
        TOTAL_COST_FLOOR_PER_TOKEN * floor_tokens_in_calldata
    )
)
```

Any transaction with a gas limit below `tx.gasUsed` evaluated with `execution_gas_used = 0` is considered invalid.

## Rationale

Access list data is always charged at floor rate (added to `access_list_cost`), and access list tokens are included in the floor calculation. This ensures:

- Access list data always pays floor rate regardless of execution level
- Access lists cannot be used to bypass the calldata floor pricing
- Consistent pricing across all transaction data sources

## Backwards Compatibility

This is a backwards incompatible gas repricing that requires a scheduled network upgrade.

Requires updates to gas estimation in wallets and nodes. Normal usage patterns remain largely unaffected.

## Reference Implementation

```python
def calculate_access_list_data_cost(access_list):
    """EIP-7981: flat 64 gas per byte of access list data."""
    # Each access entry: 20-byte address + 32 bytes per storage key
    total_bytes = sum(20 + 32 * len(access.slots) for access in access_list)
    return total_bytes * 64

def calculate_intrinsic_cost(tx):
    """
    Calculate intrinsic gas cost and floor gas cost.
    Both include the EIP-7981 access list data surcharge, so that
    tx.gasUsed = max(intrinsic_gas + execution_gas_used, floor_gas).
    """
    # Calldata tokens (EIP-7976)
    zero_bytes = count_zero_bytes(tx.data)
    nonzero_bytes = len(tx.data) - zero_bytes
    tokens_in_calldata = zero_bytes + nonzero_bytes * 4
    floor_tokens_in_calldata = len(tx.data) * 4

    # Access list cost (EIP-2930, unchanged) and EIP-7981 data surcharge
    access_list_cost = 0
    access_list_data_cost = 0
    if has_access_list(tx):
        for access in tx.access_list:
            access_list_cost += (
                ACCESS_LIST_ADDRESS_COST
                + len(access.slots) * ACCESS_LIST_STORAGE_KEY_COST
            )
        access_list_data_cost = calculate_access_list_data_cost(tx.access_list)

    # EIP-7976 floor (calldata only) plus EIP-7981 surcharge
    floor_gas = (
        TX_BASE_COST
        + floor_tokens_in_calldata * TOTAL_COST_FLOOR_PER_TOKEN
        + access_list_data_cost
    )

    # Intrinsic gas plus EIP-7981 surcharge
    calldata_cost = tokens_in_calldata * STANDARD_TOKEN_COST
    create_cost = TX_CREATE_COST + init_code_cost(tx.data) if is_create(tx) else 0
    intrinsic_gas = (
        TX_BASE_COST
        + calldata_cost
        + create_cost
        + access_list_cost
        + access_list_data_cost
    )

    return intrinsic_gas, floor_gas
```

## Security Considerations

This EIP closes a loophole that allows circumventing [EIP-7623](./eip-7623.md) floor pricing. Without this fix, attackers can achieve larger blocks than intended by combining access lists with calldata. All transaction data sources now contribute to the floor calculation consistently.

## Copyright

Copyright and related rights waived via [CC0](../LICENSE.md).
````

</details>
