---
description: null
---

# Zone

> **Package : spaceone.api.inventory.v1**

## Zone

{% hint style="info" %}
**Zone Methods:**
{% endhint %}

| NO | Method | Request Type | Response Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [create](zone.md#create) | [CreateZoneRequest](zone.md#createzonerequest) | [ZoneInfo](zone.md#zoneinfo) |  |
| 2 | [update](zone.md#update) | [UpdateZoneRequest](zone.md#updatezonerequest) | [ZoneInfo](zone.md#zoneinfo) |  |
| 3 | [delete](zone.md#delete) | [ZoneRequest](zone.md#zonerequest) | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |  |
| 4 | [get](zone.md#get) | [GetZoneRequest](zone.md#getzonerequest) | [ZoneInfo](zone.md#zoneinfo) |  |
| 5 | [add\_member](zone.md#add_member) | [ZoneMemberRequest](zone.md#zonememberrequest) | [ZoneMemberInfo](zone.md#zonememberinfo) |  |
| 6 | [modify\_member](zone.md#modify_member) | [ZoneMemberRequest](zone.md#zonememberrequest) | [ZoneMemberInfo](zone.md#zonememberinfo) |  |
| 7 | [remove\_member](zone.md#remove_member) | [RemoveZoneMemberRequest](zone.md#removezonememberrequest) | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |  |
| 8 | [list\_members](zone.md#list_members) | [ZoneMemberQuery](zone.md#zonememberquery) | [ZoneMembersInfo](zone.md#zonemembersinfo) |  |
| 9 | [list](zone.md#list) | [ZoneQuery](zone.md#zonequery) | [ZonesInfo](zone.md#zonesinfo) |  |
| 10 | [stat](zone.md#stat) | [ZoneStatQuery](zone.md#zonestatquery) | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |  |

### create

> **POST** /inventory/v1/zones

| Type | Message |
| :--- | :--- |
| Request | [CreateZoneRequest](zone.md#createzonerequest) |
| Response | [ZoneInfo](zone.md#zoneinfo) |

### update

> **PUT** /inventory/v1/zone/{zone\_id}

| Type | Message |
| :--- | :--- |
| Request | [UpdateZoneRequest](zone.md#updatezonerequest) |
| Response | [ZoneInfo](zone.md#zoneinfo) |

### delete

> **DELETE** /inventory/v1/zone/{zone\_id}

| Type | Message |
| :--- | :--- |
| Request | [ZoneRequest](zone.md#zonerequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |

### get

> **GET** /inventory/v1/zone/{zone\_id}

| Type | Message |
| :--- | :--- |
| Request | [GetZoneRequest](zone.md#getzonerequest) |
| Response | [ZoneInfo](zone.md#zoneinfo) |

### add\_member

> **GET** /inventory/v1/zone/{zone\_id}/members

| Type | Message |
| :--- | :--- |
| Request | [ZoneMemberRequest](zone.md#zonememberrequest) |
| Response | [ZoneMemberInfo](zone.md#zonememberinfo) |

### modify\_member

> **GET** /inventory/v1/zone/{zone\_id}/member/{user\_id}

| Type | Message |
| :--- | :--- |
| Request | [ZoneMemberRequest](zone.md#zonememberrequest) |
| Response | [ZoneMemberInfo](zone.md#zonememberinfo) |

### remove\_member

> **GET** /inventory/v1/zone/{zone\_id}/member/{user\_id}

| Type | Message |
| :--- | :--- |
| Request | [RemoveZoneMemberRequest](zone.md#removezonememberrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |

### list\_members

> **GET** /inventory/v1/zone/{zone\_id}/members
>
> **POST** /inventory/v1/zone/{zone\_id}/members/search

| Type | Message |
| :--- | :--- |
| Request | [ZoneMemberQuery](zone.md#zonememberquery) |
| Response | [ZoneMembersInfo](zone.md#zonemembersinfo) |

### list

> **GET** /inventory/v1/zones
>
> **POST** /inventory/v1/zones/search

| Type | Message |
| :--- | :--- |
| Request | [ZoneQuery](zone.md#zonequery) |
| Response | [ZonesInfo](zone.md#zonesinfo) |

### stat

> **POST** /inventory/v1/zones/stat

| Type | Message |
| :--- | :--- |
| Request | [ZoneStatQuery](zone.md#zonestatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |

## Message

### CreateZoneRequest

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | name | string |  | required |
| 2 | region\_id | string |  | required |
| 3 | domain\_id | string |  | required |
| 4 | tags | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |  | optional |

### GetZoneRequest

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | zone\_id | string |  | required |
| 2 | domain\_id | string |  | required |
| 3 | only | string |  | optional |

### RemoveZoneMemberRequest

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | zone\_id | string |  | required |
| 2 | user\_id | string |  | required |
| 3 | domain\_id | string |  | required |

### UpdateZoneRequest

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | zone\_id | string |  | required |
| 2 | name | string |  | optional |
| 3 | tags | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |  | optional |
| 4 | domain\_id | string |  | required |

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
      <td style="text-align:left"> <a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a>
      </td>
      <td style="text-align:left"></td>
      <td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">5</td>
      <td style="text-align:left">region_info</td>
      <td style="text-align:left"> <a href="zone.md#regioninfo">RegionInfo</a>
      </td>
      <td style="text-align:left"></td>
      <td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">6</td>
      <td style="text-align:left">domain_id</td>
      <td style="text-align:left">string</td>
      <td style="text-align:left"></td>
      <td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">7</td>
      <td style="text-align:left">created_at</td>
      <td style="text-align:left"> <a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto">google.protobuf.Timestamp</a>
      </td>
      <td style="text-align:left"></td>
      <td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">8</td>
      <td style="text-align:left">deleted_at</td>
      <td style="text-align:left"> <a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto">google.protobuf.Timestamp</a>
      </td>
      <td style="text-align:left"></td>
      <td style="text-align:left"></td>
    </tr>
  </tbody>
</table>

### ZoneMemberInfo

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | zone\_info | [ZoneInfo](zone.md#zoneinfo) |  |  |
| 2 | user\_info | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |  |  |
| 3 | labels | string |  |  |

### ZoneMemberQuery

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query | [spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query) |  | optional |
| 2 | zone\_id | string |  | optional |
| 3 | user\_id | string |  | optional |
| 4 | domain\_id | string |  | required |

### ZoneMemberRequest

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | zone\_id | string |  | required |
| 2 | user\_id | string |  | required |
| 3 | labels | string |  | optional |
| 4 | domain\_id | string |  | required |

### ZoneMembersInfo

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | results | [ZoneMemberInfo](zone.md#zonememberinfo) |  |  |
| 2 | total\_count | [int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) |  |  |

### ZoneQuery

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | zone\_id | string |  | optional |
| 2 | region\_id | string |  | optional |
| 3 | query | [spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query) |  | optional |
| 4 | name | string |  | optional |
| 5 | domain\_id | string |  | required |

### ZoneRequest

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | zone\_id | string |  | required |
| 2 | domain\_id | string |  | required |

### ZoneStatQuery

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query | [spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query) |  | required |
| 2 | domain\_id | string |  | required |

### ZonesInfo

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | results | [ZoneInfo](zone.md#zoneinfo) |  |  |
| 2 | total\_count | [int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) |  |  |

