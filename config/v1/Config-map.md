---
description: Config Map API which configure environments for account
---
# Config map

>  **Package : spaceone.api.config.v1**

## ConfigMap

{% hint style="info" %}
**ConfigMap Methods:**

{%  endhint %}


| NO |  Method | Request Type | Response Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [create](Config-map.md#create)| [CreateConfigMapRequest](Config-map.md#createconfigmaprequest) | [ConfigMapInfo](Config-map.md#configmapinfo) |  |
| 2 | [update](Config-map.md#update)| [UpdateConfigMapRequest](Config-map.md#updateconfigmaprequest) | [ConfigMapInfo](Config-map.md#configmapinfo) |  |
| 3 | [delete](Config-map.md#delete)| [ConfigMapRequest](Config-map.md#configmaprequest) |[google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| 4 | [get](Config-map.md#get)| [GetConfigMapRequest](Config-map.md#getconfigmaprequest) | [ConfigMapInfo](Config-map.md#configmapinfo) |  |
| 5 | [list](Config-map.md#list)| [ConfigMapQuery](Config-map.md#configmapquery) | [ConfigMapsInfo](Config-map.md#configmapsinfo) |  |
| 6 | [stat](Config-map.md#stat)| [ConfigMapStatQuery](Config-map.md#configmapstatquery) |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  |

### create
> **POST** /config/v1/config-maps
>



| Type | Message |
| :--- | :--- |
| Request | [CreateConfigMapRequest](Config-map.md#createconfigmaprequest) |
| Response |  [ConfigMapInfo](Config-map.md#configmapinfo)  |



### update
> **PUT** /config/v1/config-map/{name}
>



| Type | Message |
| :--- | :--- |
| Request | [UpdateConfigMapRequest](Config-map.md#updateconfigmaprequest) |
| Response |  [ConfigMapInfo](Config-map.md#configmapinfo)  |



### delete
> **DELETE** /config/v1/config-map/{name}
>



| Type | Message |
| :--- | :--- |
| Request | [ConfigMapRequest](Config-map.md#configmaprequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |



### get
> **GET** /config/v1/config-map/{name}
>



| Type | Message |
| :--- | :--- |
| Request | [GetConfigMapRequest](Config-map.md#getconfigmaprequest) |
| Response |  [ConfigMapInfo](Config-map.md#configmapinfo)  |



### list
> **GET** /config/v1/config-maps
>
> **POST** /config/v1/config-maps/search




| Type | Message |
| :--- | :--- |
| Request | [ConfigMapQuery](Config-map.md#configmapquery) |
| Response |  [ConfigMapsInfo](Config-map.md#configmapsinfo)  |



### stat
> **POST** /config/v1/config-maps/stat
>



| Type | Message |
| :--- | :--- |
| Request | [ConfigMapStatQuery](Config-map.md#configmapstatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |





## Message

### ConfigMapInfo
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | name |string | ||
| 2 | data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | ||
| 3 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | ||
| 4 | domain_id |string | ||
| 5 | created_at |[google.protobuf.Timestamp](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto) | ||

### ConfigMapQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query) |❌ ||
| 2 | name |string |❌ ||
| 3 | domain_id |string |✅ ||

### ConfigMapRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | name |string |✅ ||
| 2 | domain_id |string |✅ ||

### ConfigMapStatQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query) |✅ ||
| 2 | domain_id |string |✅ ||

### ConfigMapsInfo
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | results |[ConfigMapInfo](Config-map.md#configmapinfo) | ||
| 2 | total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | ||

### CreateConfigMapRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | name |string |✅ ||
| 2 | data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |✅ ||
| 3 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |❌ ||
| 4 | domain_id |string |✅ ||

### GetConfigMapRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | name |string |✅ ||
| 2 | domain_id |string |✅ ||
| 3 | only |string |❌ ||

### UpdateConfigMapRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | name |string |✅ ||
| 2 | data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |❌ ||
| 3 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |❌ ||
| 4 | domain_id |string |✅ ||
