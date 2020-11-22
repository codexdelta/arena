using System.Collections.Generic;
using System.Threading.Tasks;
using bare_minimum.Models;
using bare_minimum.Dtos.School;
using bare_minimum.Data;

namespace bare_minimum.Services.SchoolService
{
    public class SchoolService : ISchoolService
    {
        private readonly DataContext _context;
        public SchoolService(DataContext context)
        {
            _context = context;
        }
        public async Task<List<School>> AddSchool(AddSchoolDto addSchool)
        {
            School school = new School 
            {
                Name=addSchool.Name,
            };

            await _context.SchoolMaster.AddAsync(school);
            await _context.SaveChangesAsync();
            List<School> viva = new List<School>();
            viva.Add(school);
            return viva;
        }
    }
}