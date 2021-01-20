#include<stdio.h>
struct node
{
    int data;
    node *next;
};
int main()
{
    node *top=NULL,*tptr,*nptr;
    int i,n,x;
    for(i=0;i<5;i++)
    {
        nptr=new(node);
        scanf("%d",&nptr->data);
        nptr->next=NULL;
        if(i==0)
        {
            top=nptr;
            tptr=nptr;
        }
        else
        {
            tptr->next=nptr;
            tptr=nptr;
        }
    }
    printf("\nYour Queue is .\n");
    tptr=top;
    while(tptr!=NULL)
    {
        printf("%d ",tptr->data);
        tptr=tptr->next;
    }
    printf("\nFor queue enter 1 , for dequeue enter 2 & for exit enter 3.\n");
    while(scanf("%d",&n)!=-1){
    if(n==1)
    {
        nptr=new(node);
        scanf("%d",&nptr->data);
        nptr->next=NULL;
        tptr=top;

        while(tptr->next!=NULL)
        {
        tptr=tptr->next;
        }
        nptr->next=tptr->next;
        tptr->next=nptr;
        tptr=tptr->next;
        printf("\nAfter queue.\n");
        tptr=top;
        while(tptr!=NULL)
        {
            printf("%d ",tptr->data);
            tptr=tptr->next;
        }
        printf("\n");
    }
    if(n==2)
    {
        if(top->next==NULL)
        {
            printf("\nQueue is empty.\n");
        }
        else
        {
            top=top->next;
            tptr=top;
            printf("\nAfter dequeue.\n");
            while(tptr!=NULL)
            {
                printf("%d ",tptr->data);
                tptr=tptr->next;
            }
            printf("\n");
        }
    }
    if(n==3)
    {
        return 0;
    }
    printf("\nfor queue enter 1 , for dequeue enter 2 & for exit enter 3.\n");
    }
    return 0;
}

