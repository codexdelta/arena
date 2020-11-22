using bare_minimum.Models;
using Microsoft.EntityFrameworkCore;

namespace bare_minimum.Data
{
    public class DataContext : DbContext
    {
        // building the constructor
        public DataContext(DbContextOptions<DataContext> options) : base(options) {}

        public DbSet<Student> StudentMaster {get; set;}
        public DbSet<School> SchoolMaster {get; set;}

    }
}