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
            nptr->next=top;
            top=nptr;
            tptr=nptr;
        }
    }
    printf("\nYour stack is .\n");
    tptr=top;
    while(tptr!=NULL)
    {
        printf("%d ",tptr->data);
        tptr=tptr->next;
    }

    printf("\nfor push enter 1 & for pop enter 2 & for exit enter 3.\n");
    while(scanf("%d",&n)!=-1)
    {
    if(n==1)
    {
        nptr=new(node);
        scanf("%d",&nptr->data);
        nptr->next=NULL;

        nptr->next=top;
        top=nptr;
        tptr=nptr;
        printf("\nAfter push.\n");
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
            printf("Stack is empty.");
        }
        else
        {
            top=top->next;
            tptr=top;
            printf("\nAfter pop.\n");
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
    printf("\nfor push enter 1 & for pop enter 2 & for exit enter 3.\n");
    }
    return 0;
}
