---
description:  
---
# Statistic

>  **Package : spaceone.api.cost_saving.v1**

## Statistic

{% hint style="info" %}
**Statistic Methods:**

{%  endhint %}


| NO |  Method | Request Type | Response Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [**list**](statistic.md#list)|   [StatisticQuery](statistic.md#statisticquery) |   [StatisticsInfo](statistic.md#statisticsinfo) |  |
| 2 | [**stat**](statistic.md#stat)|   [StatisticStatQuery](statistic.md#statisticstatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  | 
 

 
### list
> **GET** /cost-saving/v1/statistics
>
> **POST** /cost-saving/v1/statistics/search



| Type | Message |
| :--- | :--- |
| Request | [StatisticQuery](statistic.md#statisticquery) |
| Response |  [StatisticsInfo](statistic.md#statisticsinfo)  |
 
 

 
### stat
> **POST** /cost-saving/v1/statistics/stat
>


| Type | Message |
| :--- | :--- |
| Request | [StatisticStatQuery](statistic.md#statisticstatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |


## 

## Message

### StatisticInfo
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | cost_saving_stat_id |string | |
| 2 | domain_id |string | |
| 3 | project_id |string | |
| 4 | saving_by |string | |
| 5 | environment |string | |
| 6 | provider |string | |
| 7 | region |string | |
| 8 | resource_type |string | |
| 9 | cost |float | |
| 10 | created_at |[google.protobuf.Timestamp](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto) | |
| 11 | update_at |[google.protobuf.Timestamp](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto) | |
| 12 | expired_at |[google.protobuf.Timestamp](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto) | |

### StatisticQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query)|❌| |
| 2 | domain_id |string|✅| |
| 3 | project_id |string|✅| |
| 4 | start_hour |string|❌| |
| 5 | end_hour |string|❌| |
| 6 | aggregation |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto)|❌| |

### StatisticStatQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✅| |
| 2 | domain_id |string|✅| |

### StatisticsInfo
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | results |[list of StatisticInfo](statistic.md#statisticinfo) | |
| 2 | total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |
