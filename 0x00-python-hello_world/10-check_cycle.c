#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"
/**
 * check_cycle - check if is a cicle
 * @list: pointer of the singly linked
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
    listint_t *fast;
    listint_t *slow;

    if (list == NULL)
        return(0);

    slow = list;
    fast = list;

    while (slow->next != NULL && fast->next != NULL && fast->next->next != NULL)
    {
        slow = slow->next;
        fast = fast->next->next;
        if (fast == slow)
            return(1);
    }
    return(0);
}