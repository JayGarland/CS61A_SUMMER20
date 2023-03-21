CREATE TABLE parents AS
  SELECT "abraham" AS parent, "barack" AS child UNION
  SELECT "abraham"          , "clinton"         UNION
  SELECT "delano"           , "herbert"         UNION
  SELECT "fillmore"         , "abraham"         UNION
  SELECT "fillmore"         , "delano"          UNION
  SELECT "fillmore"         , "grover"          UNION
  SELECT "eisenhower"       , "fillmore";

CREATE TABLE dogs AS
  SELECT "abraham" AS name, "long" AS fur, 26 AS height UNION
  SELECT "barack"         , "short"      , 52           UNION
  SELECT "clinton"        , "long"       , 47           UNION
  SELECT "delano"         , "long"       , 46           UNION
  SELECT "eisenhower"     , "short"      , 35           UNION
  SELECT "fillmore"       , "curly"      , 32           UNION
  SELECT "grover"         , "short"      , 28           UNION
  SELECT "herbert"        , "curly"      , 31;

CREATE TABLE sizes AS
  SELECT "toy" AS size, 24 AS min, 28 AS max UNION
  SELECT "mini"       , 28       , 35        UNION
  SELECT "medium"     , 35       , 45        UNION
  SELECT "standard"   , 45       , 60;


-- The size of each dog
CREATE TABLE size_of_dogs AS
  SELECT name, size FROM dogs as dog, sizes as s WHERE dog.height > s.min AND dog.height <= s.max;
--distinct the tables then compare with one another attribute of each own column value

-- All dogs with parents ordered by decreasing height of their parent
CREATE TABLE by_parent_height AS
  SELECT part.child From parents AS part, dogs AS dog WHERE dog.name = part.parent ORDER BY dog.height DESC;
  --all dogs with parents so the object is the child, and how to tell the relationship is to evaluate it by equaling the names of them and then order


-- Filling out this helper table is optional
--since "barack and clinton..." instead of "clinton and barack..." so a.child should be less than b.child 
CREATE TABLE siblings AS
  SELECT a.child as sibl1, b.child as sibl2 FROM parents as a, parents as b WHERE a.parent = b.parent AND a.child < b.child;

-- Sentences about siblings that are the same size
CREATE TABLE sentences AS
  SELECT sibl1 || " and " || sibl2 || " are " || s1.size || " siblings" FROM size_of_dogs as s1, size_of_dogs as s2, siblings WHERE s1.size = s2.size AND s1.name = sibl1 AND s2.name = sibl2;


-- Ways to stack 4 dogs to a height of at least 170, ordered by total height
CREATE TABLE stacks_helper(dogs, stack_height, last_height, n);

-- Add your INSERT INTOs here


CREATE TABLE stacks AS
  SELECT "REPLACE THIS LINE WITH YOUR SOLUTION";

