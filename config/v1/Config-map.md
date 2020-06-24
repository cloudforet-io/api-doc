---
description: Config Map is a APIs for public config setting that store any configuration values for accounts, companies, etc.
---
# Config map

>  **Package : spaceone.api.config.v1**

## ConfigMap

{% hint style="info" %}
**ConfigMap Methods:**
desc: Config Map service Methods
note: (if there's anything that you want to point out
{%  endhint %}


| NO |  Method | Request Type | Response Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [create](Config-map.md#create)| [CreateConfigMapRequest](Config-map.md#createconfigmaprequest)| [ConfigMapInfo](Config-map.md#configmapinfo) |  |
| 2 | [update](Config-map.md#update)| [UpdateConfigMapRequest](Config-map.md#updateconfigmaprequest)| [ConfigMapInfo](Config-map.md#configmapinfo) |  |
| 3 | [delete](Config-map.md#delete)| [ConfigMapRequest](Config-map.md#configmaprequest)|[google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| 4 | [get](Config-map.md#get)| [GetConfigMapRequest](Config-map.md#getconfigmaprequest)| [ConfigMapInfo](Config-map.md#configmapinfo) |  |
| 5 | [list](Config-map.md#list)| [ConfigMapQuery](Config-map.md#configmapquery)| [ConfigMapsInfo](Config-map.md#configmapsinfo) |  |
| 6 | [stat](Config-map.md#stat)| [ConfigMapStatQuery](Config-map.md#configmapstatquery)|[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  |

### create
> **POST** /config/v1/config-maps
>

> Create a new config map


| Type | Message |
| :--- | :--- |
| Request | [CreateConfigMapRequest](Config-map.md#createconfigmaprequest) |
| Response |  [ConfigMapInfo](Config-map.md#configmapinfo)  |


{% tabs %}
{% tab title="Request Example" %}
```text
{
    "query": {
        "aggregate": {
            "group": {
                "keys": [
                    {
                        "key": "group",
                        "name": "group Name"
                    }
                ],
                "fields": [
                    {
                        "operator": "count",
                        "name": "ppl count in group"
                    },
                    {
                        "key": "name",
                        "operator": "add_to_set",
                        "name": "names in  group"
                    }
                ]
            }
        },
        "sort": {
            "name": "created_at",
            "desc": true
        },
        "limit": 5
    }
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "query": {
        "aggregate": {
            "group": {
                "keys": [
                    {
                        "key": "group",
                        "name": "group Name"
                    }
                ],
                "fields": [
                    {
                        "operator": "count",
                        "name": "ppl count in group"
                    },
                    {
                        "key": "name",
                        "operator": "add_to_set",
                        "name": "names in  group"
                    }
                ]
            }
        },
        "sort": {
            "name": "created_at",
            "desc": true
        },
        "limit": 5
    }
}
```
{% endtab %}
{% endtabs %}


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
| 1 | query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query) | |optional|
| 2 | name |string | |optional|
| 3 | domain_id |string | |required|

### ConfigMapRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | name |string | |required|
| 2 | domain_id |string | |required|

### ConfigMapStatQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query) | |required|
| 2 | domain_id |string | |required|

### ConfigMapsInfo
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | results |[ConfigMapInfo](Config-map.md#configmapinfo) | ||
| 2 | total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | ||

### CreateConfigMapRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | name |string |✅ |any info that you want to put on descriptions|
| 2 | data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |✅ ||
| 3 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |❌ ||
| 4 | domain_id |string |✅ ||

### GetConfigMapRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | name |string | |required|
| 2 | domain_id |string | |required|
| 3 | only |string | |optional|

### UpdateConfigMapRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | name |string |✅ ||
| 2 | data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | ||
| 3 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |❌ ||
| 4 | domain_id |string |✅ ||
