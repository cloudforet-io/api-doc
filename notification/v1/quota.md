---
description:  
---
# Quota

>  **Package : spaceone.api.notification.v1**

## Quota

{% hint style="info" %}
**Quota Methods:**

{%  endhint %}


| NO |  Method | Request Type | Response Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [**create**](quota.md#create)|   [CreateQuotaRequest](quota.md#createquotarequest) |   [QuotaInfo](quota.md#quotainfo) | Creates a new Quota for Protocol. |
| 2 | [**update**](quota.md#update)|   [UpdateQuotaRequest](quota.md#updatequotarequest) |   [QuotaInfo](quota.md#quotainfo) | Updates a exist Quota information. |
| 3 | [**delete**](quota.md#delete)|   [QuotaRequest](quota.md#quotarequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)| Delete the Quota. |
| 4 | [**get**](quota.md#get)|   [QuotaRequest](quota.md#quotarequest) |   [QuotaInfo](quota.md#quotainfo) | Gets a single Quota information. |
| 5 | [**list**](quota.md#list)|   [QuotaQuery](quota.md#quotaquery) |   [QuotasInfo](quota.md#quotasinfo) | Lists the specified Quota information.Can search information using the query format provided by SpaceONE.Detailed information about Query format can be checked in the Search Query pages. |
| 6 | [**stat**](quota.md#stat)|   [QuotaStatQuery](quota.md#quotastatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  | 
 

 
### create
> **POST** /notification/v1/quotas
>

> Creates a new Quota for Protocol.

| Type | Message |
| :--- | :--- |
| Request | [CreateQuotaRequest](quota.md#createquotarequest) |
| Response |  [QuotaInfo](quota.md#quotainfo)  |
 
 

 
### update
> **PUT** /notification/v1/quota/{quota_id}
>

> Updates a exist Quota information.

| Type | Message |
| :--- | :--- |
| Request | [UpdateQuotaRequest](quota.md#updatequotarequest) |
| Response |  [QuotaInfo](quota.md#quotainfo)  |
 
 

 
### delete
> **DELETE** /notification/v1/quota/{quota_id}
>

> Delete the Quota.

| Type | Message |
| :--- | :--- |
| Request | [QuotaRequest](quota.md#quotarequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
 
 

 
### get
> **GET** /notification/v1/quota/{quota_id}
>

> Gets a single Quota information.

| Type | Message |
| :--- | :--- |
| Request | [QuotaRequest](quota.md#quotarequest) |
| Response |  [QuotaInfo](quota.md#quotainfo)  |
 
 

 
### list
> **GET** /notification/v1/quotas
>
> **POST** /notification/v1/quotas/search


> Lists the specified Quota information.Can search information using the query format provided by SpaceONE.Detailed information about Query format can be checked in the Search Query pages.

| Type | Message |
| :--- | :--- |
| Request | [QuotaQuery](quota.md#quotaquery) |
| Response |  [QuotasInfo](quota.md#quotasinfo)  |
 
 

 
### stat
> **POST** /notification/v1/quotas/stat
>


| Type | Message |
| :--- | :--- |
| Request | [QuotaStatQuery](quota.md#quotastatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |


## 

## Message

### CreateQuotaRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :---: | :--- |
| 1 | protocol_id |string|✅| |
| 2 | limit |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✅| The information about Quota limitation.|
| 3 | domain_id |string|✅| The ID of domain.|

### QuotaInfo
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | quota_id |string | The ID of Quota.|
| 2 | protocol_id |string | The ID of Protocol.|
| 3 | limit |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | The information about Quota limitation.|
| 4 | domain_id |string | The ID of domain|

### QuotaQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :---: | :--- |
| 1 | query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query)|❌| Query format provided by SpaceONE. Please check the link for more information.|
| 2 | quota_id |string|❌| The ID of Quota.|
| 3 | protocol_id |string|❌| The ID of Protocol.|
| 4 | domain_id |string|✅| The ID of domain.|

### QuotaRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :---: | :--- |
| 1 | quota_id |string|✅| The ID of Quota.|
| 2 | domain_id |string|✅| The ID of domain.|

### QuotaStatQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :---: | :--- |
| 1 | query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✅| Statistics Query format provided by SpaceONE. Please check the link for more information.|
| 2 | domain_id |string|✅| The ID of domain.|

### QuotasInfo
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | results |[list of QuotaInfo](quota.md#quotainfo) | List of queried Quota.|
| 2 | total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | Total counts of queried Quota.|

### UpdateQuotaRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :---: | :--- |
| 1 | quota_id |string|✅| The ID of Quota.|
| 2 | limit |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✅| The information about Quota limitation.|
| 3 | domain_id |string|✅| |
