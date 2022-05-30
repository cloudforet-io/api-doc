---
description:  
---
# Billing

>  **Package : spaceone.api.billing.v1**

## Billing

{% hint style="info" %}
**Billing Methods:**

{%  endhint %}


| Method | Request | Response |
| :-----: | :--------: | :--------: |
| [**get_data**](billing.md#get_data)|   [BillingDataRequest](billing.md#billingdatarequest) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)| 
 

 
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
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| project_id |string|❌| |
| project_group_id |string|❌| |
| service_accounts |list of string|❌| |
| filter |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| aggregation |list of string|❌| |
| start |string|✅| |
| end |string|✅| |
| granularity |string|✅| |
| domain_id |string|✅| |
| sort |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| limit |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto)|❌| |
