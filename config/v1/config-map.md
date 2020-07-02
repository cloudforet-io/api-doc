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
| 1 | [create](config-map.md#create) | [CreateConfigMapRequest](config-map.md#createconfigmaprequest) | [ConfigMapInfo](config-map.md#configmapinfo) |  |
| 2 | [update](config-map.md#update) | [UpdateConfigMapRequest](config-map.md#updateconfigmaprequest) | [ConfigMapInfo](config-map.md#configmapinfo) |  |
| 3 | [delete](config-map.md#delete) | [ConfigMapRequest](config-map.md#configmaprequest) | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |  |
| 4 | [get](config-map.md#get) | [GetConfigMapRequest](config-map.md#getconfigmaprequest) | [ConfigMapInfo](config-map.md#configmapinfo) |  |
| 5 | [list](config-map.md#list) | [ConfigMapQuery](config-map.md#configmapquery) | [ConfigMapsInfo](config-map.md#configmapsinfo) |  |
| 6 | [stat](config-map.md#stat) | [ConfigMapStatQuery](config-map.md#configmapstatquery) | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |  |

### create

> **POST** /config/v1/config-maps

| Type | Message |
| :--- | :--- |
| Request | [CreateConfigMapRequest](config-map.md#createconfigmaprequest) |
| Response | [ConfigMapInfo](config-map.md#configmapinfo) |

### update

> **PUT** /config/v1/config-map/{name}

| Type | Message |
| :--- | :--- |
| Request | [UpdateConfigMapRequest](config-map.md#updateconfigmaprequest) |
| Response | [ConfigMapInfo](config-map.md#configmapinfo) |

### delete

> **DELETE** /config/v1/config-map/{name}

| Type | Message |
| :--- | :--- |
| Request | [ConfigMapRequest](config-map.md#configmaprequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |

### get

> **GET** /config/v1/config-map/{name}

| Type | Message |
| :--- | :--- |
| Request | [GetConfigMapRequest](config-map.md#getconfigmaprequest) |
| Response | [ConfigMapInfo](config-map.md#configmapinfo) |

### list

> **GET** /config/v1/config-maps
>
> **POST** /config/v1/config-maps/search

| Type | Message |
| :--- | :--- |
| Request | [ConfigMapQuery](config-map.md#configmapquery) |
| Response | [ConfigMapsInfo](config-map.md#configmapsinfo) |

### stat

> **POST** /config/v1/config-maps/stat

| Type | Message |
| :--- | :--- |
| Request | [ConfigMapStatQuery](config-map.md#configmapstatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |

## Message

### ConfigMapInfo

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | name | string |  |  |
| 2 | data | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |  |  |
| 3 | tags | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |  |  |
| 4 | domain\_id | string |  |  |
| 5 | created\_at | [google.protobuf.Timestamp](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto) |  |  |

### ConfigMapQuery

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query | [spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query) | ❌ |  |
| 2 | name | string | ❌ |  |
| 3 | domain\_id | string | ✅ |  |

### ConfigMapRequest

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | name | string | ✅ |  |
| 2 | domain\_id | string | ✅ |  |

### ConfigMapStatQuery

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query | [spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query) | ✅ |  |
| 2 | domain\_id | string | ✅ |  |

### ConfigMapsInfo

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | results | [ConfigMapInfo](config-map.md#configmapinfo) |  |  |
| 2 | total\_count | [int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) |  |  |

### CreateConfigMapRequest

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | name | string | ✅ |  |
| 2 | data | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | ✅ |  |
| 3 | tags | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | ❌ |  |
| 4 | domain\_id | string | ✅ |  |

### GetConfigMapRequest

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | name | string | ✅ |  |
| 2 | domain\_id | string | ✅ |  |
| 3 | only | string | ❌ |  |

### UpdateConfigMapRequest

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | name | string | ✅ |  |
| 2 | data | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | ❌ |  |
| 3 | tags | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | ❌ |  |
| 4 | domain\_id | string | ✅ |  |

