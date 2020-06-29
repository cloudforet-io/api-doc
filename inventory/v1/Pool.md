---
description:  
---
# Pool

>  **Package : spaceone.api.inventory.v1**

## Pool

{% hint style="info" %}
**Pool Methods:**

{%  endhint %}


| NO |  Method | Request Type | Response Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [create](Pool.md#create)| [CreatePoolRequest](Pool.md#createpoolrequest) | [PoolInfo](Pool.md#poolinfo) |  |
| 2 | [update](Pool.md#update)| [UpdatePoolRequest](Pool.md#updatepoolrequest) | [PoolInfo](Pool.md#poolinfo) |  |
| 3 | [delete](Pool.md#delete)| [PoolRequest](Pool.md#poolrequest) |[google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| 4 | [get](Pool.md#get)| [GetPoolRequest](Pool.md#getpoolrequest) | [PoolInfo](Pool.md#poolinfo) |  |
| 5 | [add_member](Pool.md#add_member)| [PoolMemberRequest](Pool.md#poolmemberrequest) | [PoolMemberInfo](Pool.md#poolmemberinfo) |  |
| 6 | [modify_member](Pool.md#modify_member)| [PoolMemberRequest](Pool.md#poolmemberrequest) | [PoolMemberInfo](Pool.md#poolmemberinfo) |  |
| 7 | [remove_member](Pool.md#remove_member)| [RemovePoolMemberRequest](Pool.md#removepoolmemberrequest) |[google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| 8 | [list_members](Pool.md#list_members)| [PoolMemberQuery](Pool.md#poolmemberquery) | [PoolMembersInfo](Pool.md#poolmembersinfo) |  |
| 9 | [list](Pool.md#list)| [PoolQuery](Pool.md#poolquery) | [PoolsInfo](Pool.md#poolsinfo) |  |
| 10 | [stat](Pool.md#stat)| [PoolStatQuery](Pool.md#poolstatquery) |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  |

### create
> **POST** /inventory/v1/pools
>



| Type | Message |
| :--- | :--- |
| Request | [CreatePoolRequest](Pool.md#createpoolrequest) |
| Response |  [PoolInfo](Pool.md#poolinfo)  |



### update
> **PUT** /inventory/v1/pool/{pool_id}
>



| Type | Message |
| :--- | :--- |
| Request | [UpdatePoolRequest](Pool.md#updatepoolrequest) |
| Response |  [PoolInfo](Pool.md#poolinfo)  |



### delete
> **DELETE** /inventory/v1/pool/{pool_id}
>



| Type | Message |
| :--- | :--- |
| Request | [PoolRequest](Pool.md#poolrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |



### get
> **GET** /inventory/v1/pool/{pool_id}
>



| Type | Message |
| :--- | :--- |
| Request | [GetPoolRequest](Pool.md#getpoolrequest) |
| Response |  [PoolInfo](Pool.md#poolinfo)  |



### add_member
> **GET** /inventory/v1/pool/{pool_id}/members
>



| Type | Message |
| :--- | :--- |
| Request | [PoolMemberRequest](Pool.md#poolmemberrequest) |
| Response |  [PoolMemberInfo](Pool.md#poolmemberinfo)  |



### modify_member
> **GET** /inventory/v1/pool/{pool_id}/member/{user_id}
>



| Type | Message |
| :--- | :--- |
| Request | [PoolMemberRequest](Pool.md#poolmemberrequest) |
| Response |  [PoolMemberInfo](Pool.md#poolmemberinfo)  |



### remove_member
> **GET** /inventory/v1/pool/{pool_id}/member/{user_id}
>



| Type | Message |
| :--- | :--- |
| Request | [RemovePoolMemberRequest](Pool.md#removepoolmemberrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |



### list_members
> **GET** /inventory/v1/pool/{pool_id}/members
>
> **POST** /inventory/v1/pool/{pool_id}/members/search




| Type | Message |
| :--- | :--- |
| Request | [PoolMemberQuery](Pool.md#poolmemberquery) |
| Response |  [PoolMembersInfo](Pool.md#poolmembersinfo)  |



### list
> **GET** /inventory/v1/pools
>
> **POST** /inventory/v1/pools/search




| Type | Message |
| :--- | :--- |
| Request | [PoolQuery](Pool.md#poolquery) |
| Response |  [PoolsInfo](Pool.md#poolsinfo)  |



### stat
> **POST** /inventory/v1/pools/stat
>



| Type | Message |
| :--- | :--- |
| Request | [PoolStatQuery](Pool.md#poolstatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |





## Message

### CreatePoolRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | name |string |✅ ||
| 2 | zone_id |string |✅ ||
| 3 | domain_id |string |✅ ||
| 4 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |❌ ||

### GetPoolRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | pool_id |string |✅ ||
| 2 | domain_id |string |✅ ||
| 3 | only |string |❌ ||

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
      <td style="text-align:left">

string

</td>
        <td style="text-align:left"></td>
<td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">2</td>
      <td style="text-align:left">name</td>
      <td style="text-align:left">

string

</td>
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
      <td style="text-align:left">
<a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a>
</td>
        <td style="text-align:left"></td>
<td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">5</td>
      <td style="text-align:left">domain_id</td>
      <td style="text-align:left">

string

</td>
        <td style="text-align:left"></td>
<td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">6</td>
      <td style="text-align:left">region_info</td>
      <td style="text-align:left">
<a href="Pool.md#regioninfo">RegionInfo</a>
</td>
        <td style="text-align:left"></td>
<td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">7</td>
      <td style="text-align:left">zone_info</td>
      <td style="text-align:left">
<a href="Pool.md#zoneinfo">ZoneInfo</a>
</td>
        <td style="text-align:left"></td>
<td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">8</td>
      <td style="text-align:left">created_at</td>
      <td style="text-align:left">
<a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto">google.protobuf.Timestamp</a>
</td>
        <td style="text-align:left"></td>
<td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">9</td>
      <td style="text-align:left">deleted_at</td>
      <td style="text-align:left">
<a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto">google.protobuf.Timestamp</a>
</td>
        <td style="text-align:left"></td>
<td style="text-align:left"></td>
    </tr>
  </tbody>
</table>


### PoolMemberInfo
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | pool_info |[PoolInfo](Pool.md#poolinfo) | ||
| 2 | user_info |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | ||
| 3 | labels |string | ||

### PoolMemberQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query) |❌ ||
| 2 | pool_id |string |❌ ||
| 3 | user_id |string |❌ ||
| 4 | domain_id |string |✅ ||

### PoolMemberRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | pool_id |string |✅ ||
| 2 | user_id |string |✅ ||
| 3 | labels |string |❌ ||
| 4 | domain_id |string |✅ ||

### PoolMembersInfo
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | results |[PoolMemberInfo](Pool.md#poolmemberinfo) | ||
| 2 | total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | ||

### PoolQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query) |❌ ||
| 2 | pool_id |string |❌ ||
| 3 | region_id |string |❌ ||
| 4 | zone_id |string |❌ ||
| 5 | domain_id |string |✅ ||
| 6 | name |string |❌ ||

### PoolRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | pool_id |string |✅ ||
| 2 | domain_id |string |✅ ||

### PoolStatQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query) |✅ ||
| 2 | domain_id |string |✅ ||

### PoolsInfo
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | results |[PoolInfo](Pool.md#poolinfo) | ||
| 2 | total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | ||

### RemovePoolMemberRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | pool_id |string |✅ ||
| 2 | user_id |string |✅ ||
| 3 | domain_id |string |✅ ||

### UpdatePoolRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | pool_id |string |✅ ||
| 2 | domain_id |string |✅ ||
| 3 | name |string |❌ ||
| 4 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |❌ ||
