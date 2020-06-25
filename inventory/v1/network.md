---
description: null
---

# Network

> **Package : spaceone.api.inventory.v1**

## Network

{% hint style="info" %}
**Network Methods:**
{% endhint %}

| NO | Method | Request Type | Response Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [create](network.md#create) | [CreateNetworkRequest](network.md#createnetworkrequest) | [NetworkInfo](network.md#networkinfo) |  |
| 2 | [update](network.md#update) | [UpdateNetworkRequest](network.md#updatenetworkrequest) | [NetworkInfo](network.md#networkinfo) |  |
| 3 | [pin\_data](network.md#pin_data) | [PinNetworkDataRequest](network.md#pinnetworkdatarequest) | [NetworkInfo](network.md#networkinfo) |  |
| 4 | [delete](network.md#delete) | [NetworkRequest](network.md#networkrequest) | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |  |
| 5 | [get](network.md#get) | [GetNetworkRequest](network.md#getnetworkrequest) | [NetworkInfo](network.md#networkinfo) |  |
| 6 | [list](network.md#list) | [NetworkQuery](network.md#networkquery) | [NetworksInfo](network.md#networksinfo) |  |
| 7 | [stat](network.md#stat) | [NetworkStatQuery](network.md#networkstatquery) | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |  |

### create

> **POST** /inventory/v1/networks

| Type | Message |
| :--- | :--- |
| Request | [CreateNetworkRequest](network.md#createnetworkrequest) |
| Response | [NetworkInfo](network.md#networkinfo) |

### update

> **PUT** /inventory/v1/network/{network\_id}

| Type | Message |
| :--- | :--- |
| Request | [UpdateNetworkRequest](network.md#updatenetworkrequest) |
| Response | [NetworkInfo](network.md#networkinfo) |

### pin\_data

> **PUT** /inventory/v1/network/{network\_id}/pin-data

| Type | Message |
| :--- | :--- |
| Request | [PinNetworkDataRequest](network.md#pinnetworkdatarequest) |
| Response | [NetworkInfo](network.md#networkinfo) |

### delete

> **DELETE** /inventory/v1/network/{network\_id}

| Type | Message |
| :--- | :--- |
| Request | [NetworkRequest](network.md#networkrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |

### get

> **GET** /inventory/v1/network/{network\_id}

| Type | Message |
| :--- | :--- |
| Request | [GetNetworkRequest](network.md#getnetworkrequest) |
| Response | [NetworkInfo](network.md#networkinfo) |

### list

> **GET** /inventory/v1/networks
>
> **POST** /inventory/v1/networks/search

| Type | Message |
| :--- | :--- |
| Request | [NetworkQuery](network.md#networkquery) |
| Response | [NetworksInfo](network.md#networksinfo) |

### stat

> **POST** /inventory/v1/networks/stat

| Type | Message |
| :--- | :--- |
| Request | [NetworkStatQuery](network.md#networkstatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |

## Message

### CreateNetworkRequest

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | name | string |  | required |
| 2 | cidr | string |  | required |
| 3 | data | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |  | optional |
| 4 | metadata | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |  | optional |
| 5 | reference | [NetworkReference](network.md#networkreference) |  | optional |
| 6 | tags | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |  | optional |
| 7 | zone\_id | string |  | required |
| 8 | domain\_id | string |  | required |

### GetNetworkRequest

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | network\_id | string |  | required |
| 2 | domain\_id | string |  | required |
| 3 | only | string |  | optional |

### NetworkInfo

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | network\_id | string |  |  |
| 2 | name | string |  |  |
| 3 | cidr | string |  |  |
| 4 | data | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |  |  |
| 5 | metadata | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |  |  |
| 6 | reference | [NetworkReference](network.md#networkreference) |  |  |
| 7 | tags | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |  |  |
| 8 | collection\_info | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |  |  |
| 9 | region\_info | [RegionInfo](network.md#regioninfo) |  |  |
| 10 | zone\_info | [ZoneInfo](network.md#zoneinfo) |  |  |
| 11 | domain\_id | string |  |  |
| 12 | created\_at | [google.protobuf.Timestamp](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto) |  |  |

### NetworkQuery

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query | [spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query) |  | optional |
| 2 | network\_id | string |  | optional |
| 3 | name | string |  | optional |
| 4 | cidr | string |  | optional |
| 5 | zone\_id | string |  | optional |
| 6 | region\_id | string |  | optional |
| 7 | domain\_id | string |  | required |

### NetworkReference

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | resource\_id | string |  |  |
| 2 | external\_link | string |  |  |

### NetworkRequest

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | network\_id | string |  | required |
| 2 | domain\_id | string |  | required |

### NetworkStatQuery

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query | [spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query) |  | required |
| 2 | domain\_id | string |  | required |

### NetworksInfo

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | results | [NetworkInfo](network.md#networkinfo) |  |  |
| 2 | total\_count | [int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) |  |  |

### PinNetworkDataRequest

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | network\_id | string |  | required |
| 2 | keys | string |  | required |
| 3 | domain\_id | string |  | required |

### UpdateNetworkRequest

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | network\_id | string |  | required |
| 2 | name | string |  | optional |
| 3 | data | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |  | optional |
| 4 | metadata | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |  | optional |
| 5 | reference | [NetworkReference](network.md#networkreference) |  | optional |
| 6 | tags | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |  | optional |
| 7 | domain\_id | string |  | required |

