using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using NBitcoin;

namespace BitchainLearning
{
    class Program
    {
        static void Main(string[] args)
        {
            var privateKey = new Key();
            Console.WriteLine("Hello world! " + privateKey.GetWif(Network.Main));
            Console.WriteLine("And my public key is " + privateKey.PubKey);
            Console.ReadLine();
        }
    }
}
