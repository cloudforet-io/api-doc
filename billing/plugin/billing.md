---
description:  
---
# Billing

>  **Package : spaceone.api.billing.plugin**

## Billing

{% hint style="info" %}
**Billing Methods:**

{%  endhint %}


| Method | Request | Response | Description &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; |
| :-----: | :--------: | :--------: | :-------------------- |
| [**get_data**](billing.md#get_data)|   [BillingDataRequest](billing.md#billingdatarequest) |   [PluginBillingDataResponse](billing.md#pluginbillingdataresponse) |  |TEST

| Method | Request | Response | Description &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; |
| :-----: | :--------: | :--------: | :-------------------- |
|<div style="width:70px; text-align:center;">  [**get_data**](billing.md#get_data) </div> | <div style="width:200px; text-align:center;">    [BillingDataRequest](billing.md#billingdatarequest)  </div> | <div style="width:200px; text-align:center;">   [PluginBillingDataResponse](billing.md#pluginbillingdataresponse)  </div> | <div style="width:400px;">  </div> | 
 

 
### get_data


| Type | Message |
| :--- | :--- |
| Request | [BillingDataRequest](billing.md#billingdatarequest) |
| Response |  [PluginBillingDataResponse](billing.md#pluginbillingdataresponse)  |


## 

## Message

### BillingData
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| date |string|✅| |
| cost |double|✅| |
| currency |string|❌| |

### BillingDataRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| options |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✅| |
| secret_data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✅| |
| filter |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| aggregation |list of string|❌| |
| start |string|❌| billing period's start date|
| end |string|✅| billing period's end date|
| granularity |string|❌| |
| schema |string|❌| |

### BillingInfo
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| resource_type |string|✅| |
| billing_data |[list of BillingData](billing.md#billingdata)|✅| |
| name |string|❌| |

### PluginBillingDataResponse
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| results |[list of BillingInfo](billing.md#billinginfo)|✅| |
| total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto)|✅| |
