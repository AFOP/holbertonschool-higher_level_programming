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
    listint_t *current;

    current = list;
    if (list == NULL)
        return(0);
    while (list != NULL)
    {
        if (list->next == NULL)
            return(0);
        list = list->next;
        if (current == list)
            break;
    }
    return(1);
}
