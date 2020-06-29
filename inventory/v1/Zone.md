---
description:  
---
# Zone

>  **Package : spaceone.api.inventory.v1**

## Zone

{% hint style="info" %}
**Zone Methods:**

{%  endhint %}


| NO |  Method | Request Type | Response Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [create](Zone.md#create)| [CreateZoneRequest](Zone.md#createzonerequest) | [ZoneInfo](Zone.md#zoneinfo) |  |
| 2 | [update](Zone.md#update)| [UpdateZoneRequest](Zone.md#updatezonerequest) | [ZoneInfo](Zone.md#zoneinfo) |  |
| 3 | [delete](Zone.md#delete)| [ZoneRequest](Zone.md#zonerequest) |[google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| 4 | [get](Zone.md#get)| [GetZoneRequest](Zone.md#getzonerequest) | [ZoneInfo](Zone.md#zoneinfo) |  |
| 5 | [add_member](Zone.md#add_member)| [ZoneMemberRequest](Zone.md#zonememberrequest) | [ZoneMemberInfo](Zone.md#zonememberinfo) |  |
| 6 | [modify_member](Zone.md#modify_member)| [ZoneMemberRequest](Zone.md#zonememberrequest) | [ZoneMemberInfo](Zone.md#zonememberinfo) |  |
| 7 | [remove_member](Zone.md#remove_member)| [RemoveZoneMemberRequest](Zone.md#removezonememberrequest) |[google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| 8 | [list_members](Zone.md#list_members)| [ZoneMemberQuery](Zone.md#zonememberquery) | [ZoneMembersInfo](Zone.md#zonemembersinfo) |  |
| 9 | [list](Zone.md#list)| [ZoneQuery](Zone.md#zonequery) | [ZonesInfo](Zone.md#zonesinfo) |  |
| 10 | [stat](Zone.md#stat)| [ZoneStatQuery](Zone.md#zonestatquery) |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  |

### create
> **POST** /inventory/v1/zones
>



| Type | Message |
| :--- | :--- |
| Request | [CreateZoneRequest](Zone.md#createzonerequest) |
| Response |  [ZoneInfo](Zone.md#zoneinfo)  |



### update
> **PUT** /inventory/v1/zone/{zone_id}
>



| Type | Message |
| :--- | :--- |
| Request | [UpdateZoneRequest](Zone.md#updatezonerequest) |
| Response |  [ZoneInfo](Zone.md#zoneinfo)  |



### delete
> **DELETE** /inventory/v1/zone/{zone_id}
>



| Type | Message |
| :--- | :--- |
| Request | [ZoneRequest](Zone.md#zonerequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |



### get
> **GET** /inventory/v1/zone/{zone_id}
>



| Type | Message |
| :--- | :--- |
| Request | [GetZoneRequest](Zone.md#getzonerequest) |
| Response |  [ZoneInfo](Zone.md#zoneinfo)  |



### add_member
> **GET** /inventory/v1/zone/{zone_id}/members
>



| Type | Message |
| :--- | :--- |
| Request | [ZoneMemberRequest](Zone.md#zonememberrequest) |
| Response |  [ZoneMemberInfo](Zone.md#zonememberinfo)  |



### modify_member
> **GET** /inventory/v1/zone/{zone_id}/member/{user_id}
>



| Type | Message |
| :--- | :--- |
| Request | [ZoneMemberRequest](Zone.md#zonememberrequest) |
| Response |  [ZoneMemberInfo](Zone.md#zonememberinfo)  |



### remove_member
> **GET** /inventory/v1/zone/{zone_id}/member/{user_id}
>



| Type | Message |
| :--- | :--- |
| Request | [RemoveZoneMemberRequest](Zone.md#removezonememberrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |



### list_members
> **GET** /inventory/v1/zone/{zone_id}/members
>
> **POST** /inventory/v1/zone/{zone_id}/members/search




| Type | Message |
| :--- | :--- |
| Request | [ZoneMemberQuery](Zone.md#zonememberquery) |
| Response |  [ZoneMembersInfo](Zone.md#zonemembersinfo)  |



### list
> **GET** /inventory/v1/zones
>
> **POST** /inventory/v1/zones/search




| Type | Message |
| :--- | :--- |
| Request | [ZoneQuery](Zone.md#zonequery) |
| Response |  [ZonesInfo](Zone.md#zonesinfo)  |



### stat
> **POST** /inventory/v1/zones/stat
>



| Type | Message |
| :--- | :--- |
| Request | [ZoneStatQuery](Zone.md#zonestatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |





## Message

### CreateZoneRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | name |string |✅ ||
| 2 | region_id |string |✅ ||
| 3 | domain_id |string |✅ ||
| 4 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |❌ ||

### GetZoneRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | zone_id |string |✅ ||
| 2 | domain_id |string |✅ ||
| 3 | only |string |❌ ||

### RemoveZoneMemberRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | zone_id |string |✅ ||
| 2 | user_id |string |✅ ||
| 3 | domain_id |string |✅ ||

### UpdateZoneRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | zone_id |string |✅ ||
| 2 | name |string |❌ ||
| 3 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |❌ ||
| 4 | domain_id |string |✅ ||

### ZoneInfo
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
      <td style="text-align:left">zone_id</td>
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
<p>ZoneInfo.State</p>
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
      <td style="text-align:left">region_info</td>
      <td style="text-align:left">
<a href="Zone.md#regioninfo">RegionInfo</a>
</td>
        <td style="text-align:left"></td>
<td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">6</td>
      <td style="text-align:left">domain_id</td>
      <td style="text-align:left">

string

</td>
        <td style="text-align:left"></td>
<td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">7</td>
      <td style="text-align:left">created_at</td>
      <td style="text-align:left">
<a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto">google.protobuf.Timestamp</a>
</td>
        <td style="text-align:left"></td>
<td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">8</td>
      <td style="text-align:left">deleted_at</td>
      <td style="text-align:left">
<a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto">google.protobuf.Timestamp</a>
</td>
        <td style="text-align:left"></td>
<td style="text-align:left"></td>
    </tr>
  </tbody>
</table>


### ZoneMemberInfo
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | zone_info |[ZoneInfo](Zone.md#zoneinfo) | ||
| 2 | user_info |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | ||
| 3 | labels |string | ||

### ZoneMemberQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query) |❌ ||
| 2 | zone_id |string |❌ ||
| 3 | user_id |string |❌ ||
| 4 | domain_id |string |✅ ||

### ZoneMemberRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | zone_id |string |✅ ||
| 2 | user_id |string |✅ ||
| 3 | labels |string |❌ ||
| 4 | domain_id |string |✅ ||

### ZoneMembersInfo
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | results |[ZoneMemberInfo](Zone.md#zonememberinfo) | ||
| 2 | total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | ||

### ZoneQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | zone_id |string |❌ ||
| 2 | region_id |string |❌ ||
| 3 | query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query) |❌ ||
| 4 | name |string |❌ ||
| 5 | domain_id |string |✅ ||

### ZoneRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | zone_id |string |✅ ||
| 2 | domain_id |string |✅ ||

### ZoneStatQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query) |✅ ||
| 2 | domain_id |string |✅ ||

### ZonesInfo
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | results |[ZoneInfo](Zone.md#zoneinfo) | ||
| 2 | total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | ||
