help_msg = """
NAME
    todocli - Command line client for Microsoft ToDo 
        
SYNOPSIS
   todocli [options] COMMAND ...  
        
   'COMMAND' can be one of the following values:
        ls                  Display all lists  
            
        lst <list_name>     Display all tasks from list
                list_name       Name of the list
            
        md <task>           Sets a task to be due today.
                            This will result in the task being put in the 'My Day' list.
        
        mdr <list_name> <sample size>
                            Randomly assigns tasks to be due today.
            list_name       Name of the list to sample from              
            sample size     # of tasks to assign to "My Day"

        cld <list_name> <task_name>
                            Clears due date for a task
            list_name       Name of list containing task
            task_name       Name of task to clear due date for
        
        cla <list_name>     Clears due dates for all tasks in a list
            list_name       Name of list to clear due dates for
                            
        new <task> [-r time]
                            Create a new task
            task            Task to create. See 'Specifying a task' for details.
            -r time         Set a reminder. See 'Specifying time' for details.              
            
        newl <list_name>    Create a new list
            list_name       Name of the list
                
        complete <task>     Set task status to completed
            task            Task to complete. See 'Specifying a task' for details.
               
        rm <task>           Remove a task
            task            Task to remove. See 'Specifying a task' for details.
                   
OPTIONS
    -h, --help
        Display a usage message.
            
Specifying a task:
    For commands which take 'task' as a parameter, 'task' can be one of the following:
        
    task_name
    list_name/task_name
    task_number
    list_name/task_number
        
    If 'list_name' is omitted, the default task list will be used. 
    'task_number' is the position displayed when specifying option '-n'. 
       
Specifying time:
    For options which take 'time' as a parameter, 'time' can be one of the following:
        
    {n}h
        Current time + n hours. 
        e.g. 1h, 12h. 
        Max: 99h
            
        morning
        Today at 07:00 AM if current time < 07:00 AM, otherwise tomorrow  
            
        tomorrow
            Tomorrow at 07:00 AM
    
        evening
            Today at 06:00 PM if current time < 06:00 PM, otherwise tomorrow
   
        {hour}:{minute}
            Today at {hour}:{minute} if current time < {hour}:{minute}, otherwise tomorrow 
            e.g. 9:30, 09:30, 17:15
            
        {hour}:{minute} am|pm 
            Today at {hour}:{minute} am|pm  if current time < {hour}:{minute} am|pm, otherwise tomorrow
            e.g. 9:30 am, 12:00 am, 10:15 pm
            
        {day}.{month}. {hour}:{minute}
            The given day at {hour}:{minute}
            e.g. 24.12. 12:00
            e.g. 7.4.   9:15
        
        {day}.{month}.{year}
            The given day at 7:00 am
            e.g. 22.12.2020
            e.g. 01.01.21
        """
