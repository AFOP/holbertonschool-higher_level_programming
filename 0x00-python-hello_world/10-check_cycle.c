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
    while (list != NULL)
    {
        list = list->next;
        if (list->next == NULL)
            return(0);
        if (list->next != NULL)
            break;
    }
    return(1);
}
