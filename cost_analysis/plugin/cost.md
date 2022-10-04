---
description:  
---
# Cost

>  **Package : spaceone.api.cost_analysis.plugin**

## Cost

{% hint style="info" %}
**Cost Methods:**

{%  endhint %}


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**get_data**](cost.md#get_data)|   [GetDataRequest](cost.md#getdatarequest) | **`stream`**   [CostsInfo](cost.md#costsinfo) | 
 

 
### get_data

> ''

| Type | Message |
| :--- | :--- |
| Request | [GetDataRequest](cost.md#getdatarequest) |
| Response |  [CostsInfo](cost.md#costsinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{}
```
{% endtab %}
{% endtabs %}


## 

## Message

### CostInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| cost |float | |
| currency |string | |
| usage_quantity |float | |
| provider |string | |
| region_code |string | |
| category |string | |
| product |string | |
| account |string | |
| usage_type |string | |
| resource_group |string | |
| resource |string | |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| additional_info |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| billed_at |string | |

### CostsInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| results |[list of CostInfo](cost.md#costinfo) | |

### GetDataRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| options |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✔| |
| secret_data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✔| |
| schema |string|✘| |
| task_options |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✘| |
| domain_id |string|✔| |
