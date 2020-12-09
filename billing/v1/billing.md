---
description:  
---
# Billing

>  **Package : spaceone.api.billing.v1**

## Billing

{% hint style="info" %}
**Billing Methods:**

{%  endhint %}


| NO |  Method | Request Type | Response Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [**get_data**](billing.md#get_data)|   [BillingDataRequest](billing.md#billingdatarequest) |   [BillingDataInfo](billing.md#billingdatainfo) |  | 
 

 
### get_data
> **GET** /billing/v1/billing/get-data
>


| Type | Message |
| :--- | :--- |
| Request | [BillingDataRequest](billing.md#billingdatarequest) |
| Response |  [BillingDataInfo](billing.md#billingdatainfo)  |


## 

## Message

### BillingData
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | date |string | |
| 2 | cost |double | |
| 3 | currency |string | |

### BillingDataInfo
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | results |[list of BillingInfo](billing.md#billinginfo) | |
| 2 | total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### BillingDataRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | project_id |string|❌| |
| 2 | project_group_id |string|❌| |
| 3 | service_accounts |list of string|❌| |
| 4 | filter |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| 5 | aggregation |list of string|❌| |
| 6 | start |[google.protobuf.Timestamp](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto)|✅| |
| 7 | end |[google.protobuf.Timestamp](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto)|✅| |
| 8 | granularity |string|✅| |
| 9 | domain_id |string|✅| |

### BillingInfo
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | service_account_id |string | |
| 2 | resource_type |string | |
| 3 | name |string | |
| 4 | billing_data |[list of BillingData](billing.md#billingdata) | |
| 5 | domain_id |string | |
