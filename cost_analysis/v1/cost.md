---
description:  
---
# Cost

>  **Package : spaceone.api.cost_analysis.v1**

## Cost

{% hint style="info" %}
**Cost Methods:**

{%  endhint %}


| NO |  Method | Request Type | Response Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [**create**](cost.md#create)|   [CreateCostRequest](cost.md#createcostrequest) |   [CostInfo](cost.md#costinfo) |  |
| 2 | [**delete**](cost.md#delete)|   [CostRequest](cost.md#costrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| 3 | [**get**](cost.md#get)|   [GetCostRequest](cost.md#getcostrequest) |   [CostInfo](cost.md#costinfo) |  |
| 4 | [**list**](cost.md#list)|   [CostQuery](cost.md#costquery) |   [CostsInfo](cost.md#costsinfo) |  |
| 5 | [**stat**](cost.md#stat)|   [CostStatQuery](cost.md#coststatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  | 
 

 
### create
> **POST** /cost-analysis/v1/costs
>


| Type | Message |
| :--- | :--- |
| Request | [CreateCostRequest](cost.md#createcostrequest) |
| Response |  [CostInfo](cost.md#costinfo)  |
 
 

 
### delete
> **DELETE** /cost-analysis/v1/cost/{cost_id}
>


| Type | Message |
| :--- | :--- |
| Request | [CostRequest](cost.md#costrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
 
 

 
### get
> **GET** /cost-analysis/v1/cost/{cost_id}
>


| Type | Message |
| :--- | :--- |
| Request | [GetCostRequest](cost.md#getcostrequest) |
| Response |  [CostInfo](cost.md#costinfo)  |
 
 

 
### list
> **GET** /cost-analysis/v1/costs
>
> **POST** /cost-analysis/v1/costs/search



| Type | Message |
| :--- | :--- |
| Request | [CostQuery](cost.md#costquery) |
| Response |  [CostsInfo](cost.md#costsinfo)  |
 
 

 
### stat
> **POST** /cost-analysis/v1/costs/stat
>


| Type | Message |
| :--- | :--- |
| Request | [CostStatQuery](cost.md#coststatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |


## 

## Message

### CostInfo
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | cost_id |string | |
| 2 | cost_key |string | |
| 3 | usd_cost |float | |
| 4 | original_currency |string | |
| 5 | original_cost |float | |
| 6 | usage_quantity |float | |
| 7 | provider |string | |
| 8 | region_code |string | |
| 9 | product |string | |
| 10 | account |string | |
| 11 | type |string | |
| 12 | resource_group |string | |
| 13 | resource |string | |
| 14 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| 15 | additional_info |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| 16 | service_account_id |string | |
| 17 | project_id |string | |
| 18 | data_source_id |string | |
| 19 | domain_id |string | |
| 20 | billed_at |string | |
| 21 | created_at |string | |

### CostQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :---: | :--- |
| 1 | query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query)|❌| |
| 2 | cost_id |string|❌| |
| 3 | cost_key |string|❌| |
| 4 | original_currency |string|❌| |
| 5 | provider |string|❌| |
| 6 | region_code |string|❌| |
| 7 | product |string|❌| |
| 8 | account |string|❌| |
| 9 | type |string|❌| |
| 10 | resource_group |string|❌| |
| 11 | resource |string|❌| |
| 12 | service_account_id |string|❌| |
| 13 | project_id |string|❌| |
| 14 | data_source_id |string|❌| |
| 15 | domain_id |string|✅| |

### CostRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :---: | :--- |
| 1 | cost_id |string|✅| |
| 2 | domain_id |string|✅| |

### CostStatQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :---: | :--- |
| 1 | query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✅| |
| 2 | domain_id |string|✅| |

### CostsInfo
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | results |[list of CostInfo](cost.md#costinfo) | |
| 2 | total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### CreateCostRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :---: | :--- |
| 1 | original_cost |float|✅| |
| 2 | original_currency |string|✅| |
| 3 | usage_quantity |float|❌| |
| 4 | provider |string|❌| |
| 5 | region_code |string|❌| |
| 6 | product |string|❌| |
| 7 | account |string|❌| |
| 8 | type |string|❌| |
| 9 | resource_group |string|❌| |
| 10 | resource |string|❌| |
| 11 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| 12 | additional_info |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| 13 | service_account_id |string|❌| |
| 14 | project_id |string|✅| |
| 15 | data_source_id |string|✅| |
| 16 | domain_id |string|✅| |
| 17 | billed_at |string|❌| |
| 18 | created_at |string|❌| |

### GetCostRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :---: | :--- |
| 1 | cost_id |string|✅| |
| 2 | domain_id |string|✅| |
| 3 | only |list of string|❌| |
