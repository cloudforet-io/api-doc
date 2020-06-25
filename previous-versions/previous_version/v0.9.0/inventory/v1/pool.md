---
description: null
---

# Pool

> **Package : spaceone.api.inventory.v1**

## Pool

{% hint style="info" %}
**Pool Methods:**
{% endhint %}

| NO | Method | Request Type | Response Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [create](pool.md#create) | [CreatePoolRequest](pool.md#createpoolrequest) | [PoolInfo](pool.md#poolinfo) |  |
| 2 | [update](pool.md#update) | [UpdatePoolRequest](pool.md#updatepoolrequest) | [PoolInfo](pool.md#poolinfo) |  |
| 3 | [delete](pool.md#delete) | [PoolRequest](pool.md#poolrequest) | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |  |
| 4 | [get](pool.md#get) | [GetPoolRequest](pool.md#getpoolrequest) | [PoolInfo](pool.md#poolinfo) |  |
| 5 | [add\_member](pool.md#add_member) | [PoolMemberRequest](pool.md#poolmemberrequest) | [PoolMemberInfo](pool.md#poolmemberinfo) |  |
| 6 | [modify\_member](pool.md#modify_member) | [PoolMemberRequest](pool.md#poolmemberrequest) | [PoolMemberInfo](pool.md#poolmemberinfo) |  |
| 7 | [remove\_member](pool.md#remove_member) | [RemovePoolMemberRequest](pool.md#removepoolmemberrequest) | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |  |
| 8 | [list\_members](pool.md#list_members) | [PoolMemberQuery](pool.md#poolmemberquery) | [PoolMembersInfo](pool.md#poolmembersinfo) |  |
| 9 | [list](pool.md#list) | [PoolQuery](pool.md#poolquery) | [PoolsInfo](pool.md#poolsinfo) |  |
| 10 | [stat](pool.md#stat) | [PoolStatQuery](pool.md#poolstatquery) | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |  |

### create

> **POST** /inventory/v1/pools

| Type | Message |
| :--- | :--- |
| Request | [CreatePoolRequest](pool.md#createpoolrequest) |
| Response | [PoolInfo](pool.md#poolinfo) |

### update

> **PUT** /inventory/v1/pool/{pool\_id}

| Type | Message |
| :--- | :--- |
| Request | [UpdatePoolRequest](pool.md#updatepoolrequest) |
| Response | [PoolInfo](pool.md#poolinfo) |

### delete

> **DELETE** /inventory/v1/pool/{pool\_id}

| Type | Message |
| :--- | :--- |
| Request | [PoolRequest](pool.md#poolrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |

### get

> **GET** /inventory/v1/pool/{pool\_id}

| Type | Message |
| :--- | :--- |
| Request | [GetPoolRequest](pool.md#getpoolrequest) |
| Response | [PoolInfo](pool.md#poolinfo) |

### add\_member

> **GET** /inventory/v1/pool/{pool\_id}/members

| Type | Message |
| :--- | :--- |
| Request | [PoolMemberRequest](pool.md#poolmemberrequest) |
| Response | [PoolMemberInfo](pool.md#poolmemberinfo) |

### modify\_member

> **GET** /inventory/v1/pool/{pool\_id}/member/{user\_id}

| Type | Message |
| :--- | :--- |
| Request | [PoolMemberRequest](pool.md#poolmemberrequest) |
| Response | [PoolMemberInfo](pool.md#poolmemberinfo) |

### remove\_member

> **GET** /inventory/v1/pool/{pool\_id}/member/{user\_id}

| Type | Message |
| :--- | :--- |
| Request | [RemovePoolMemberRequest](pool.md#removepoolmemberrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |

### list\_members

> **GET** /inventory/v1/pool/{pool\_id}/members
>
> **POST** /inventory/v1/pool/{pool\_id}/members/search

| Type | Message |
| :--- | :--- |
| Request | [PoolMemberQuery](pool.md#poolmemberquery) |
| Response | [PoolMembersInfo](pool.md#poolmembersinfo) |

### list

> **GET** /inventory/v1/pools
>
> **POST** /inventory/v1/pools/search

| Type | Message |
| :--- | :--- |
| Request | [PoolQuery](pool.md#poolquery) |
| Response | [PoolsInfo](pool.md#poolsinfo) |

### stat

> **POST** /inventory/v1/pools/stat

| Type | Message |
| :--- | :--- |
| Request | [PoolStatQuery](pool.md#poolstatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |

## Message

### CreatePoolRequest

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | name | string |  | required |
| 2 | zone\_id | string |  | required |
| 3 | domain\_id | string |  | required |
| 4 | tags | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |  | optional |

### GetPoolRequest

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | pool\_id | string |  | required |
| 2 | domain\_id | string |  | required |
| 3 | only | string |  | optional |

### PoolInfo

<table>
  <thead>
    <tr>
      <th style="text-align:left">No</th>
      <th style="text-align:left">Field</th>
      <th style="text-align:left">Type</th>
      <th style="text-align:left">Required</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">1</td>
      <td style="text-align:left">pool_id</td>
      <td style="text-align:left">string</td>
      <td style="text-align:left"></td>
      <td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">2</td>
      <td style="text-align:left">name</td>
      <td style="text-align:left">string</td>
      <td style="text-align:left"></td>
      <td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">3</td>
      <td style="text-align:left">state</td>
      <td style="text-align:left">
        <p>PoolInfo.State</p>
        <ul>
          <li>NONE</li>
          <li>ACTIVE</li>
          <li>DELETED</li>
        </ul>
      </td>
      <td style="text-align:left"></td>
      <td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">4</td>
      <td style="text-align:left">tags</td>
      <td style="text-align:left"> <a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a>
      </td>
      <td style="text-align:left"></td>
      <td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">5</td>
      <td style="text-align:left">domain_id</td>
      <td style="text-align:left">string</td>
      <td style="text-align:left"></td>
      <td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">6</td>
      <td style="text-align:left">region_info</td>
      <td style="text-align:left"> <a href="pool.md#regioninfo">RegionInfo</a>
      </td>
      <td style="text-align:left"></td>
      <td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">7</td>
      <td style="text-align:left">zone_info</td>
      <td style="text-align:left"> <a href="pool.md#zoneinfo">ZoneInfo</a>
      </td>
      <td style="text-align:left"></td>
      <td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">8</td>
      <td style="text-align:left">created_at</td>
      <td style="text-align:left"> <a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto">google.protobuf.Timestamp</a>
      </td>
      <td style="text-align:left"></td>
      <td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">9</td>
      <td style="text-align:left">deleted_at</td>
      <td style="text-align:left"> <a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto">google.protobuf.Timestamp</a>
      </td>
      <td style="text-align:left"></td>
      <td style="text-align:left"></td>
    </tr>
  </tbody>
</table>

### PoolMemberInfo

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | pool\_info | [PoolInfo](pool.md#poolinfo) |  |  |
| 2 | user\_info | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |  |  |
| 3 | labels | string |  |  |

### PoolMemberQuery

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query | [spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query) |  | optional |
| 2 | pool\_id | string |  | optional |
| 3 | user\_id | string |  | optional |
| 4 | domain\_id | string |  | required |

### PoolMemberRequest

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | pool\_id | string |  | required |
| 2 | user\_id | string |  | required |
| 3 | labels | string |  | optional |
| 4 | domain\_id | string |  | required |

### PoolMembersInfo

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | results | [PoolMemberInfo](pool.md#poolmemberinfo) |  |  |
| 2 | total\_count | [int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) |  |  |

### PoolQuery

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query | [spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query) |  | optional |
| 2 | pool\_id | string |  | optional |
| 3 | region\_id | string |  | optional |
| 4 | zone\_id | string |  | optional |
| 5 | domain\_id | string |  | required |
| 6 | name | string |  | optional |

### PoolRequest

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | pool\_id | string |  | required |
| 2 | domain\_id | string |  | required |

### PoolStatQuery

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query | [spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query) |  | required |
| 2 | domain\_id | string |  | required |

### PoolsInfo

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | results | [PoolInfo](pool.md#poolinfo) |  |  |
| 2 | total\_count | [int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) |  |  |

### RemovePoolMemberRequest

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | pool\_id | string |  | required |
| 2 | user\_id | string |  | required |
| 3 | domain\_id | string |  | required |

### UpdatePoolRequest

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | pool\_id | string |  | required |
| 2 | domain\_id | string |  | required |
| 3 | name | string |  | optional |
| 4 | tags | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |  | optional |

