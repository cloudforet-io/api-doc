---
description:  
---
# Cost query set

>  **Package : spaceone.api.cost_analysis.v1**

## CostQuerySet

{% hint style="info" %}
**CostQuerySet Methods:**

{%  endhint %}


| Method | Request | Response | Description |
| :-----: | :--------: | :--------: | :-------------------- |
| [**create**](cost-query-set.md#create)|   [CreateCostQuerySetRequest](cost-query-set.md#createcostquerysetrequest) |   [CostQuerySetInfo](cost-query-set.md#costquerysetinfo) |  |
| [**update**](cost-query-set.md#update)|   [UpdateCostQuerySetRequest](cost-query-set.md#updatecostquerysetrequest) |   [CostQuerySetInfo](cost-query-set.md#costquerysetinfo) |  |
| [**delete**](cost-query-set.md#delete)|   [CostQuerySetRequest](cost-query-set.md#costquerysetrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| [**get**](cost-query-set.md#get)|   [GetCostQuerySetRequest](cost-query-set.md#getcostquerysetrequest) |   [CostQuerySetInfo](cost-query-set.md#costquerysetinfo) |  |
| [**list**](cost-query-set.md#list)|   [CostQuerySetQuery](cost-query-set.md#costquerysetquery) |   [CostQuerySetsInfo](cost-query-set.md#costquerysetsinfo) |  |
| [**stat**](cost-query-set.md#stat)|   [CostQuerySetStatQuery](cost-query-set.md#costquerysetstatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  |TEST

<table style="border-collapse: collapse; text-align: left; line-height: 1.5;">
    <thead>
    <tr>
      <th scope="cols" style="padding: 10px; font-weight: bold; vertical-align: top; color: #369; border-bottom: 3px solid #036;">Method</th>
      <th scope="cols" style="padding: 10px; font-weight: bold; vertical-align: top; color: #369; border-bottom: 3px solid #036;">Request</th>
      <th scope="cols" style="padding: 10px; font-weight: bold; vertical-align: top; color: #369; border-bottom: 3px solid #036;">Response</th>
      <th scope="cols" style="padding: 10px; font-weight: bold; vertical-align: top; color: #369; border-bottom: 3px solid #036;">Description</th>
    </tr>
    </thead>
    <tbody>
    <tr>
      <th scope="row" style="width: 80px; padding: 10px; font-weight: bold; vertical-align: top; border-bottom: 1px solid #ccc;">create</th>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   CreateCostQuerySetRequest </td>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   CostQuerySetInfo </td>
      <td style="width: 400px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;"></td>
    </tr>
    <tr>
      <th scope="row" style="width: 80px; padding: 10px; font-weight: bold; vertical-align: top; border-bottom: 1px solid #ccc;">update</th>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   UpdateCostQuerySetRequest </td>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   CostQuerySetInfo </td>
      <td style="width: 400px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;"></td>
    </tr>
    <tr>
      <th scope="row" style="width: 80px; padding: 10px; font-weight: bold; vertical-align: top; border-bottom: 1px solid #ccc;">delete</th>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   CostQuerySetRequest </td>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   google.protobuf.Empty </td>
      <td style="width: 400px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;"></td>
    </tr>
    <tr>
      <th scope="row" style="width: 80px; padding: 10px; font-weight: bold; vertical-align: top; border-bottom: 1px solid #ccc;">get</th>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   GetCostQuerySetRequest </td>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   CostQuerySetInfo </td>
      <td style="width: 400px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;"></td>
    </tr>
    <tr>
      <th scope="row" style="width: 80px; padding: 10px; font-weight: bold; vertical-align: top; border-bottom: 1px solid #ccc;">list</th>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   CostQuerySetQuery </td>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   CostQuerySetsInfo </td>
      <td style="width: 400px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;"></td>
    </tr>
    <tr>
      <th scope="row" style="width: 80px; padding: 10px; font-weight: bold; vertical-align: top; border-bottom: 1px solid #ccc;">stat</th>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   CostQuerySetStatQuery </td>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   google.protobuf.Struct </td>
      <td style="width: 400px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;"></td>
    </tr></tbody>
</table> 
 

 
### create
> **POST** /cost-analysis/v1/cost-query-sets
>


| Type | Message |
| :--- | :--- |
| Request | [CreateCostQuerySetRequest](cost-query-set.md#createcostquerysetrequest) |
| Response |  [CostQuerySetInfo](cost-query-set.md#costquerysetinfo)  |
 
 

 
### update
> **PUT** /cost-analysis/v1/cost-query-set/{cost_query_set_id}
>


| Type | Message |
| :--- | :--- |
| Request | [UpdateCostQuerySetRequest](cost-query-set.md#updatecostquerysetrequest) |
| Response |  [CostQuerySetInfo](cost-query-set.md#costquerysetinfo)  |
 
 

 
### delete
> **DELETE** /cost-analysis/v1/cost-query-set/{cost_query_set_id}
>


| Type | Message |
| :--- | :--- |
| Request | [CostQuerySetRequest](cost-query-set.md#costquerysetrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
 
 

 
### get
> **GET** /cost-analysis/v1/cost-query-set/{cost_query_set_id}
>


| Type | Message |
| :--- | :--- |
| Request | [GetCostQuerySetRequest](cost-query-set.md#getcostquerysetrequest) |
| Response |  [CostQuerySetInfo](cost-query-set.md#costquerysetinfo)  |
 
 

 
### list
> **GET** /cost-analysis/v1/cost-query-sets
>
> **POST** /cost-analysis/v1/cost-query-sets/search



| Type | Message |
| :--- | :--- |
| Request | [CostQuerySetQuery](cost-query-set.md#costquerysetquery) |
| Response |  [CostQuerySetsInfo](cost-query-set.md#costquerysetsinfo)  |
 
 

 
### stat
> **POST** /cost-analysis/v1/cost-query-sets/stat
>


| Type | Message |
| :--- | :--- |
| Request | [CostQuerySetStatQuery](cost-query-set.md#costquerysetstatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |


## 

## Message

### CostQuerySetInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| cost_query_set_id |string | |
| name |string | |
| options |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| user_id |string | |
| domain_id |string | |
| created_at |string | |
| updated_at |string | |

### CostQuerySetQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query)|❌| |
| cost_query_set_id |string|❌| |
| name |string|❌| |
| user_id |string|❌| |
| domain_id |string|✅| |

### CostQuerySetRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| cost_query_set_id |string|✅| |
| domain_id |string|✅| |

### CostQuerySetStatQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✅| |
| domain_id |string|✅| |

### CostQuerySetsInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| results |[list of CostQuerySetInfo](cost-query-set.md#costquerysetinfo) | |
| total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### CreateCostQuerySetRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| name |string|✅| |
| options |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✅| |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| domain_id |string|✅| |

### GetCostQuerySetRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| cost_query_set_id |string|✅| |
| domain_id |string|✅| |
| only |list of string|❌| |

### UpdateCostQuerySetRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| cost_query_set_id |string|✅| |
| name |string|❌| |
| options |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| domain_id |string|✅| |
