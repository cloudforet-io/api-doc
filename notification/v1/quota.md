---
description:  
---
# Quota

>  **Package : spaceone.api.notification.v1**

## Quota

{% hint style="info" %}
**Quota Methods:**

{%  endhint %}


| Method | Request | Response | Description &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; |
| :-----: | :--------: | :--------: | :-------------------- |
| [**create**](quota.md#create)|   [CreateQuotaRequest](quota.md#createquotarequest) |   [QuotaInfo](quota.md#quotainfo) | Creates a new Quota for Protocol. |
| [**update**](quota.md#update)|   [UpdateQuotaRequest](quota.md#updatequotarequest) |   [QuotaInfo](quota.md#quotainfo) | Updates a exist Quota information. |
| [**delete**](quota.md#delete)|   [QuotaRequest](quota.md#quotarequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)| Delete the Quota. |
| [**get**](quota.md#get)|   [QuotaRequest](quota.md#quotarequest) |   [QuotaInfo](quota.md#quotainfo) | Gets a single Quota information. |
| [**list**](quota.md#list)|   [QuotaQuery](quota.md#quotaquery) |   [QuotasInfo](quota.md#quotasinfo) | Lists the specified Quota information.Can search information using the query format provided by SpaceONE.Detailed information about Query format can be checked in the Search Query pages. |
| [**stat**](quota.md#stat)|   [QuotaStatQuery](quota.md#quotastatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  |TEST

| Method | Request | Response | Description &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; |
| :-----: | :--------: | :--------: | :-------------------- |
|<div style="width:70px; text-align:center;">  [**create**](quota.md#create) </div> | <div style="width:200px; text-align:center;">    [CreateQuotaRequest](quota.md#createquotarequest)  </div> | <div style="width:200px; text-align:center;">   [QuotaInfo](quota.md#quotainfo)  </div> | <div style="width:400px;"> Creates a new Quota for Protocol. </div> |
|<div style="width:70px; text-align:center;">  [**update**](quota.md#update) </div> | <div style="width:200px; text-align:center;">    [UpdateQuotaRequest](quota.md#updatequotarequest)  </div> | <div style="width:200px; text-align:center;">   [QuotaInfo](quota.md#quotainfo)  </div> | <div style="width:400px;"> Updates a exist Quota information. </div> |
|<div style="width:70px; text-align:center;">  [**delete**](quota.md#delete) </div> | <div style="width:200px; text-align:center;">    [QuotaRequest](quota.md#quotarequest)  </div> | <div style="width:200px; text-align:center;">  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) </div> | <div style="width:400px;"> Delete the Quota. </div> |
|<div style="width:70px; text-align:center;">  [**get**](quota.md#get) </div> | <div style="width:200px; text-align:center;">    [QuotaRequest](quota.md#quotarequest)  </div> | <div style="width:200px; text-align:center;">   [QuotaInfo](quota.md#quotainfo)  </div> | <div style="width:400px;"> Gets a single Quota information. </div> |
|<div style="width:70px; text-align:center;">  [**list**](quota.md#list) </div> | <div style="width:200px; text-align:center;">    [QuotaQuery](quota.md#quotaquery)  </div> | <div style="width:200px; text-align:center;">   [QuotasInfo](quota.md#quotasinfo)  </div> | <div style="width:400px;"> Lists the specified Quota information.Can search information using the query format provided by SpaceONE.Detailed information about Query format can be checked in the Search Query pages. </div> |
|<div style="width:70px; text-align:center;">  [**stat**](quota.md#stat) </div> | <div style="width:200px; text-align:center;">    [QuotaStatQuery](quota.md#quotastatquery)  </div> | <div style="width:200px; text-align:center;">  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) </div> | <div style="width:400px;">  </div> | 
 

 
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
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| protocol_id |string|✅| |
| limit |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✅| The information about Quota limitation.|
| domain_id |string|✅| The ID of domain.|

### QuotaInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| quota_id |string | The ID of Quota.|
| protocol_id |string | The ID of Protocol.|
| limit |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | The information about Quota limitation.|
| domain_id |string | The ID of domain|

### QuotaQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query)|❌| Query format provided by SpaceONE. Please check the link for more information.|
| quota_id |string|❌| The ID of Quota.|
| protocol_id |string|❌| The ID of Protocol.|
| domain_id |string|✅| The ID of domain.|

### QuotaRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| quota_id |string|✅| The ID of Quota.|
| domain_id |string|✅| The ID of domain.|

### QuotaStatQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✅| Statistics Query format provided by SpaceONE. Please check the link for more information.|
| domain_id |string|✅| The ID of domain.|

### QuotasInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| results |[list of QuotaInfo](quota.md#quotainfo) | List of queried Quota.|
| total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | Total counts of queried Quota.|

### UpdateQuotaRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| quota_id |string|✅| The ID of Quota.|
| limit |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✅| The information about Quota limitation.|
| domain_id |string|✅| |
