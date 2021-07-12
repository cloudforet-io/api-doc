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
| 1 | [**get_data**](billing.md#get_data)|   [BillingDataRequest](billing.md#billingdatarequest) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  | 
 

 
### get_data
> **GET** /billing/v1/billing/get-data
>


| Type | Message |
| :--- | :--- |
| Request | [BillingDataRequest](billing.md#billingdatarequest) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |


## 

## Message

### BillingDataRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :---: | :--- |
| 1 | project_id |string|❌| |
| 2 | project_group_id |string|❌| |
| 3 | service_accounts |list of string|❌| |
| 4 | filter |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| 5 | aggregation |list of string|❌| |
| 6 | start |string|✅| |
| 7 | end |string|✅| |
| 8 | granularity |string|✅| |
| 9 | domain_id |string|✅| |
| 10 | sort |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| 11 | limit |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto)|❌| |
