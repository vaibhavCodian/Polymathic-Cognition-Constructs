## For TF Module Generation PRMPT example

```markdown
Deeply Analyze The Attached Repo content for terraform-google-sql-db to provision cloud-sql in gcp
Specifically :
sql-db/terraform-google-sql-db                               (For Reference)
sql-db/terraform-google-sql-db/modules              ( For Reference reference of the modules to be created )
sql-db/terraform-google-sql-db/example              ( For Reference Refernece Of the Example To )
sql-db/sql-db/                                                              ( path where the re-implemented code is to be stored based on contextual changes of making thing dynamic
sql-db/sql-db/modules
based on above generated requirements similarly;
########################################################################################################################################
-> Use Terraform Dynamic Block and optional Variable such that in Tfvars we can use map of object to provision multiple resource of same type
a single map of object for a single module with ability to provison multiple resource;
-> use of Dynamic Block to modularization based on above Requirement, and cover each parameter for each resource variablized and structured similar to above;
-> in envioment /dev/ main.tf and terraform.vars have proper multi-line comment  based on resource name in simple word ;
########################################################################################################################################
Specifically update :
------------------------------------------------------------------------
/sql-db/sql-db/modules/postgresql/main.tf
/sql-db/sql-db/modules/postgresql/outputs.tf
/sql-db/sql-db/modules/postgresql/variables.tf
/sql-db/sql-db/modules/postgresql/read_replica.tf
------------------------------------------------------------------------

make the code such clean and easy to understand first provide updated code for postgresql cloud sql module and a simple example in existing /sql-db/sql-db/modules/postgresql codebase:
path where changes are to be made and etc
------------------------------------------------------------------------
-> 1. update folder structure
-> 2. use map of object to make everyting consitent even for outputs, tfvars and etc;
-> provide content for the code in /sql-db/sql-db/modules/postgresql codebase for each file with only required clean changes based on context, without placeholder and unrequired changes;
```
