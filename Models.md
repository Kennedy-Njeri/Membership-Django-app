Model Architectural Planning


Membership
   -slug/id
   -type (free, pro, enterprise)
   -price
   -stripe plan id
   
UserMembership
    -user   (foreign key to default user)
    -stripe customer id
    -membership type (foreign key to membership)
    
Subscription
    -user membership 
    -stripe subscription id (foreignkey to UserMembership)
    -active
    
Course
    -slug
    -title
    -description
    -allowed memberships (foreignkey to memberships)
    
Lesson
    -slug
    -title
    -course (foreignkey to course)
    -position
    -video
    -thumbnail
    

   
    
    
   
   