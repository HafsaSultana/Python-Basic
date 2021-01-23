<<<<<<< HEAD
#include<stdio.h>
#include<malloc.h>
struct node
{
    int data;
    struct node *link;
};
int main()
{
     struct node *t,*f,*e;
     struct node *t1,*t2,*t3;

     for(int i=0;i<5;i++)
     {
         t=(struct node*)malloc(sizeof(node));
         //t->data=i+1;
         scanf("%d",&t->data);
         t->link=NULL;
         if(i==0)
         {
             f=t;
         }
         else
         {
            e->link=t;
         }
         e=t;
     }
     t1=f->link;
     t2=f->link->link->link;
     t1->link=t2;
     while(f!=NULL)
     {
         printf("%d  ",f->data);
         f=f->link;
     }
}
=======
#include<stdio.h>
#include<malloc.h>
struct node
{
    int data;
    struct node *link;
};
int main()
{
     struct node *t,*f,*e;
     struct node *t1,*t2,*t3;

     for(int i=0;i<5;i++)
     {
         t=(struct node*)malloc(sizeof(node));
         //t->data=i+1;
         scanf("%d",&t->data);
         t->link=NULL;
         if(i==0)
         {
             f=t;
         }
         else
         {
            e->link=t;
         }
         e=t;
     }
     t1=f->link;
     t2=f->link->link->link;
     t1->link=t2;
     while(f!=NULL)
     {
         printf("%d  ",f->data);
         f=f->link;
     }
}
>>>>>>> 745d9055431b073d56692add3b0c158869ea679a
