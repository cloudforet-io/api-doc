---
description:  
---
# Billing

>  **Package : spaceone.api.billing.plugin**

## Billing

{% hint style="info" %}
**Billing Methods:**

{%  endhint %}


| NO |  Method | Request Type | Response Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [**get_data**](billing.md#get_data)|   [BillingDataRequest](billing.md#billingdatarequest) |   [PluginBillingDataResponse](billing.md#pluginbillingdataresponse) |  | 
 

 
### get_data


| Type | Message |
| :--- | :--- |
| Request | [BillingDataRequest](billing.md#billingdatarequest) |
| Response |  [PluginBillingDataResponse](billing.md#pluginbillingdataresponse)  |


## 

## Message

### BillingData
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | date |string|✅| |
| 2 | cost |double|✅| |
| 3 | currency |string|❌| |

### BillingDataRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | options |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✅| |
| 2 | secret_data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✅| |
| 3 | filter |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| 4 | aggregation |list of string|❌| |
| 5 | start |string|❌| billing period's start date|
| 6 | end |string|✅| billing period's end date|
| 7 | granularity |string|❌| |
| 8 | schema |string|❌| |

### BillingInfo
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | resource_type |string|✅| |
| 2 | billing_data |[list of BillingData](billing.md#billingdata)|✅| |
| 3 | name |string|❌| |

### PluginBillingDataResponse
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | results |[list of BillingInfo](billing.md#billinginfo)|✅| |
| 2 | total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto)|✅| |
