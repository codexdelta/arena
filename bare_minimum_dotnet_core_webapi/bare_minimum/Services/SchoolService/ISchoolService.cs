using System.Collections.Generic;
using System.Threading.Tasks;
using bare_minimum.Dtos.School;
using bare_minimum.Models;

namespace bare_minimum.Services.SchoolService
{
    public interface ISchoolService
    {
        Task<List<School>> AddSchool(AddSchoolDto addSchool);
    }
}