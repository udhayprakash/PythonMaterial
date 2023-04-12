Authors table:
id: integer, primary key
name: string, required
email: string, required, unique

Articles table:
id: integer, primary key
title: string, required
body: text, required
created_at: datetime, default: current timestamp
updated_at: datetime, default: current timestamp, on update: current timestamp
author_id: integer, foreign key to Authors table

Comments table:
id: integer, primary key
body: text, required
created_at: datetime, default: current timestamp
updated_at: datetime, default: current timestamp, on update: current timestamp
article_id: integer, foreign key to Articles table
author_id: integer, foreign key to Authors table
