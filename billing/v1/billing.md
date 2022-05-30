---
description:  
---
# Billing

>  **Package : spaceone.api.billing.v1**

## Billing

{% hint style="info" %}
**Billing Methods:**

{%  endhint %}


| Method | Request | Response | Description &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; |
| :-----: | :--------: | :--------: | :-------------------- |
| [**get_data**](billing.md#get_data)|   [BillingDataRequest](billing.md#billingdatarequest) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  |TEST

| Method | Request | Response | Description &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; |
| :-----: | :--------: | :--------: | :-------------------- |
|<div style="width:70px; text-align:center;">  [**get_data**](billing.md#get_data) </div> | <div style="width:200px; text-align:center;">    [BillingDataRequest](billing.md#billingdatarequest)  </div> | <div style="width:200px; text-align:center;">  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) </div> | <div style="width:400px;">  </div> | 
 

 
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
