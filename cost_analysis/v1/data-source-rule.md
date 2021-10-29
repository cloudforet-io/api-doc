---
description:  
---
# Data source rule

>  **Package : spaceone.api.cost_analysis.v1**

## DataSourceRule

{% hint style="info" %}
**DataSourceRule Methods:**

{%  endhint %}


| NO |  Method | Request Type | Response Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [**create**](data-source-rule.md#create)|   [CreateDataSourceRuleRequest](data-source-rule.md#createdatasourcerulerequest) |   [DataSourceRuleInfo](data-source-rule.md#datasourceruleinfo) |  |
| 2 | [**update**](data-source-rule.md#update)|   [UpdateDataSourceRuleRequest](data-source-rule.md#updatedatasourcerulerequest) |   [DataSourceRuleInfo](data-source-rule.md#datasourceruleinfo) |  |
| 3 | [**change_order**](data-source-rule.md#change_order)|   [ChangeDataSourceRuleOrderRequest](data-source-rule.md#changedatasourceruleorderrequest) |   [DataSourceRuleInfo](data-source-rule.md#datasourceruleinfo) |  |
| 4 | [**delete**](data-source-rule.md#delete)|   [DataSourceRuleRequest](data-source-rule.md#datasourcerulerequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| 5 | [**get**](data-source-rule.md#get)|   [GetDataSourceRuleRequest](data-source-rule.md#getdatasourcerulerequest) |   [DataSourceRuleInfo](data-source-rule.md#datasourceruleinfo) |  |
| 6 | [**list**](data-source-rule.md#list)|   [DataSourceRuleQuery](data-source-rule.md#datasourcerulequery) |   [DataSourceRulesInfo](data-source-rule.md#datasourcerulesinfo) |  |
| 7 | [**stat**](data-source-rule.md#stat)|   [DataSourceRuleStatQuery](data-source-rule.md#datasourcerulestatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  | 
 

 
### create
> **POST** /cost-analysis/v2/data_source_rules
>


| Type | Message |
| :--- | :--- |
| Request | [CreateDataSourceRuleRequest](data-source-rule.md#createdatasourcerulerequest) |
| Response |  [DataSourceRuleInfo](data-source-rule.md#datasourceruleinfo)  |
 
 

 
### update
> **PUT** /cost-analysis/v2/data_source_rule/{data_source_rule_id}
>


| Type | Message |
| :--- | :--- |
| Request | [UpdateDataSourceRuleRequest](data-source-rule.md#updatedatasourcerulerequest) |
| Response |  [DataSourceRuleInfo](data-source-rule.md#datasourceruleinfo)  |
 
 

 
### change_order
> **PUT** /cost-analysis/v2/data_source_rule/{data_source_rule_id}/order
>


| Type | Message |
| :--- | :--- |
| Request | [ChangeDataSourceRuleOrderRequest](data-source-rule.md#changedatasourceruleorderrequest) |
| Response |  [DataSourceRuleInfo](data-source-rule.md#datasourceruleinfo)  |
 
 

 
### delete
> **DELETE** /cost-analysis/v2/data_source_rule/{data_source_rule_id}
>


| Type | Message |
| :--- | :--- |
| Request | [DataSourceRuleRequest](data-source-rule.md#datasourcerulerequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
 
 

 
### get
> **GET** /cost-analysis/v2/data_source_rule/{data_source_rule_id}
>


| Type | Message |
| :--- | :--- |
| Request | [GetDataSourceRuleRequest](data-source-rule.md#getdatasourcerulerequest) |
| Response |  [DataSourceRuleInfo](data-source-rule.md#datasourceruleinfo)  |
 
 

 
### list
> **GET** /cost-analysis/v2/data_source_rules
>
> **POST** /cost-analysis/v2/data_source_rules/search



| Type | Message |
| :--- | :--- |
| Request | [DataSourceRuleQuery](data-source-rule.md#datasourcerulequery) |
| Response |  [DataSourceRulesInfo](data-source-rule.md#datasourcerulesinfo)  |
 
 

 
### stat
> **POST** /cost-analysis/v2/data_source_rules/stat
>


| Type | Message |
| :--- | :--- |
| Request | [DataSourceRuleStatQuery](data-source-rule.md#datasourcerulestatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |


## 

## Message

### ChangeDataSourceRuleOrderRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :---: | :--- |
| 1 | data_source_rule_id |string|✅| |
| 2 | order |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto)|✅| |
| 3 | domain_id |string|✅| |

### CreateDataSourceRuleRequest
<table>
  <thead>
    <tr>
      <th style="text-align:left">No</th>
      <th style="text-align:left">Field</th>
      <th style="text-align:left">Type</th>
      <th style="text-align:center">Required</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">1</td>
      <td style="text-align:left">name</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">2</td>
      <td style="text-align:left">conditions</td>
      <td style="text-align:left"><a href="data-source-rule.md#datasourcerulecondition">list of DataSourceRuleCondition</a></td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">3</td>
      <td style="text-align:left">conditions_policy</td>
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
      <td style="text-align:left">4</td>
      <td style="text-align:left">actions</td>
      <td style="text-align:left"><a href="data-source-rule.md#datasourceruleactions">DataSourceRuleActions</a></td>
<td style="text-align:center">✅</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">5</td>
      <td style="text-align:left">options</td>
      <td style="text-align:left"><a href="data-source-rule.md#datasourceruleoptions">DataSourceRuleOptions</a></td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">6</td>
      <td style="text-align:left">tags</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">7</td>
      <td style="text-align:left">data_source_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✅</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">8</td>
      <td style="text-align:left">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✅</td>
<td style="text-align:left"></td>
   </tr>
  </tbody>
</table>



### DataSourceRuleActions
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | change_project |string | |
| 2 | match_project |[MatchRule](data-source-rule.md#matchrule) | |
| 3 | match_service_account |[MatchRule](data-source-rule.md#matchrule) | |
| 4 | add_additional_info |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |

### DataSourceRuleCondition
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | key |string | |
| 2 | value |string | |
| 3 | operator |string | |

### DataSourceRuleInfo
<table>
  <thead>
    <tr>
      <th style="text-align:left">No</th>
      <th style="text-align:left">Field</th>
      <th style="text-align:left">Type</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">1</td>
      <td style="text-align:left">data_source_rule_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">2</td>
      <td style="text-align:left">name</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">3</td>
      <td style="text-align:left">order</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto">int32</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">4</td>
      <td style="text-align:left">conditions</td>
      <td style="text-align:left"><a href="data-source-rule.md#datasourcerulecondition">list of DataSourceRuleCondition</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">5</td>
      <td style="text-align:left">conditions_policy</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>ALL</li>
          	<li>ANY</li>
          	<li>ALWAYS</li>
        </ul></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">6</td>
      <td style="text-align:left">actions</td>
      <td style="text-align:left"><a href="data-source-rule.md#datasourceruleactions">DataSourceRuleActions</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">7</td>
      <td style="text-align:left">options</td>
      <td style="text-align:left"><a href="data-source-rule.md#datasourceruleoptions">DataSourceRuleOptions</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">8</td>
      <td style="text-align:left">tags</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">9</td>
      <td style="text-align:left">data_source_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">10</td>
      <td style="text-align:left">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">11</td>
      <td style="text-align:left">created_at</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
  </tbody>
</table>



### DataSourceRuleOptions
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | stop_processing |bool | |

### DataSourceRuleQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :---: | :--- |
| 1 | query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query)|❌| |
| 2 | data_source_rule_id |string|❌| |
| 3 | name |string|❌| |
| 4 | data_source_id |string|❌| |
| 5 | domain_id |string|✅| |

### DataSourceRuleRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :---: | :--- |
| 1 | data_source_rule_id |string|✅| |
| 2 | domain_id |string|✅| |

### DataSourceRuleStatQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :---: | :--- |
| 1 | query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✅| |
| 2 | domain_id |string|✅| |

### DataSourceRulesInfo
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | results |[list of DataSourceRuleInfo](data-source-rule.md#datasourceruleinfo) | |
| 2 | total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### GetDataSourceRuleRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :---: | :--- |
| 1 | data_source_rule_id |string|✅| |
| 2 | domain_id |string|✅| |
| 3 | only |list of string|❌| |

### MatchRule
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | source |string | |
| 2 | target |string | |

### UpdateDataSourceRuleRequest
<table>
  <thead>
    <tr>
      <th style="text-align:left">No</th>
      <th style="text-align:left">Field</th>
      <th style="text-align:left">Type</th>
      <th style="text-align:center">Required</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">1</td>
      <td style="text-align:left">data_source_rule_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✅</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">2</td>
      <td style="text-align:left">name</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">3</td>
      <td style="text-align:left">conditions</td>
      <td style="text-align:left"><a href="data-source-rule.md#datasourcerulecondition">list of DataSourceRuleCondition</a></td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">4</td>
      <td style="text-align:left">conditions_policy</td>
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
      <td style="text-align:left">5</td>
      <td style="text-align:left">actions</td>
      <td style="text-align:left"><a href="data-source-rule.md#datasourceruleactions">DataSourceRuleActions</a></td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">6</td>
      <td style="text-align:left">options</td>
      <td style="text-align:left"><a href="data-source-rule.md#datasourceruleoptions">DataSourceRuleOptions</a></td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">7</td>
      <td style="text-align:left">tags</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">8</td>
      <td style="text-align:left">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✅</td>
<td style="text-align:left"></td>
   </tr>
  </tbody>
</table>


