---
description: Config Map API which configure environments for account
---

# Config Map

> **Package : spaceone.api.config.v1**

## ConfigMap

{% hint style="info" %}
**ConfigMap Methods:**
{% endhint %}

| NO | Method | Request Type | Response Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [create](https://github.com/spaceone-dev/api-doc/tree/709a9f739008ac01f9038b4950fc11b1f3d05742/config/v1/Config-map.md#create) | [CreateConfigMapRequest](https://github.com/spaceone-dev/api-doc/tree/709a9f739008ac01f9038b4950fc11b1f3d05742/config/v1/Config-map.md#createconfigmaprequest) | [ConfigMapInfo](https://github.com/spaceone-dev/api-doc/tree/709a9f739008ac01f9038b4950fc11b1f3d05742/config/v1/Config-map.md#configmapinfo) |  |
| 2 | [update](https://github.com/spaceone-dev/api-doc/tree/709a9f739008ac01f9038b4950fc11b1f3d05742/config/v1/Config-map.md#update) | [UpdateConfigMapRequest](https://github.com/spaceone-dev/api-doc/tree/709a9f739008ac01f9038b4950fc11b1f3d05742/config/v1/Config-map.md#updateconfigmaprequest) | [ConfigMapInfo](https://github.com/spaceone-dev/api-doc/tree/709a9f739008ac01f9038b4950fc11b1f3d05742/config/v1/Config-map.md#configmapinfo) |  |
| 3 | [delete](https://github.com/spaceone-dev/api-doc/tree/709a9f739008ac01f9038b4950fc11b1f3d05742/config/v1/Config-map.md#delete) | [ConfigMapRequest](https://github.com/spaceone-dev/api-doc/tree/709a9f739008ac01f9038b4950fc11b1f3d05742/config/v1/Config-map.md#configmaprequest) | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |  |
| 4 | [get](https://github.com/spaceone-dev/api-doc/tree/709a9f739008ac01f9038b4950fc11b1f3d05742/config/v1/Config-map.md#get) | [GetConfigMapRequest](https://github.com/spaceone-dev/api-doc/tree/709a9f739008ac01f9038b4950fc11b1f3d05742/config/v1/Config-map.md#getconfigmaprequest) | [ConfigMapInfo](https://github.com/spaceone-dev/api-doc/tree/709a9f739008ac01f9038b4950fc11b1f3d05742/config/v1/Config-map.md#configmapinfo) |  |
| 5 | [list](https://github.com/spaceone-dev/api-doc/tree/709a9f739008ac01f9038b4950fc11b1f3d05742/config/v1/Config-map.md#list) | [ConfigMapQuery](https://github.com/spaceone-dev/api-doc/tree/709a9f739008ac01f9038b4950fc11b1f3d05742/config/v1/Config-map.md#configmapquery) | [ConfigMapsInfo](https://github.com/spaceone-dev/api-doc/tree/709a9f739008ac01f9038b4950fc11b1f3d05742/config/v1/Config-map.md#configmapsinfo) |  |
| 6 | [stat](https://github.com/spaceone-dev/api-doc/tree/709a9f739008ac01f9038b4950fc11b1f3d05742/config/v1/Config-map.md#stat) | [ConfigMapStatQuery](https://github.com/spaceone-dev/api-doc/tree/709a9f739008ac01f9038b4950fc11b1f3d05742/config/v1/Config-map.md#configmapstatquery) | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |  |

### 

### create

> **POST** /config/v1/config-maps

| Type | Message |
| :--- | :--- |
| Request | [CreateConfigMapRequest](https://github.com/spaceone-dev/api-doc/tree/709a9f739008ac01f9038b4950fc11b1f3d05742/config/v1/Config-map.md#createconfigmaprequest) |
| Response | [ConfigMapInfo](https://github.com/spaceone-dev/api-doc/tree/709a9f739008ac01f9038b4950fc11b1f3d05742/config/v1/Config-map.md#configmapinfo) |

### 

### update

> **PUT** /config/v1/config-map/{name}

| Type | Message |
| :--- | :--- |
| Request | [UpdateConfigMapRequest](https://github.com/spaceone-dev/api-doc/tree/709a9f739008ac01f9038b4950fc11b1f3d05742/config/v1/Config-map.md#updateconfigmaprequest) |
| Response | [ConfigMapInfo](https://github.com/spaceone-dev/api-doc/tree/709a9f739008ac01f9038b4950fc11b1f3d05742/config/v1/Config-map.md#configmapinfo) |

### 

### delete

> **DELETE** /config/v1/config-map/{name}

| Type | Message |
| :--- | :--- |
| Request | [ConfigMapRequest](https://github.com/spaceone-dev/api-doc/tree/709a9f739008ac01f9038b4950fc11b1f3d05742/config/v1/Config-map.md#configmaprequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |

### 

### get

> **GET** /config/v1/config-map/{name}

| Type | Message |
| :--- | :--- |
| Request | [GetConfigMapRequest](https://github.com/spaceone-dev/api-doc/tree/709a9f739008ac01f9038b4950fc11b1f3d05742/config/v1/Config-map.md#getconfigmaprequest) |
| Response | [ConfigMapInfo](https://github.com/spaceone-dev/api-doc/tree/709a9f739008ac01f9038b4950fc11b1f3d05742/config/v1/Config-map.md#configmapinfo) |

### 

### list

> **GET** /config/v1/config-maps
>
> **POST** /config/v1/config-maps/search

| Type | Message |
| :--- | :--- |
| Request | [ConfigMapQuery](https://github.com/spaceone-dev/api-doc/tree/709a9f739008ac01f9038b4950fc11b1f3d05742/config/v1/Config-map.md#configmapquery) |
| Response | [ConfigMapsInfo](https://github.com/spaceone-dev/api-doc/tree/709a9f739008ac01f9038b4950fc11b1f3d05742/config/v1/Config-map.md#configmapsinfo) |

### 

### stat

> **POST** /config/v1/config-maps/stat

| Type | Message |
| :--- | :--- |
| Request | [ConfigMapStatQuery](https://github.com/spaceone-dev/api-doc/tree/709a9f739008ac01f9038b4950fc11b1f3d05742/config/v1/Config-map.md#configmapstatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |

## 

## Message

### ConfigMapInfo

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | name | string |  |  |
| 2 | data | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |  |  |
| 3 | tags | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |  |  |
| 4 | domain\_id | string |  |  |
| 5 | created\_at | [google.protobuf.Timestamp](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto) |  |  |

### 

### ConfigMapQuery

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query | [spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query) | ❌ |  |
| 2 | name | string | ❌ |  |
| 3 | domain\_id | string | ✅ |  |

### 

### ConfigMapRequest

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | name | string | ✅ |  |
| 2 | domain\_id | string | ✅ |  |

### 

### ConfigMapStatQuery

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query | [spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query) | ✅ |  |
| 2 | domain\_id | string | ✅ |  |

### 

### ConfigMapsInfo

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | results | [ConfigMapInfo](https://github.com/spaceone-dev/api-doc/tree/709a9f739008ac01f9038b4950fc11b1f3d05742/config/v1/Config-map.md#configmapinfo) |  |  |
| 2 | total\_count | [int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) |  |  |

### 

### CreateConfigMapRequest

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | name | string | ✅ |  |
| 2 | data | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | ✅ |  |
| 3 | tags | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | ❌ |  |
| 4 | domain\_id | string | ✅ |  |

### 

### GetConfigMapRequest

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | name | string | ✅ |  |
| 2 | domain\_id | string | ✅ |  |
| 3 | only | string | ❌ |  |

### 

### UpdateConfigMapRequest

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | name | string | ✅ |  |
| 2 | data | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | ❌ |  |
| 3 | tags | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | ❌ |  |
| 4 | domain\_id | string | ✅ |  |

