List<int?> numbers = new List<int?> { 1, 1, 0, 5, 5, 5, 5 }; // -> 1,1,0,5,5,5,5 -> 0,2,7

PrintIntList(numbers);
Merge(numbers);
Console.WriteLine("->");
PrintIntList(numbers);

// If there are two of the same integer, they are merged and get increased by 1
// Example: 5,5 -> 6
// Merge loops through list until there are no more possible merges
// Example: 5,5,5,5 -> 6,6 -> 7
void Merge(List<int?> list)
{
    numbers.Sort();
    while (HasDuplicates(numbers))
    {
        for (int i = 0; i < numbers.Count - 1; i++)
        {
            int? current = numbers[i];
            if (current != null)
            {
                for (int j = i + 1; j < numbers.Count; j++)
                {
                    int? contender = numbers[j];
                    if (contender != null && contender == current)
                    {
                        // merge current and contender
                        current++;
                        numbers[i] = current;
                        numbers[j] = null;
                    }
                }
            }
        }
        RemoveNulls(numbers);
    }
}

bool HasDuplicates(List<int?> intList)
{
    for (int i = 0; i < intList.Count; i++)
    {
        int? current = intList[i];
        if(current != null)
        {
            for (int j = i + 1; j < intList.Count; j++)
            {
                if (intList[i] == intList[j])
                {
                    return true;
                }
            }
        }
    }
    return false;
}

void RemoveNulls(List<int?> intList)
{
    intList.RemoveAll(item => item == null);
}

void PrintIntList(List<int?> intList)
{
    foreach (int? i in intList)
    {
        if(i == null)
        {
            Console.WriteLine("null");
        }
        else
        {
            Console.WriteLine(i);
        }
    }
}
