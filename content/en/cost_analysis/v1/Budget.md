---
title: "Budget"
linkTitle: "Budget"
weight: 3
bookFlatSection: true
---
# [Budget](#Budget)
A Budget is a planned amount of cost expenditure for reduction and prediction of infrastructure costs.


>  **Package : spaceone.api.cost_analysis.v1**

<br>
<br>

## Budget





**Budget Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./Budget#create) | [CreateBudgetRequest](Budget#createbudgetrequest) | [BudgetInfo](Budget#budgetinfo) |
| [**update**](./Budget#update) | [UpdateBudgetRequest](Budget#updatebudgetrequest) | [BudgetInfo](Budget#budgetinfo) |
| [**set_notification**](./Budget#set_notification) | [SetBudgetNotificationRequest](Budget#setbudgetnotificationrequest) | [BudgetInfo](Budget#budgetinfo) |
| [**delete**](./Budget#delete) | [BudgetRequest](Budget#budgetrequest) | [Empty](Budget#empty) |
| [**get**](./Budget#get) | [GetBudgetRequest](Budget#getbudgetrequest) | [BudgetInfo](Budget#budgetinfo) |
| [**list**](./Budget#list) | [BudgetQuery](Budget#budgetquery) | [BudgetsInfo](Budget#budgetsinfo) |
| [**stat**](./Budget#stat) | [BudgetStatQuery](Budget#budgetstatquery) | [Struct](Budget#struct) |



    
<br>

### create

Creates a new Budget. When creating a Budget, it should be set for a specific ProjectGroup or Project. The budgeted amount and date of the `planned_limits` should be specified on a monthly or yearly basis.



> **POST** /cost-analysis/v1/budget/create
>





 {{< tabs " create " >}}

 {{< tab "Request Example" >}}



[CreateBudgetRequest](./Budget#createbudgetrequest)

* **time_unit** (TimeUnit)   `Required` 


* **start** (string)   `Required` 


* **end** (string)   `Required` 


* **domain_id** (string)   `Required` 


* **name** (string)  


* **limit** (float)  


* **planned_limits** (PlannedLimit)  `Repeated`   


* **cost_types** (Struct)  


* **notifications** (BudgetNotification)  `Repeated`   


* **tags** (Struct)  


* **project_id** (string)  


* **project_group_id** (string)  





{{< highlight json >}}
{
   "name": "Cloudforet-Budget",
   "planned_limits": [{"date": "2022-01", "limit": 1000.0},
                      {"date": "2022-02", "limit": 1100.0},
                      {"date": "2022-03", "limit": 1200.0},
                      {"date": "2022-04", "limit": 1300.0},
                      {"date": "2022-05", "limit": 1400.0},
                      {"date": "2022-06", "limit": 1500.0},
                      {"date": "2022-07", "limit": 1600.0},
                      {"date": "2022-08", "limit": 1700.0},
                      {"date": "2022-09", "limit": 1800.0},
                      {"date": "2022-10", "limit": 1900.0},
                      {"date": "2022-11", "limit": 2000.0},
                      {"date": "2022-12", "limit": 2100.0}],
   "time_unit": "MONTHLY",
   "start": "2022-01",
   "end": "2022-12",
   "project_group_id": "pg-812c90990877"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[BudgetInfo](#BUDGETINFO)
* **budget_id** (string)   `Required` 

* **name** (string)   `Required` 

* **limit** (float)   `Required` 

* **planned_limits** (PlannedLimit)  `Repeated`   `Required` 

* **total_usage_usd_cost** (float)   `Required` 

* **cost_types** (Struct)   `Required` 

* **time_unit** (TimeUnit)   `Required` 

* **start** (string)   `Required` 

* **end** (string)   `Required` 

* **notifications** (BudgetNotification)  `Repeated`   `Required` 

* **tags** (Struct)   `Required` 

* **project_id** (string)   `Required` 

* **project_group_id** (string)   `Required` 

* **domain_id** (string)   `Required` 

* **created_at** (string)   `Required` 

* **updated_at** (string)   `Required` 



{{< highlight json >}}
{
       "budget_id": "budget-d51b6b6a9910",
       "name": "Cloudforet-Budget",
       "limit": 18600.0,
       "planned_limits": [
           {
               "date": "2022-01",
               "limit": 1000.0
           },
           {
               "date": "2022-02",
               "limit": 1100.0
           },
           {
               "date": "2022-03",
               "limit": 1200.0
           },
           {
               "date": "2022-04",
               "limit": 1300.0
           },
           {
               "date": "2022-05",
               "limit": 1400.0
           },
           {
               "date": "2022-06",
               "limit": 1500.0
           },
           {
               "date": "2022-07",
               "limit": 1600.0
           },
           {
               "date": "2022-08",
               "limit": 1700.0
           },
           {
               "date": "2022-09",
               "limit": 1800.0
           },
           {
               "date": "2022-10",
               "limit": 1900.0
           },
           {
               "date": "2022-11",
               "limit": 2000.0
           },
           {
               "date": "2022-12",
               "limit": 2100.0
           }
       ],
       "total_usage_usd_cost": 43412.45,
       "time_unit": "MONTHLY",
       "start": "2022-01",
       "end": "2022-12",
       "tags": {},
       "project_group_id": "pg-812c90990877",
       "domain_id": "domain-58010aa2e451",
       "created_at": "2022-07-18T09:30:56.901Z",
       "updated_at": "2022-07-18T09:30:56.901Z"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### update

Updates a specific Budget. You can make changes in the budgeted amount of the time period specified while creating the resource.



> **POST** /cost-analysis/v1/budget/update
>





 {{< tabs " update " >}}

 {{< tab "Request Example" >}}



[UpdateBudgetRequest](./Budget#updatebudgetrequest)

* **budget_id** (string)   `Required` 


* **domain_id** (string)   `Required` 


* **name** (string)  


* **limit** (float)  


* **planned_limits** (PlannedLimit)  `Repeated`   


* **end** (string)  


* **tags** (Struct)  





{{< highlight json >}}
{
   "budget_id": "budget-d51b6b6a9910",
   "name": "Cloudforet-Budget-test", "limit": 15000.0,
   "planned_limits": [{"date": "2022-01", "limit": 500.0},
                      {"date": "2022-02", "limit": 500.0},
                      {"date": "2022-03", "limit": 500.0},
                      {"date": "2022-04", "limit": 500.0},
                      {"date": "2022-05", "limit": 500.0},
                      {"date": "2022-06", "limit": 500.0},
                      {"date": "2022-07", "limit": 500.0},
                      {"date": "2022-08", "limit": 500.0},
                      {"date": "2022-09", "limit": 500.0}],
   "end": "2022-12",
   "tags": {}
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[BudgetInfo](#BUDGETINFO)
* **budget_id** (string)   `Required` 

* **name** (string)   `Required` 

* **limit** (float)   `Required` 

* **planned_limits** (PlannedLimit)  `Repeated`   `Required` 

* **total_usage_usd_cost** (float)   `Required` 

* **cost_types** (Struct)   `Required` 

* **time_unit** (TimeUnit)   `Required` 

* **start** (string)   `Required` 

* **end** (string)   `Required` 

* **notifications** (BudgetNotification)  `Repeated`   `Required` 

* **tags** (Struct)   `Required` 

* **project_id** (string)   `Required` 

* **project_group_id** (string)   `Required` 

* **domain_id** (string)   `Required` 

* **created_at** (string)   `Required` 

* **updated_at** (string)   `Required` 



{{< highlight json >}}
{
       "budget_id": "budget-d51b6b6a9910",
       "name": "Cloudforet-Budget",
       "limit": 18600.0,
       "planned_limits": [
           {
               "date": "2022-01",
               "limit": 1000.0
           },
           {
               "date": "2022-02",
               "limit": 1100.0
           },
           {
               "date": "2022-03",
               "limit": 1200.0
           },
           {
               "date": "2022-04",
               "limit": 1300.0
           },
           {
               "date": "2022-05",
               "limit": 1400.0
           },
           {
               "date": "2022-06",
               "limit": 1500.0
           },
           {
               "date": "2022-07",
               "limit": 1600.0
           },
           {
               "date": "2022-08",
               "limit": 1700.0
           },
           {
               "date": "2022-09",
               "limit": 1800.0
           },
           {
               "date": "2022-10",
               "limit": 1900.0
           },
           {
               "date": "2022-11",
               "limit": 2000.0
           },
           {
               "date": "2022-12",
               "limit": 2100.0
           }
       ],
       "total_usage_usd_cost": 43412.45,
       "time_unit": "MONTHLY",
       "start": "2022-01",
       "end": "2022-12",
       "tags": {},
       "project_group_id": "pg-812c90990877",
       "domain_id": "domain-58010aa2e451",
       "created_at": "2022-07-18T09:30:56.901Z",
       "updated_at": "2022-07-18T09:30:56.901Z"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### set_notification

Sets a notification on a specific Budget. Sets a threshold on the budget, and if the cost exceeds the threshold, a notification is raised.



> **POST** /cost-analysis/v1/budget/set-notification
>





 {{< tabs " set_notification " >}}

 {{< tab "Request Example" >}}



[SetBudgetNotificationRequest](./Budget#setbudgetnotificationrequest)

* **budget_id** (string)   `Required` 


* **notifications** (BudgetNotification)  `Repeated`    `Required` 


* **domain_id** (string)   `Required` 





{{< highlight json >}}
{
   "budget_id": "budget-4c8606da4521",
   "notifications": [
       {
           "threshold": 20.0,
           "unit": "PERCENT",
           "notification_type": "CRITICAL"
       },
       {
           "threshold": 1000.0,
           "unit": "ACTUAL_COST",
           "notification_type": "WARNING"
       }
   ]
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[BudgetInfo](#BUDGETINFO)
* **budget_id** (string)   `Required` 

* **name** (string)   `Required` 

* **limit** (float)   `Required` 

* **planned_limits** (PlannedLimit)  `Repeated`   `Required` 

* **total_usage_usd_cost** (float)   `Required` 

* **cost_types** (Struct)   `Required` 

* **time_unit** (TimeUnit)   `Required` 

* **start** (string)   `Required` 

* **end** (string)   `Required` 

* **notifications** (BudgetNotification)  `Repeated`   `Required` 

* **tags** (Struct)   `Required` 

* **project_id** (string)   `Required` 

* **project_group_id** (string)   `Required` 

* **domain_id** (string)   `Required` 

* **created_at** (string)   `Required` 

* **updated_at** (string)   `Required` 



{{< highlight json >}}
{
       "budget_id": "budget-d51b6b6a9910",
       "name": "Cloudforet-Budget",
       "limit": 18600.0,
       "planned_limits": [
           {
               "date": "2022-01",
               "limit": 1000.0
           },
           {
               "date": "2022-02",
               "limit": 1100.0
           },
           {
               "date": "2022-03",
               "limit": 1200.0
           },
           {
               "date": "2022-04",
               "limit": 1300.0
           },
           {
               "date": "2022-05",
               "limit": 1400.0
           },
           {
               "date": "2022-06",
               "limit": 1500.0
           },
           {
               "date": "2022-07",
               "limit": 1600.0
           },
           {
               "date": "2022-08",
               "limit": 1700.0
           },
           {
               "date": "2022-09",
               "limit": 1800.0
           },
           {
               "date": "2022-10",
               "limit": 1900.0
           },
           {
               "date": "2022-11",
               "limit": 2000.0
           },
           {
               "date": "2022-12",
               "limit": 2100.0
           }
       ],
       "total_usage_usd_cost": 43412.45,
       "time_unit": "MONTHLY",
       "start": "2022-01",
       "end": "2022-12",
       "tags": {},
       "project_group_id": "pg-812c90990877",
       "domain_id": "domain-58010aa2e451",
       "created_at": "2022-07-18T09:30:56.901Z",
       "updated_at": "2022-07-18T09:30:56.901Z"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### delete

Deletes a specific Budget. You must specify the `budget_id` of the Budget to delete.



> **POST** /cost-analysis/v1/budget/delete
>





 {{< tabs " delete " >}}

 {{< tab "Request Example" >}}



[BudgetRequest](./Budget#budgetrequest)

* **budget_id** (string)   `Required` 


* **domain_id** (string)   `Required` 





{{< highlight json >}}
{
   "budget_id": "budget-d51b6b6a9910"
}
{{< /highlight >}}
{{< /tab >}}



{{< /tabs >}}


    
<br>

### get

Gets a specific Budget. Prints detailed information about the Budget, including `planned_limits` of the project group or project for the pre-defined period.



> **POST** /cost-analysis/v1/budget/get
>





 {{< tabs " get " >}}



 {{< tab "Response Example" >}}

[BudgetInfo](#BUDGETINFO)
* **budget_id** (string)   `Required` 

* **name** (string)   `Required` 

* **limit** (float)   `Required` 

* **planned_limits** (PlannedLimit)  `Repeated`   `Required` 

* **total_usage_usd_cost** (float)   `Required` 

* **cost_types** (Struct)   `Required` 

* **time_unit** (TimeUnit)   `Required` 

* **start** (string)   `Required` 

* **end** (string)   `Required` 

* **notifications** (BudgetNotification)  `Repeated`   `Required` 

* **tags** (Struct)   `Required` 

* **project_id** (string)   `Required` 

* **project_group_id** (string)   `Required` 

* **domain_id** (string)   `Required` 

* **created_at** (string)   `Required` 

* **updated_at** (string)   `Required` 



{{< highlight json >}}
{
       "budget_id": "budget-d51b6b6a9910",
       "name": "Cloudforet-Budget",
       "limit": 18600.0,
       "planned_limits": [
           {
               "date": "2022-01",
               "limit": 1000.0
           },
           {
               "date": "2022-02",
               "limit": 1100.0
           },
           {
               "date": "2022-03",
               "limit": 1200.0
           },
           {
               "date": "2022-04",
               "limit": 1300.0
           },
           {
               "date": "2022-05",
               "limit": 1400.0
           },
           {
               "date": "2022-06",
               "limit": 1500.0
           },
           {
               "date": "2022-07",
               "limit": 1600.0
           },
           {
               "date": "2022-08",
               "limit": 1700.0
           },
           {
               "date": "2022-09",
               "limit": 1800.0
           },
           {
               "date": "2022-10",
               "limit": 1900.0
           },
           {
               "date": "2022-11",
               "limit": 2000.0
           },
           {
               "date": "2022-12",
               "limit": 2100.0
           }
       ],
       "total_usage_usd_cost": 43412.45,
       "time_unit": "MONTHLY",
       "start": "2022-01",
       "end": "2022-12",
       "tags": {},
       "project_group_id": "pg-812c90990877",
       "domain_id": "domain-58010aa2e451",
       "created_at": "2022-07-18T09:30:56.901Z",
       "updated_at": "2022-07-18T09:30:56.901Z"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### list

Gets a list of all Budgets. You can use a query to get a filtered list of Budgets.



> **POST** /cost-analysis/v1/budget/list
>





 {{< tabs " list " >}}

 {{< tab "Request Example" >}}



[BudgetQuery](./Budget#budgetquery)

* **domain_id** (string)   `Required` 


* **query** (Query)  


* **budget_id** (string)  


* **name** (string)  


* **project_id** (string)  


* **project_group_id** (string)  


* **time_unit** (TimeUnit)  





{{< highlight json >}}
{
   "query": {}
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[BudgetsInfo](#BUDGETSINFO)
* **results** (BudgetInfo)  `Repeated`   `Required` 

* **total_count** (int32)   `Required` 



{{< highlight json >}}
{
       "results": [
           {
               "budget_id": "budget-409e33836ea2",
               "name": "Budget 2 - Monthly",
               "limit": 18600.0,
               "planned_limits": [
                   {
                       "date": "2022-01",
                       "limit": 1000.0
                   },
                   {
                       "date": "2022-02",
                       "limit": 1100.0
                   },
                   {
                       "date": "2022-03",
                       "limit": 1200.0
                   },
                   {
                       "date": "2022-04",
                       "limit": 1300.0
                   },
                   {
                       "date": "2022-05",
                       "limit": 1400.0
                   },
                   {
                       "date": "2022-06",
                       "limit": 1500.0
                   },
                   {
                       "date": "2022-07",
                       "limit": 1600.0
                   },
                   {
                       "date": "2022-08",
                       "limit": 1700.0
                   },
                   {
                       "date": "2022-09",
                       "limit": 1800.0
                   },
                   {
                       "date": "2022-10",
                       "limit": 1900.0
                   },
                   {
                       "date": "2022-11",
                       "limit": 2000.0
                   },
                   {
                       "date": "2022-12",
                       "limit": 2100.0
                   }
               ],
               "total_usage_usd_cost": 43412.45,
               "time_unit": "MONTHLY",
               "start": "2022-01",
               "end": "2022-12",
               "tags": {},
               "project_group_id": "pg-812c90990877",
               "domain_id": "domain-58010aa2e451",
               "created_at": "2022-04-12T06:09:56.917Z",
               "updated_at": "2022-04-12T06:09:56.917Z"
           }
       ],
       "total_count": 6
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### stat





> **POST** /cost-analysis/v1/budget/stat
>






    


<br>
<br>

## Message



### BudgetInfo
* **budget_id** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **limit** (float)   `Required` 

    
* **planned_limits** (PlannedLimit)  `Repeated`    `Required` 

    
* **total_usage_usd_cost** (float)   `Required` 

    
* **cost_types** (Struct)   `Required` 

    
* **time_unit** (TimeUnit)   `Required` 

    
* **start** (string)   `Required` 

    
* **end** (string)   `Required` 

    
* **notifications** (BudgetNotification)  `Repeated`    `Required` 

    
* **tags** (Struct)   `Required` 

    
* **project_id** (string)   `Required` 

    
* **project_group_id** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    
* **updated_at** (string)   `Required` 

    <br>

### BudgetNotification
* **threshold** (float)   `Required` 

    
* **unit** (Unit)   `Required` 

    
* **notification_type** (NotificationType)   `Required` 

    <br>

### BudgetQuery
* **domain_id** (string)   `Required` 

    
* **query** (Query)  

    
* **budget_id** (string)  

    
* **name** (string)  

    
* **project_id** (string)  

    
* **project_group_id** (string)  

    
* **time_unit** (TimeUnit)  

    <br>

### BudgetRequest
* **budget_id** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    <br>

### BudgetStatQuery
* **query** (StatisticsQuery)   `Required` 

    
* **domain_id** (string)   `Required` 

    <br>

### BudgetsInfo
* **results** (BudgetInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>

### CreateBudgetRequest
* **time_unit** (TimeUnit)   `Required` 

    
* **start** (string)   `Required` 

    
* **end** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **name** (string)  

    
* **limit** (float)  

    
* **planned_limits** (PlannedLimit)  `Repeated`   

    
* **cost_types** (Struct)  

    
* **notifications** (BudgetNotification)  `Repeated`   

    
* **tags** (Struct)  

    
* **project_id** (string)  

    
* **project_group_id** (string)  

    <br>

### GetBudgetRequest
* **budget_id** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **only** (string)  `Repeated`   

    <br>

### PlannedLimit
* **date** (string)   `Required` 

    
* **limit** (float)   `Required` 

    <br>

### SetBudgetNotificationRequest
* **budget_id** (string)   `Required` 

    
* **notifications** (BudgetNotification)  `Repeated`    `Required` 

    
* **domain_id** (string)   `Required` 

    <br>

### UpdateBudgetRequest
* **budget_id** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **name** (string)  

    
* **limit** (float)  

    
* **planned_limits** (PlannedLimit)  `Repeated`   

    
* **end** (string)  

    
* **tags** (Struct)  

    <br>
