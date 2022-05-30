---
description:  
---
# Data source rule

>  **Package : spaceone.api.cost_analysis.v1**

## DataSourceRule

{% hint style="info" %}
**DataSourceRule Methods:**

{%  endhint %}


| Method | Request | Response | Description |
| :-----: | :--------: | :--------: | :-------------------- |
| [**create**](data-source-rule.md#create)|   [CreateDataSourceRuleRequest](data-source-rule.md#createdatasourcerulerequest) |   [DataSourceRuleInfo](data-source-rule.md#datasourceruleinfo) |  |
| [**update**](data-source-rule.md#update)|   [UpdateDataSourceRuleRequest](data-source-rule.md#updatedatasourcerulerequest) |   [DataSourceRuleInfo](data-source-rule.md#datasourceruleinfo) |  |
| [**change_order**](data-source-rule.md#change_order)|   [ChangeDataSourceRuleOrderRequest](data-source-rule.md#changedatasourceruleorderrequest) |   [DataSourceRuleInfo](data-source-rule.md#datasourceruleinfo) |  |
| [**delete**](data-source-rule.md#delete)|   [DataSourceRuleRequest](data-source-rule.md#datasourcerulerequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| [**get**](data-source-rule.md#get)|   [GetDataSourceRuleRequest](data-source-rule.md#getdatasourcerulerequest) |   [DataSourceRuleInfo](data-source-rule.md#datasourceruleinfo) |  |
| [**list**](data-source-rule.md#list)|   [DataSourceRuleQuery](data-source-rule.md#datasourcerulequery) |   [DataSourceRulesInfo](data-source-rule.md#datasourcerulesinfo) |  |
| [**stat**](data-source-rule.md#stat)|   [DataSourceRuleStatQuery](data-source-rule.md#datasourcerulestatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  |TEST

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
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   CreateDataSourceRuleRequest </td>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   DataSourceRuleInfo </td>
      <td style="width: 400px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;"></td>
    </tr>
    <tr>
      <th scope="row" style="width: 80px; padding: 10px; font-weight: bold; vertical-align: top; border-bottom: 1px solid #ccc;">update</th>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   UpdateDataSourceRuleRequest </td>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   DataSourceRuleInfo </td>
      <td style="width: 400px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;"></td>
    </tr>
    <tr>
      <th scope="row" style="width: 80px; padding: 10px; font-weight: bold; vertical-align: top; border-bottom: 1px solid #ccc;">change_order</th>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   ChangeDataSourceRuleOrderRequest </td>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   DataSourceRuleInfo </td>
      <td style="width: 400px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;"></td>
    </tr>
    <tr>
      <th scope="row" style="width: 80px; padding: 10px; font-weight: bold; vertical-align: top; border-bottom: 1px solid #ccc;">delete</th>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   DataSourceRuleRequest </td>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   google.protobuf.Empty </td>
      <td style="width: 400px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;"></td>
    </tr>
    <tr>
      <th scope="row" style="width: 80px; padding: 10px; font-weight: bold; vertical-align: top; border-bottom: 1px solid #ccc;">get</th>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   GetDataSourceRuleRequest </td>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   DataSourceRuleInfo </td>
      <td style="width: 400px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;"></td>
    </tr>
    <tr>
      <th scope="row" style="width: 80px; padding: 10px; font-weight: bold; vertical-align: top; border-bottom: 1px solid #ccc;">list</th>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   DataSourceRuleQuery </td>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   DataSourceRulesInfo </td>
      <td style="width: 400px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;"></td>
    </tr>
    <tr>
      <th scope="row" style="width: 80px; padding: 10px; font-weight: bold; vertical-align: top; border-bottom: 1px solid #ccc;">stat</th>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   DataSourceRuleStatQuery </td>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   google.protobuf.Struct </td>
      <td style="width: 400px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;"></td>
    </tr></tbody>
</table> 
 

 
### create
> **POST** /cost-analysis/v1/data_source_rules
>


| Type | Message |
| :--- | :--- |
| Request | [CreateDataSourceRuleRequest](data-source-rule.md#createdatasourcerulerequest) |
| Response |  [DataSourceRuleInfo](data-source-rule.md#datasourceruleinfo)  |
 
 

 
### update
> **PUT** /cost-analysis/v1/data_source_rule/{data_source_rule_id}
>


| Type | Message |
| :--- | :--- |
| Request | [UpdateDataSourceRuleRequest](data-source-rule.md#updatedatasourcerulerequest) |
| Response |  [DataSourceRuleInfo](data-source-rule.md#datasourceruleinfo)  |
 
 

 
### change_order
> **PUT** /cost-analysis/v1/data_source_rule/{data_source_rule_id}/order
>


| Type | Message |
| :--- | :--- |
| Request | [ChangeDataSourceRuleOrderRequest](data-source-rule.md#changedatasourceruleorderrequest) |
| Response |  [DataSourceRuleInfo](data-source-rule.md#datasourceruleinfo)  |
 
 

 
### delete
> **DELETE** /cost-analysis/v1/data_source_rule/{data_source_rule_id}
>


| Type | Message |
| :--- | :--- |
| Request | [DataSourceRuleRequest](data-source-rule.md#datasourcerulerequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
 
 

 
### get
> **GET** /cost-analysis/v1/data_source_rule/{data_source_rule_id}
>


| Type | Message |
| :--- | :--- |
| Request | [GetDataSourceRuleRequest](data-source-rule.md#getdatasourcerulerequest) |
| Response |  [DataSourceRuleInfo](data-source-rule.md#datasourceruleinfo)  |
 
 

 
### list
> **GET** /cost-analysis/v1/data_source_rules
>
> **POST** /cost-analysis/v1/data_source_rules/search



| Type | Message |
| :--- | :--- |
| Request | [DataSourceRuleQuery](data-source-rule.md#datasourcerulequery) |
| Response |  [DataSourceRulesInfo](data-source-rule.md#datasourcerulesinfo)  |
 
 

 
### stat
> **POST** /cost-analysis/v1/data_source_rules/stat
>


| Type | Message |
| :--- | :--- |
| Request | [DataSourceRuleStatQuery](data-source-rule.md#datasourcerulestatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |


## 

## Message

### ChangeDataSourceRuleOrderRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| data_source_rule_id |string|✅| |
| order |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto)|✅| |
| domain_id |string|✅| |

### CreateDataSourceRuleRequest
<table>
  <thead>
    <tr>
      <th style="text-align:left; width:100px;">Field</th>
      <th style="text-align:left">Type</th>
      <th style="text-align:center">Required</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left; width:100px;">name</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">conditions</td>
      <td style="text-align:left"><a href="data-source-rule.md#datasourcerulecondition">list of DataSourceRuleCondition</a></td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">conditions_policy</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>ALL</li>
          	<li>ANY</li>
          	<li>ALWAYS</li>
        </ul></td>
<td style="text-align:center">✅</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">actions</td>
      <td style="text-align:left"><a href="data-source-rule.md#datasourceruleactions">DataSourceRuleActions</a></td>
<td style="text-align:center">✅</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">options</td>
      <td style="text-align:left"><a href="data-source-rule.md#datasourceruleoptions">DataSourceRuleOptions</a></td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">tags</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">data_source_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✅</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✅</td>
<td style="text-align:left"></td>
   </tr>
  </tbody>
</table>



### DataSourceRuleActions
| Field | Type |  Description |
| :--- | :--- | :--- |
| change_project |string | |
| match_project |[MatchRule](data-source-rule.md#matchrule) | |
| match_service_account |[MatchRule](data-source-rule.md#matchrule) | |
| add_additional_info |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |

### DataSourceRuleCondition
| Field | Type |  Description |
| :--- | :--- | :--- |
| key |string | |
| value |string | |
| operator |string | |

### DataSourceRuleInfo
<table>
  <thead>
    <tr>
      <th style="text-align:left; width:100px;">Field</th>
      <th style="text-align:left">Type</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left; width:100px;">data_source_rule_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">name</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">order</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto">int32</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">conditions</td>
      <td style="text-align:left"><a href="data-source-rule.md#datasourcerulecondition">list of DataSourceRuleCondition</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">conditions_policy</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>ALL</li>
          	<li>ANY</li>
          	<li>ALWAYS</li>
        </ul></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">actions</td>
      <td style="text-align:left"><a href="data-source-rule.md#datasourceruleactions">DataSourceRuleActions</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">options</td>
      <td style="text-align:left"><a href="data-source-rule.md#datasourceruleoptions">DataSourceRuleOptions</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">tags</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">data_source_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">created_at</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
  </tbody>
</table>



### DataSourceRuleOptions
| Field | Type |  Description |
| :--- | :--- | :--- |
| stop_processing |bool | |

### DataSourceRuleQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query)|❌| |
| data_source_rule_id |string|❌| |
| name |string|❌| |
| data_source_id |string|❌| |
| domain_id |string|✅| |

### DataSourceRuleRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| data_source_rule_id |string|✅| |
| domain_id |string|✅| |

### DataSourceRuleStatQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✅| |
| domain_id |string|✅| |

### DataSourceRulesInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| results |[list of DataSourceRuleInfo](data-source-rule.md#datasourceruleinfo) | |
| total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### GetDataSourceRuleRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| data_source_rule_id |string|✅| |
| domain_id |string|✅| |
| only |list of string|❌| |

### MatchRule
| Field | Type |  Description |
| :--- | :--- | :--- |
| source |string | |
| target |string | |

### UpdateDataSourceRuleRequest
<table>
  <thead>
    <tr>
      <th style="text-align:left; width:100px;">Field</th>
      <th style="text-align:left">Type</th>
      <th style="text-align:center">Required</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left; width:100px;">data_source_rule_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✅</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">name</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">conditions</td>
      <td style="text-align:left"><a href="data-source-rule.md#datasourcerulecondition">list of DataSourceRuleCondition</a></td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">conditions_policy</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>ALL</li>
          	<li>ANY</li>
          	<li>ALWAYS</li>
        </ul></td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">actions</td>
      <td style="text-align:left"><a href="data-source-rule.md#datasourceruleactions">DataSourceRuleActions</a></td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">options</td>
      <td style="text-align:left"><a href="data-source-rule.md#datasourceruleoptions">DataSourceRuleOptions</a></td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">tags</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✅</td>
<td style="text-align:left"></td>
   </tr>
  </tbody>
</table>


