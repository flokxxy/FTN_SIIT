package com.example.demo.zadatak1;

import com.example.demo.model.Accommodation;
import com.example.demo.model.Client;
import com.example.demo.model.DateRange;
import com.example.demo.model.Reservation;
import com.example.demo.repository.ReservationRepository;
import com.example.demo.service.AccommodationService;
import com.example.demo.service.ReservationService;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.ArgumentCaptor;
import org.mockito.Mock;
import org.mockito.junit.jupiter.MockitoExtension;

import java.util.ArrayList;
import java.util.List;
import java.time.LocalDate;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertThrows;
import static org.junit.jupiter.api.Assertions.assertTrue;
import static org.mockito.ArgumentMatchers.any;
import static org.mockito.Mockito.never;
import static org.mockito.Mockito.verify;
import static org.mockito.Mockito.verifyNoInteractions;
import static org.mockito.Mockito.when;

@ExtendWith(MockitoExtension.class)
class ReservationServiceTest {

    private static final long ACCOMMODATION_ID = 1L;

    @Mock
    private ReservationRepository repository;

    @Mock
    private AccommodationService accommodationService;

    private ReservationService reservationService;
    private Client client;
    private DateRange dateRange;

    @BeforeEach
    void setUp() {
        reservationService = new ReservationService(repository, accommodationService);
        client = new Client(1L, "Test Client", "test", "password");
        dateRange = new DateRange(
                LocalDate.of(2024, 1, 15),
                LocalDate.of(2024, 1, 20)
        );
    }

    @Test
    void shouldThrowExceptionWhenStartDateAfterEndDate() {
        DateRange range = new DateRange(
                LocalDate.of(2024, 1, 25),
                LocalDate.of(2024, 1, 20)
        );

        assertThrows(IllegalArgumentException.class,
                () -> reservationService.createReservation(ACCOMMODATION_ID, client, range));

        verifyNoInteractions(repository, accommodationService);
    }

    @Test
    void shouldReturnFalseWhenAccommodationIsNotAvailable() {
        when(accommodationService.isAccommodationAvailable(ACCOMMODATION_ID, dateRange)).thenReturn(false);

        boolean reservationCreated = reservationService.createReservation(ACCOMMODATION_ID, client, dateRange);

        assertFalse(reservationCreated);
        verify(accommodationService).isAccommodationAvailable(ACCOMMODATION_ID, dateRange);
        verify(repository, never()).findAllByClientId(client.getId());
        verify(repository, never()).save(any(Reservation.class));
        verify(accommodationService, never()).getById(ACCOMMODATION_ID);
        verify(accommodationService, never()).save(any(Accommodation.class));
    }

    @Test
    void shouldReturnFalseWhenClientHasOverlappingReservation() {
        Reservation existingReservation = new Reservation(
                1L,
                client,
                LocalDate.of(2024, 1, 18),
                LocalDate.of(2024, 1, 22)
        );

        when(accommodationService.isAccommodationAvailable(ACCOMMODATION_ID, dateRange)).thenReturn(true);
        when(repository.findAllByClientId(client.getId())).thenReturn(List.of(existingReservation));

        boolean reservationCreated = reservationService.createReservation(ACCOMMODATION_ID, client, dateRange);

        assertFalse(reservationCreated);
        verify(repository).findAllByClientId(client.getId());
        verify(repository, never()).save(any(Reservation.class));
        verify(accommodationService, never()).getById(ACCOMMODATION_ID);
        verify(accommodationService, never()).save(any(Accommodation.class));
    }

    @Test
    void shouldReturnFalseWhenClientReservationEndsOnRequestedStartDate() {
        Reservation existingReservation = new Reservation(
                1L,
                client,
                LocalDate.of(2024, 1, 10),
                LocalDate.of(2024, 1, 15)
        );

        when(accommodationService.isAccommodationAvailable(ACCOMMODATION_ID, dateRange)).thenReturn(true);
        when(repository.findAllByClientId(client.getId())).thenReturn(List.of(existingReservation));

        boolean reservationCreated = reservationService.createReservation(ACCOMMODATION_ID, client, dateRange);

        assertFalse(reservationCreated);
        verify(repository, never()).save(any(Reservation.class));
    }

    @Test
    void shouldReturnFalseWhenClientReservationStartsOnRequestedEndDate() {
        Reservation existingReservation = new Reservation(
                1L,
                client,
                LocalDate.of(2024, 1, 20),
                LocalDate.of(2024, 1, 25)
        );

        when(accommodationService.isAccommodationAvailable(ACCOMMODATION_ID, dateRange)).thenReturn(true);
        when(repository.findAllByClientId(client.getId())).thenReturn(List.of(existingReservation));

        boolean reservationCreated = reservationService.createReservation(ACCOMMODATION_ID, client, dateRange);

        assertFalse(reservationCreated);
        verify(repository, never()).save(any(Reservation.class));
    }

    @Test
    void shouldCreateReservationWhenClientHasNonOverlappingReservation() {
        Reservation existingReservation = new Reservation(
                1L,
                client,
                LocalDate.of(2024, 1, 10),
                LocalDate.of(2024, 1, 14)
        );
        Accommodation accommodation = createAccommodation();

        when(accommodationService.isAccommodationAvailable(ACCOMMODATION_ID, dateRange)).thenReturn(true);
        when(repository.findAllByClientId(client.getId())).thenReturn(List.of(existingReservation));
        when(accommodationService.getById(ACCOMMODATION_ID)).thenReturn(accommodation);

        boolean reservationCreated = reservationService.createReservation(ACCOMMODATION_ID, client, dateRange);

        assertTrue(reservationCreated);
        verify(repository).save(any(Reservation.class));
        verify(accommodationService).save(accommodation);
        assertEquals(1, accommodation.getReservations().size());
    }

    @Test
    void shouldCreateReservationSuccessfully() {
        Accommodation accommodation = createAccommodation();

        when(accommodationService.isAccommodationAvailable(ACCOMMODATION_ID, dateRange)).thenReturn(true);
        when(repository.findAllByClientId(client.getId())).thenReturn(List.of());
        when(accommodationService.getById(ACCOMMODATION_ID)).thenReturn(accommodation);

        boolean reservationCreated = reservationService.createReservation(ACCOMMODATION_ID, client, dateRange);

        assertTrue(reservationCreated);

        ArgumentCaptor<Reservation> reservationCaptor = ArgumentCaptor.forClass(Reservation.class);
        verify(repository).save(reservationCaptor.capture());

        Reservation savedReservation = reservationCaptor.getValue();
        assertEquals(client, savedReservation.getClient());
        assertEquals(dateRange.getStartDate(), savedReservation.getStartDate());
        assertEquals(dateRange.getEndDate(), savedReservation.getEndDate());

        verify(accommodationService).getById(ACCOMMODATION_ID);
        verify(accommodationService).save(accommodation);
        assertEquals(savedReservation, accommodation.getReservations().get(0));
    }

    @Test
    void shouldCreateReservationWhenStartDateEqualsEndDate() {
        DateRange oneDayRange = new DateRange(
                LocalDate.of(2024, 1, 15),
                LocalDate.of(2024, 1, 15)
        );
        Accommodation accommodation = createAccommodation();

        when(accommodationService.isAccommodationAvailable(ACCOMMODATION_ID, oneDayRange)).thenReturn(true);
        when(repository.findAllByClientId(client.getId())).thenReturn(List.of());
        when(accommodationService.getById(ACCOMMODATION_ID)).thenReturn(accommodation);

        boolean reservationCreated = reservationService.createReservation(ACCOMMODATION_ID, client, oneDayRange);

        assertTrue(reservationCreated);
        verify(repository).save(any(Reservation.class));
        verify(accommodationService).save(accommodation);
    }

    private Accommodation createAccommodation() {
        return new Accommodation(
                ACCOMMODATION_ID,
                "Zlatibor",
                new DateRange(LocalDate.of(2024, 1, 1), LocalDate.of(2024, 1, 31)),
                new ArrayList<>()
        );
    }
}
