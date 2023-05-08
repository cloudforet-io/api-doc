---
title: "Budget"
linkTitle: "Budget"
weight: 3
bookFlatSection: true
---
# [Budget](#Budget)
desc: A Budget is a planned amount of cost expenditure for reduction and prediction of infrastructure costs.


>  **Package : spaceone.api.cost_analysis.v1**

<br>
<br>

## Budget


**Budget Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./Budget#create) | [CreateBudgetRequest](Budget#createbudgetrequest) | [BudgetInfo](./Budget#budgetinfo) |
| [**update**](./Budget#update) | [UpdateBudgetRequest](Budget#updatebudgetrequest) | [BudgetInfo](./Budget#budgetinfo) |
| [**set_notification**](./Budget#set_notification) | [SetBudgetNotificationRequest](Budget#setbudgetnotificationrequest) | [BudgetInfo](./Budget#budgetinfo) |
| [**delete**](./Budget#delete) | [BudgetRequest](Budget#budgetrequest) | [Empty](./Budget#empty) |
| [**get**](./Budget#get) | [GetBudgetRequest](Budget#getbudgetrequest) | [BudgetInfo](./Budget#budgetinfo) |
| [**list**](./Budget#list) | [BudgetQuery](Budget#budgetquery) | [BudgetsInfo](./Budget#budgetsinfo) |
| [**stat**](./Budget#stat) | [BudgetStatQuery](Budget#budgetstatquery) | [Struct](./Budget#struct) |



    
<br>

### create

> **POST** /cost-analysis/v1/budget/create
>




 {{< tabs " create " >}}




{{< /tabs >}}

    
<br>

### update

> **POST** /cost-analysis/v1/budget/update
>




 {{< tabs " update " >}}




{{< /tabs >}}

    
<br>

### set_notification

> **POST** /cost-analysis/v1/budget/set-notification
>




 {{< tabs " set_notification " >}}




{{< /tabs >}}

    
<br>

### delete

> **POST** /cost-analysis/v1/budget/delete
>




 {{< tabs " delete " >}}




{{< /tabs >}}

    
<br>

### get

> **POST** /cost-analysis/v1/budget/get
>




 {{< tabs " get " >}}




{{< /tabs >}}

    
<br>

### list

> **POST** /cost-analysis/v1/budget/list
>




 {{< tabs " list " >}}




{{< /tabs >}}

    
<br>

### stat

> **POST** /cost-analysis/v1/budget/stat
>




 {{< tabs " stat " >}}




{{< /tabs >}}

    


<br>
<br>

## Message



### BudgetInfo
* **budget_id** (string)  `Required` 

    
* **name** (string)  `Required` 

    
* **limit** (float)  `Required` 

    
* **planned_limits** (PlannedLimit)  `Required` 

    
* **total_usage_usd_cost** (float)  `Required` 

    
* **cost_types** (Struct)  `Required` 

    
* **time_unit** (TimeUnit)  `Required` 

    
* **start** (string)  `Required` 

    
* **end** (string)  `Required` 

    
* **notifications** (BudgetNotification)  `Required` 

    
* **tags** (Struct)  `Required` 

    
* **project_id** (string)  `Required` 

    
* **project_group_id** (string)  `Required` 

    
* **domain_id** (string)  `Required` 

    
* **created_at** (string)  `Required` 

    
* **updated_at** (string)  `Required` 

    <br>

### BudgetNotification
* **threshold** (float)  `Required` 

    
* **unit** (Unit)  `Required` 

    
* **notification_type** (NotificationType)  `Required` 

    <br>

### BudgetQuery
* **query** (Query)  `Required` 

  *is_required: false*

    
* **budget_id** (string)  `Required` 

  *is_required: false*

    
* **name** (string)  `Required` 

  *is_required: false*

    
* **project_id** (string)  `Required` 

  *is_required: false*

    
* **project_group_id** (string)  `Required` 

  *is_required: false*

    
* **time_unit** (TimeUnit)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### BudgetRequest
* **budget_id** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### BudgetStatQuery
* **query** (StatisticsQuery)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### BudgetsInfo
* **results** (BudgetInfo)  `Required` 

    
* **total_count** (int32)  `Required` 

    <br>

### CreateBudgetRequest
* **name** (string)  `Required` 

  *is_required: false*

    
* **limit** (float)  `Required` 

  *is_required: false*

    
* **planned_limits** (PlannedLimit)  `Required` 

  *is_required: false*

    
* **cost_types** (Struct)  `Required` 

  *is_required: false*

    
* **time_unit** (TimeUnit)  `Required` 

  *is_required: true*

    
* **start** (string)  `Required` 

  *is_required: true*

    
* **end** (string)  `Required` 

  *is_required: true*

    
* **notifications** (BudgetNotification)  `Required` 

  *is_required: false*

    
* **tags** (Struct)  `Required` 

  *is_required: false*

    
* **project_id** (string)  `Required` 

  *is_required: false*

    
* **project_group_id** (string)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### GetBudgetRequest
* **budget_id** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    
* **only** (string)  `Required` 

  *is_required: false*

    <br>

### PlannedLimit
* **date** (string)  `Required` 

    
* **limit** (float)  `Required` 

    <br>

### SetBudgetNotificationRequest
* **budget_id** (string)  `Required` 

  *is_required: true*

    
* **notifications** (BudgetNotification)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### UpdateBudgetRequest
* **budget_id** (string)  `Required` 

  *is_required: true*

    
* **name** (string)  `Required` 

  *is_required: false*

    
* **limit** (float)  `Required` 

  *is_required: false*

    
* **planned_limits** (PlannedLimit)  `Required` 

  *is_required: false*

    
* **end** (string)  `Required` 

  *is_required: false*

    
* **tags** (Struct)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>
