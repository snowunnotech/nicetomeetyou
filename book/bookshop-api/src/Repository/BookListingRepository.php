<?php

namespace App\Repository;

use App\Entity\BookListing;
use Doctrine\Bundle\DoctrineBundle\Repository\ServiceEntityRepository;
use Doctrine\Persistence\ManagerRegistry;

/**
 * @method BookListing|null find($id, $lockMode = null, $lockVersion = null)
 * @method BookListing|null findOneBy(array $criteria, array $orderBy = null)
 * @method BookListing[]    findAll()
 * @method BookListing[]    findBy(array $criteria, array $orderBy = null, $limit = null, $offset = null)
 */
class BookListingRepository extends ServiceEntityRepository
{
    public function __construct(ManagerRegistry $registry)
    {
        parent::__construct($registry, BookListing::class);
    }

    // /**
    //  * @return BookListing[] Returns an array of BookListing objects
    //  */
    /*
    public function findByExampleField($value)
    {
        return $this->createQueryBuilder('b')
            ->andWhere('b.exampleField = :val')
            ->setParameter('val', $value)
            ->orderBy('b.id', 'ASC')
            ->setMaxResults(10)
            ->getQuery()
            ->getResult()
        ;
    }
    */

    /*
    public function findOneBySomeField($value): ?BookListing
    {
        return $this->createQueryBuilder('b')
            ->andWhere('b.exampleField = :val')
            ->setParameter('val', $value)
            ->getQuery()
            ->getOneOrNullResult()
        ;
    }
    */
}
