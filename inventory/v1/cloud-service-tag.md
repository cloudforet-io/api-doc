---
description:  
---
# Cloud service tag

>  **Package : spaceone.api.inventory.v1**

## CloudServiceTag

{% hint style="info" %}
**CloudServiceTag Methods:**

{%  endhint %}


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**list**](cloud-service-tag.md#list)|   [CloudServiceTagQuery](cloud-service-tag.md#cloudservicetagquery) |   [CloudServiceTagsInfo](cloud-service-tag.md#cloudservicetagsinfo) |
| [**stat**](cloud-service-tag.md#stat)|   [CloudServiceTagStatQuery](cloud-service-tag.md#cloudservicetagstatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)| 
 

 
### list
> **GET** /inventory/v1/cloud-service-tags
>
> **POST** /inventory/v1/cloud-service-tags/search



| Type | Message |
| :--- | :--- |
| Request | [CloudServiceTagQuery](cloud-service-tag.md#cloudservicetagquery) |
| Response |  [CloudServiceTagsInfo](cloud-service-tag.md#cloudservicetagsinfo)  |
 
 

 
### stat
> **POST** /inventory/v1/cloud-service-tags/stat
>


| Type | Message |
| :--- | :--- |
| Request | [CloudServiceTagStatQuery](cloud-service-tag.md#cloudservicetagstatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |


## 

## Message

### CloudServiceTagInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| tag_id |string | |
| cloud_service_id |string | |
| key |string | |
| value |string | |
| provider |string | |
| project_id |string | |
| domain_id |string | |
| created_at |string | |

### CloudServiceTagQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query)|✘| |
| cloud_service_id |string|✘| |
| key |string|✘| |
| provider |string|✘| |
| project_id |string|✘| |
| domain_id |string|✔| |

### CloudServiceTagStatQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✔| |
| domain_id |string|✔| |

### CloudServiceTagsInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| results |[list of CloudServiceTagInfo](cloud-service-tag.md#cloudservicetaginfo) | |
| total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |
