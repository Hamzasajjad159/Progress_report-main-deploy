EmpUsers: Name, EMails etc
Workdetail: Title (e.g photography, editing, marketing etc)
Products: Sku, title, date_added, date_completed (whole pipeling is realted to product work and users)
Progress: product_id, user_id, work_id, status (ongoing or complete)(work_id will change based on which work is complete)
EmpPosition: title (Photographer, editor, manager etc)
userPosition: user_id, position_id, work_id (in case user work in multiple positions)
progressUpdated: product_id, user_id, date_changed, status_changed_to, work_id (this is to keep log of every change that can be used for user reports and analytics)
