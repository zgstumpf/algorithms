List<int> numbers = new List<int> {1, 1, 1, 3, 3, 1};

for(int i = 0; i < numbers.Count;i++)
{
    int current = numbers[i];
    while(numbers.Where(n=>n.Equals(current)).Count() > 1)
    {
        numbers.Remove(current);
        numbers.Remove(current);
        numbers.Add(current+1);
        i = 0;
    }
}

foreach(int i in numbers)
{
    Console.WriteLine(i);
}
